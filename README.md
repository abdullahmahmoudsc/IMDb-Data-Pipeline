# IMDb-Data-Pipeline

A data pipeline project for scraping, cleaning, and visualizing IMDb Top 250 movies.

## Project Overview

This project collects data from IMDb Top 250 movies using Selenium, cleans and transforms the data using Pandas, and creates visualizations using Matplotlib.

The pipeline consists of three main stages:

1. Web Scraping
2. Data Cleaning
3. Data Visualization

## Data Collected

The project collects the following information for each movie:

- Movie Name
- Release Year
- Runtime
- IMDb Rating
- Number of Votes

## Technologies Used

- Python
- Selenium
- Pandas
- Matplotlib

## Data Pipeline

IMDb Top 250  
↓  
Web Scraping  
↓  
Raw CSV  
↓  
Data Cleaning  
↓  
Cleaned CSV  
↓  
Data Visualization

## Visualizations

The project includes the following visualizations:

- IMDb Rating Distribution
- IMDb Rating vs Number of Votes
- Movies by Release Year
- Movie Runtime Distribution
- Top 10 Highest Rated Movies

## Project Structure

```text
IMDb-Data-Pipeline/
│
├── data/
│   ├── imdb_raw.csv
│   └── imdb_cleaned.csv
│
├── scraping.py
├── cleaning.py
├── visualization.py
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the scripts in the following order:

```text
scraping.py
cleaning.py
visualization.py
```

## Data Validation

The cleaned dataset was validated to ensure data quality.

- No missing values
- No duplicate records
- Valid movie ratings
- Valid runtime values
- Valid vote counts
