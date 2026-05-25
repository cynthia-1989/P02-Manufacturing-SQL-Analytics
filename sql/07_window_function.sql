-- ================================================================
-- 07_window_function.sql
-- P02 Manufacturing SQL — Window Function
-- Purpose: Rank production runs by efficiency within each plant
-- ================================================================

SELECT
    pr.run_id,
    pr.run_date,
    pl.plant_name,
    pr.shift,
    pr.actual_units,
    pr.defective_units,
    pr.efficiency_pct,

    RANK() OVER (
        PARTITION BY pr.plant_id
        ORDER BY pr.efficiency_pct DESC NULLS LAST
    ) AS efficiency_rank_within_plant

FROM manufacturing.production_runs pr
JOIN manufacturing.plants pl
    ON pr.plant_id = pl.plant_id

ORDER BY pl.plant_name, efficiency_rank_within_plant
LIMIT 100;