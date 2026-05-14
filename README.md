#Germany Data Job Market Analysis

This project was built to analyze Germany-based data job postings using API extraction, Python-based data processing, and Tableau dashboard visualization. The main idea behind the project was to understand hiring trends, popular roles, and location-wise demand across different data-related jobs in Germany.

#Workflow

API Extraction -> Data Cleaning -> Feature Engineering -> CSV Output -> Tableau Dashboard

#Tools Used

- Python
- Python Pandas
- Tableau
- REST API

#Data Source

The data was collected using the German Federal Employment Agency Job Search API.

API Endpoint:
https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs

#Project Structure

data_extraction.py: extracts raw job data from the API and stores it as a CSV file
transformation.py: performs preprocessing and transformation on the extracted dataset
data_jobs.csv: raw extracted dataset
jobs_transformed.csv: cleaned dataset used for Tableau visualization
germany_jobs_dashboard.png: dashboard screenshot generated using Tableau

#Extraction

The extraction script fetches job postings for roles such as:

- Data Scientist
- Data Analyst
- Data Engineer
- ML Engineer
- Business Analyst

The script also handles pagination, duplicate removal, failed requests, and JSON validation before storing the extracted records as a raw CSV dataset.

#Transformation

The transformation script performs basic preprocessing and cleaning tasks including:

- handling missing values
- splitting city and region fields
- cleaning text columns
- formatting values
- creating derived columns

The cleaned dataset is then exported as a processed CSV file which is later connected to Tableau.

#Dashboard

The Tableau dashboard was built to analyze:

- role distribution
- company-wise hiring
- location-based demand
- hiring trends across Germany

#Project Outcome

Through this project, I was able to work on an end-to-end analytics workflow involving API-based extraction, preprocessing, feature engineering, and dashboard reporting. It also helped me better understand how semi-structured datasets can be cleaned and transformed before being used for analytical reporting and visualization.
