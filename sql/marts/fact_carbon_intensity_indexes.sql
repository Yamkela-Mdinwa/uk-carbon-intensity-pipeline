CREATE INDEX IF NOT EXISTS idx_fact_datetime
    ON marts.fact_carbon_intensity (datetime_id);

CREATE INDEX IF NOT EXISTS idx_fact_region
    ON marts.fact_carbon_intensity (region_id);

CREATE INDEX IF NOT EXISTS idx_fact_measure
    ON marts.fact_carbon_intensity (measure_type_id);

