# Air Quality ETL Pipeline

## Project Overview

This project implements an Extract, Transform and Load (ETL) pipeline to prepare air-quality data for analysis and visualization.

The pipeline uses Python to process and clean the data, SQLite to store the processed records, and Power BI to visualize the resulting dataset.

The objective is to demonstrate how raw data can be transformed into a structured, analysis-ready format through a repeatable workflow.

## Project Objectives

- Extract air-quality data from the project's input source.
- Clean and prepare the data using Python.
- Store processed data in a SQLite database.
- Make the processed dataset available for downstream analysis.
- Visualize air-quality metrics using Power BI.

## Tools & Technologies

- **Python:** ETL scripting and data processing.
- **Pandas:** Data manipulation and cleaning, where used in the pipeline.
- **SQLite:** Structured storage of processed data.
- **CSV:** Data exchange and storage of cleaned records.
- **Power BI:** Data visualization and dashboard development.

## ETL Workflow

### 1. Extract

Read air-quality data from the source configured in the pipeline and prepare it for processing.

### 2. Transform

Apply the cleaning and preparation steps implemented in the Python script. These steps should be documented according to the actual code, including any handling of missing values, data types or duplicate records.

### 3. Load

Store the processed records in a SQLite database so they can be queried and reused for analysis.

### 4. Visualize

Use the processed data to create a Power BI dashboard for exploring air-quality measurements and patterns.

## Key Outputs

- `etl_pipeline.py` — Python ETL pipeline.
- `air_quality_clean.csv` — Cleaned data output.
- `air_quality.db` — SQLite database.
- `air_quality_etl.pbix` — Power BI dashboard.

## Key Findings

The primary deliverable is a workflow that converts air-quality input data into cleaned, stored and analysis-ready output.

Specific environmental findings—such as changes over time, differences between locations or variation in pollutant measurements—should be documented only after checking the actual dataset and dashboard results.

## Skills Demonstrated

Python scripting, data cleaning, ETL concepts, SQLite database handling, structured data storage, data pipeline development and Power BI visualization.

## Conclusion

This project demonstrates practical ETL fundamentals by connecting data extraction, transformation, database storage and visualization in a single workflow. It complements business analytics projects by showcasing the data preparation process that supports reliable reporting.
