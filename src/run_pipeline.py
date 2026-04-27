import subprocess
import sys
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv


# -----------------------------
# BASE CONFIG
# -----------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
os.chdir(BASE_DIR)

# Load environment variables from .env file
load_dotenv(BASE_DIR / ".env")



LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / f"pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Neon connection string (recommended: override via env var)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# -----------------------------
# SQL TRANSFORM SCRIPTS (ORDER MATTERS)
# -----------------------------

SQL_FILES = [
    "insert_dim_datetime.sql",
    "insert_dim_region.sql",
    "insert_fact_carbon_intensity.sql",
]

# -----------------------------
# LOGGING
# -----------------------------

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)

    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

# -----------------------------
# RUN COMMAND WRAPPER
# -----------------------------

def run_command(command, step_name):
    log(f"START: {step_name}")

    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.stdout:
            log(result.stdout.strip())

        if result.stderr:
            log(result.stderr.strip())

        log(f"SUCCESS: {step_name}")

    except subprocess.CalledProcessError as e:
        log(f"FAILED: {step_name}")
        log(e.stderr.strip())
        sys.exit(1)

# -----------------------------
# PIPELINE EXECUTION
# -----------------------------

def main():
    log("PIPELINE STARTED")

    # -------------------------
    # 1. EXTRACT
    # -------------------------
    run_command(
        [sys.executable, str(BASE_DIR / "src/extract/extract.py")],
        "Extract raw carbon intensity data"
    )

    # -------------------------
    # 2. LOAD STAGING (NEON)
    # -------------------------
    run_command(
        [sys.executable, str(BASE_DIR / "src/load/load_staging.py")],
        "Load staging tables (Neon)"
    )

    # -------------------------
    # 3. TRANSFORM (NEON via psql)
    # -------------------------
    for sql_file in SQL_FILES:
        run_command(
            [
                "psql",
                DATABASE_URL,
                "-f",
                str(BASE_DIR / f"src/transform/{sql_file}")
            ],
            f"Run {sql_file}"
        )

    log("PIPELINE FINISHED SUCCESSFULLY")

# -----------------------------
# ENTRY POINT
# -----------------------------

if __name__ == "__main__":
    main()
