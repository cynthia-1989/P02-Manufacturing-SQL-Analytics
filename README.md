# P02 ⭐⭐ — Manufacturing SQL 🏭

## Overview

This project builds a manufacturing SQL extraction pipeline for analysing production operations, quality control performance, equipment activity, plant efficiency, and manufacturing defect behaviour.

The pipeline connects to a PostgreSQL manufacturing database, performs SQL extraction queries, joins multiple manufacturing tables, and generates a flat raw dataset for downstream ETL and analytics workflows.

---

## Table of Contents

1. [Project Brief](#project-brief)
2. [SQL Workflow](#sql-workflow)
3. [Input and Output](#input-and-output)
4. [Project Structure](#project-structure)
5. [Production Run Analysis](#production-run-analysis)
6. [Quality Check Analysis](#quality-check-analysis)
7. [Equipment Analysis](#equipment-analysis)
8. [Aggregation Queries](#aggregation-queries)
9. [Join Operations](#join-operations)
10. [CTE and Window Functions](#cte-and-window-functions)
11. [Visualisations](#visualisations)
12. [How to Run](#how-to-run)
13. [Tests](#tests)
14. [Git Workflow](#git-workflow)

---

## Project Brief

**Company:** Precision Craft Industries  
**Role:** Data Analyst

The manufacturing dataset includes records such as:

- Production run records
- Quality check results
- Equipment maintenance logs
- Plant operations
- Product information

The analysis focuses on extracting manufacturing operational data from PostgreSQL and preparing a flat analytical dataset for downstream ETL processing and defect prediction modelling.

---

## SQL Workflow

### 1. Database Connection

Connect to the PostgreSQL manufacturing database using:

- Supabase
- SQLAlchemy
- PostgreSQL driver

Database schema used:

```text
manufacturing
```

---

### 2. SQL Extraction

Run SQL extraction queries against the manufacturing schema.

Key manufacturing tables include:

```text
production_runs
quality_checks
equipment
plants
products
```

---

### 3. SQL Basics

The project includes basic SQL operations such as:

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT

---

### 4. Aggregation Queries

The project performs manufacturing aggregations including:

- Defect rate calculations
- Production efficiency analysis
- Plant production summaries
- Shift performance analysis
- Equipment utilisation statistics

SQL functions used include:

```sql
COUNT()
SUM()
AVG()
MIN()
MAX()
GROUP BY
```

---

### 5. Join Operations

The project joins manufacturing tables to create a flat analytical dataset.

Joins include:

- Production runs + quality checks
- Production runs + equipment
- Plants + production activity
- Products + quality results

The final dataset combines manufacturing operational records into one extract.

---

### 6. CTE and Window Functions

The project includes advanced SQL using:

- Common Table Expressions (CTEs)
- Window functions

Examples include:

```sql
ROW_NUMBER()
RANK()
DENSE_RANK()
OVER(PARTITION BY ...)
```

CTEs and window functions are used to rank production runs by efficiency within each manufacturing plant.

---

## Input and Output

### Input

```text
PostgreSQL manufacturing database
```

### Outputs

```text
data/raw-data.csv
sql/
reports/
```

---

## Project Structure

```text
P02-manufacturing-sql/
│
├── data/
│   └── raw-data.csv
│
├── reports/
│
├── sql/
│   ├── 01_sql_basics.sql
│   ├── 02_aggregations.sql
│   ├── 03_joins.sql
│   ├── 04_cte_window.sql
│   └── 05_extract_raw_data.sql
│
├── src/
│   ├── query_runner.py
│   └── data_extractor.py
│
├── tests/
│
├── run.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Production Run Analysis

The project analyses manufacturing production operations including:

- Production volume
- Production efficiency
- Shift productivity
- Plant performance
- Run duration analysis

Metrics generated include:

- Total production output
- Average run efficiency
- Production counts by plant
- Shift-based productivity statistics

---

## Quality Check Analysis

The project analyses manufacturing quality control records.

Analysis includes:

- Defect rates
- Quality inspection outcomes
- Product quality comparisons
- Plant quality performance
- Shift quality analysis

Metrics generated include:

- Total defect counts
- Average defect rates
- Pass/fail inspection statistics
- Quality performance by plant

---

## Equipment Analysis

The project analyses equipment operations and maintenance activity.

Analysis includes:

- Equipment utilisation
- Maintenance frequency
- Equipment downtime
- Production equipment efficiency

Metrics generated include:

- Equipment activity counts
- Downtime statistics
- Maintenance summaries
- Equipment efficiency rankings

---

## Aggregation Queries

The project performs manufacturing aggregation analysis using:

```sql
COUNT()
SUM()
AVG()
MIN()
MAX()
GROUP BY
```

Aggregations help summarise manufacturing operational performance.

---

## Join Operations

The project joins multiple manufacturing tables into one analytical dataset.

Joined tables include:

```text
production_runs
quality_checks
equipment
plants
products
```

The joined dataset is exported as:

```text
data/raw-data.csv
```

---

## CTE and Window Functions

Advanced SQL functionality includes:

- CTE-based queries
- Ranking functions
- Partitioned analysis
- Efficiency rankings

Examples include:

- Ranking production runs by efficiency
- Ranking plants by defect rate
- Ranking equipment by downtime

---

## Visualisations

The project notebook can generate manufacturing visualisations including:

- Defect rate charts
- Plant efficiency comparisons
- Production trend charts
- Equipment utilisation charts

Saved charts are stored in:

```text
reports/
```

---

## How to Run

Run the complete manufacturing SQL extraction pipeline:

```bash
python run.py
```

The pipeline performs:

1. Database connection
2. SQL query execution
3. Join extraction
4. Raw dataset creation
5. CSV export

---

## Tests

Run unit tests using:

```bash
pytest tests/
```

Tests cover:

- Database connectivity
- SQL query execution
- Aggregation queries
- Join operations
- Data extraction
- CSV generation

---

## Git Workflow

```bash
git status
git add .
git commit -m "feat: complete manufacturing SQL extraction project"
git push
```

---

## Success Criteria Achieved

- All five tables queried successfully
- Aggregation queries completed
- Join operations completed
- CTE and window functions implemented
- raw-data.csv generated
- Production and quality tables joined successfully
- Project pushed to GitHub

---