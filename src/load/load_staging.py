import os
import json
from pathlib import Path
import psycopg2
from psycopg2.extras import execute_values

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw" / "carbon_intensity"


def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))



def load_staging():
    print("BASE_DIR:", BASE_DIR)
    print("RAW_DIR:", RAW_DIR)

    files = sorted(RAW_DIR.glob("national_intensity_*.json"))
    print("FILES FOUND:", files)

    if not files:
        print("No raw files found")
        return

    rows = []

    for file_path in files:
        with open(file_path) as f:
            payload = json.load(f)

        for record in payload.get("data", []):
            rows.append((
                record["from"],
                record["to"],
                0,                      # region_id (0 = national)
                "United Kingdom",       # region_name
                record["intensity"].get("forecast"),
                record["intensity"].get("actual"),
                record["intensity"].get("index"),
            ))

    if not rows:
        print("No rows to insert")
        return

    insert_query = """
        INSERT INTO staging.stg_carbon_intensity (
            period_from,
            period_to,
            region_id,
            region_name,
            forecast_intensity,
            actual_intensity,
            intensity_index
        )
        VALUES %s
    """

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            execute_values(cursor, insert_query, rows)
        conn.commit()
        print(f"{len(rows)} rows inserted into staging.stg_carbon_intensity")
    finally:
        conn.close()


if __name__ == "__main__":
    load_staging()

