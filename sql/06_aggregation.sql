-- ================================================================
-- 06_aggregation.sql
-- P02 Manufacturing SQL — Aggregation Queries
-- Purpose: Defect rates and efficiency by plant and shift
-- ================================================================

-- 1. Defect rate by plant
SELECT
    pl.plant_name,
    COUNT(pr.run_id) AS total_runs,
    SUM(pr.actual_units) AS total_units_produced,
    SUM(pr.defective_units) AS total_defective_units,
    ROUND(
        SUM(pr.defective_units) * 100.0 / NULLIF(SUM(pr.actual_units), 0),
        2
    ) AS defect_rate_pct,
    ROUND(AVG(pr.efficiency_pct), 2) AS avg_efficiency_pct
FROM manufacturing.production_runs pr
JOIN manufacturing.plants pl
    ON pr.plant_id = pl.plant_id
GROUP BY pl.plant_name
ORDER BY defect_rate_pct DESC;


-- 2. Defect rate and efficiency by shift
SELECT
    pr.shift,
    COUNT(pr.run_id) AS total_runs,
    SUM(pr.actual_units) AS total_units_produced,
    SUM(pr.defective_units) AS total_defective_units,
    ROUND(
        SUM(pr.defective_units) * 100.0 / NULLIF(SUM(pr.actual_units), 0),
        2
    ) AS defect_rate_pct,
    ROUND(AVG(pr.efficiency_pct), 2) AS avg_efficiency_pct
FROM manufacturing.production_runs pr
GROUP BY pr.shift
ORDER BY defect_rate_pct DESC;


-- 3. Defect rate by product category
SELECT
    p.category,
    COUNT(pr.run_id) AS total_runs,
    SUM(pr.actual_units) AS total_units_produced,
    SUM(pr.defective_units) AS total_defective_units,
    ROUND(
        SUM(pr.defective_units) * 100.0 / NULLIF(SUM(pr.actual_units), 0),
        2
    ) AS defect_rate_pct
FROM manufacturing.production_runs pr
JOIN manufacturing.products p
    ON pr.product_id = p.product_id
GROUP BY p.category
ORDER BY defect_rate_pct DESC;