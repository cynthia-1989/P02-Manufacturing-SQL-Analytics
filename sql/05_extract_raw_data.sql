SELECT
    -- Production
    pr.run_id,
    pr.run_date,
    pr.shift,
    pr.actual_units,
    pr.defective_units,
    pr.efficiency_pct,

    -- Quality
    qc.sample_size,
    qc.failed,
    qc.defect_type,

    -- Plant
    pl.plant_name,
    pl.city,

    -- Product
    p.product_name,
    p.category

FROM manufacturing.production_runs pr

JOIN manufacturing.quality_checks qc
    ON pr.run_id = qc.run_id

JOIN manufacturing.plants pl
    ON pr.plant_id = pl.plant_id

JOIN manufacturing.products p
    ON pr.product_id = p.product_id

ORDER BY pr.run_date, pr.run_id

LIMIT 50;