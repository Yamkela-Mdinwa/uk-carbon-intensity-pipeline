INSERT INTO marts.dim_datetime (
    datetime_utc,
    date,
    hour,
    minute,
    day,
    month,
    year
)
SELECT DISTINCT
    s.period_from AS datetime_utc,
    s.period_from::DATE AS date,
    EXTRACT(HOUR FROM s.period_from)::INT AS hour,
    EXTRACT(MINUTE FROM s.period_from)::INT AS minute,
    EXTRACT(DAY FROM s.period_from)::INT AS day,
    EXTRACT(MONTH FROM s.period_from)::INT AS month,
    EXTRACT(YEAR FROM s.period_from)::INT AS year
FROM staging.stg_carbon_intensity s
ON CONFLICT (datetime_utc) DO NOTHING;
