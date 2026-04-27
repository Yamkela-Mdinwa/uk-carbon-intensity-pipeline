CREATE TABLE marts.fact_carbon_intensity (
    carbon_fact_id SERIAL PRIMARY KEY,

    datetime_id INTEGER NOT NULL,
    region_id INTEGER NOT NULL,

    actual_intensity INTEGER,
    forecast_intensity INTEGER,
    forecast_error INTEGER,

    CONSTRAINT fk_datetime
        FOREIGN KEY (datetime_id)
        REFERENCES marts.dim_datetime (datetime_id),

    CONSTRAINT fk_region
        FOREIGN KEY (region_id)
        REFERENCES marts.dim_region (region_id)
);
