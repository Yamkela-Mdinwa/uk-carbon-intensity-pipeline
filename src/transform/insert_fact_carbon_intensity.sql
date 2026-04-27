INSERT INTO marts.fact_carbon_intensity (
    datetime_id,
    region_id,
    actual_intensity,
    forecast_intensity,
    forecast_error
)
SELECT
    d.datetime_id,
    r.region_id,

    MAX(s.actual_intensity) AS actual_intensity,
    MAX(s.forecast_intensity) AS forecast_intensity,

    CASE
        WHEN MAX(s.actual_intensity) IS NOT NULL
         AND MAX(s.forecast_intensity) IS NOT NULL
        THEN MAX(s.actual_intensity) - MAX(s.forecast_intensity)
        ELSE NULL
    END AS forecast_error

FROM staging.stg_carbon_intensity s
JOIN marts.dim_datetime d
    ON d.datetime_utc = s.period_from
JOIN marts.dim_region r
    ON r.region_name = s.region_name

GROUP BY d.datetime_id, r.region_id

ON CONFLICT (datetime_id, region_id)
DO UPDATE SET
    actual_intensity = EXCLUDED.actual_intensity,
    forecast_intensity = EXCLUDED.forecast_intensity,
    forecast_error = EXCLUDED.forecast_error;
