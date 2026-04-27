import json
import requests
from pathlib import Path
from datetime import datetime, timezone


BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw" / "carbon_intensity"


def fetch_national_intensity():
    url = "https://api.carbonintensity.org.uk/intensity"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def save_raw_json(data):
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    file_path = RAW_DIR / f"national_intensity_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    data = fetch_national_intensity()
    save_raw_json(data)
    print("Raw carbon intensity data extracted")

