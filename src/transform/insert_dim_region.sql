INSERT INTO marts.dim_region (region_name)
SELECT DISTINCT region_name
FROM staging.stg_carbon_intensity
ON CONFLICT (region_name) DO NOTHING;
