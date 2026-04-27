CREATE TABLE IF NOT EXISTS staging.stg_carbon_intensity (
    stg_id          BIGSERIAL PRIMARY KEY,
    period_from     TIMESTAMPTZ NOT NULL,
    period_to       TIMESTAMPTZ NOT NULL,
    region_id       INTEGER NOT NULL,
    region_name     TEXT NOT NULL,
    forecast_intensity INTEGER,
    actual_intensity   INTEGER,
    intensity_index    TEXT,
    extracted_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

