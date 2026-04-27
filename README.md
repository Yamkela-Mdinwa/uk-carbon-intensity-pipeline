# UK Carbon Intensity Data Pipeline & Analytics Dashboard

An end-to-end data pipeline and analytics system designed to monitor UK carbon intensity, evaluate forecasting performance, and support carbon-aware decision making.

This project demonstrates how raw environmental data can be transformed into actionable insights through data engineering, modelling, and visualisation.

---

## 📊 Dashboard Preview

[Dashboard](powerbi/screenshots/dashboard.png)

---

## 🌍 Why This Project Matters

Energy systems are becoming increasingly complex and carbon-aware.

Understanding when carbon intensity is high or low enables:
- Smarter energy usage
- Reduced environmental impact
- Better operational planning

This project bridges the gap between raw carbon data and real-world decision making.

---

## 🛠️ What I Built

- Automated data pipeline using the UK Carbon Intensity API
- Data ingestion and storage in PostgreSQL (Neon)
- Data modelling using a star schema (fact and dimension tables)
- Forecast evaluation metrics including accuracy, error, and bias
- Interactive Power BI dashboard for monitoring and analysis

---

## ⚙️ Architecture


```text
API → Python (Extract) → PostgreSQL (Neon) → SQL Modelling → Power BI Dashboard



## 📁 Project Structure

uk-carbon-intensity-pipeline/
├── src/
│   ├── extract/        # API data extraction
│   ├── transform/      # SQL execution scripts
│   ├── load/           # Load data into database
│   └── run_pipeline.py # Pipeline orchestration
│
├── sql/
│   ├── staging/        # Raw staging tables
│   └── marts/          # Star schema (fact & dimensions)
│
├── powerbi/
│   ├── screenshots/    # Dashboard preview
│   └── dashboard.pbix  # Power BI file
│
├── run_pipeline.sh     # Pipeline execution script
├── README.md
├── requirements.txt
└── .gitignore



---

## 🧠 Data Model

The project uses a star schema optimised for time-series analysis:

- **fact_carbon_intensity**
  - actual_intensity  
  - forecast_intensity  
  - forecast_error  

- **dim_datetime**
- **dim_region** (currently UK-wide)

This structure enables efficient aggregation and KPI computation.

---

## 📊 Key Metrics

The dashboard includes:

- Carbon Intensity (Actual vs Forecast)
- Forecast Accuracy (%)
- Forecast Error
- Volatility (standard deviation)
- High Carbon Hours (%)
- Hourly carbon intensity patterns

---

## 🔍 Key Insights

- Carbon intensity consistently peaks during evening hours, indicating higher reliance on carbon-intensive energy sources
- Forecast accuracy remains high (~93%), making the model suitable for planning decisions
- Approximately 20% of observed periods fall into high-carbon conditions
- Moderate volatility suggests variability that can impact forecast reliability

---

## 🎯 Business Questions Answered

This project helps answer:

- When are the lowest-carbon periods for energy usage?
- How reliable are carbon intensity forecasts?
- How often does the system operate in high-carbon conditions?
- How volatile is carbon intensity over time?

These insights support:
- Carbon-aware scheduling (e.g. EV charging, compute workloads)
- Demand shifting strategies
- Environmental compliance monitoring

---

## 🧩 Analytical Approach

The analysis is structured around three key dimensions:

- **Level** → Current carbon intensity
- **Stability** → Volatility and fluctuations
- **Reliability** → Forecast accuracy and error

This ensures the dashboard supports both monitoring and decision-making.

---

## 🚀 Future Improvements

- Integrate generation mix data (wind, solar, gas) to explain drivers of carbon intensity
- Add regional-level analysis across the UK
- Improve data completeness through automated backfilling
- Introduce carbon cost modelling for financial impact analysis
- Implement alerting for high-carbon or high-volatility periods

---

## 🛠️ Technologies Used

- Python (data extraction and pipeline orchestration)
- PostgreSQL (Neon cloud database)
- SQL (data modelling and transformations)
- Power BI (visualisation and dashboarding)
- Linux & Cron (automation)

---

## ▶️ How to Run

```bash
# Activate environment
source venv/bin/activate

# Run pipeline
bash run_pipeline.sh
