CREATE INDEX IF NOT EXISTS idx_stg_ci_period_from
    ON staging.stg_carbon_intensity (period_from);

CREATE INDEX IF NOT EXISTS idx_stg_ci_region
    ON staging.stg_carbon_intensity (region_id);

