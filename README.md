# Amazon Prime Video Content Analysis & Power BI Dashboard

An end-to-end data analytics project exploring Amazon Prime Video's content catalogue to identify content distribution patterns, release-year trends, ratings, genres, and movie-duration insights using Python and Power BI.

## Project Overview

This project focuses on analysing an Amazon Prime Video dataset to understand the composition and characteristics of its available content. Exploratory Data Analysis (EDA) was performed to examine movies and TV shows, release years, ratings, genres, and movie durations. The findings are presented through analytical visualisations and an interactive Power BI dashboard.

The project demonstrates a practical data analytics workflow, from understanding the dataset and examining data quality to analysing patterns and communicating insights through visualisations.

## Problem Statement

Streaming platforms manage large content catalogues containing movies and television shows across multiple genres, ratings, and release years. Analysing this information can help stakeholders understand catalogue composition and identify patterns in the available content.

The objective of this project is to:

- Analyse the distribution of Movies and TV Shows.
- Explore content release-year trends.
- Examine ratings and genre distributions.
- Investigate movie-duration patterns.
- Present key findings through clear visualisations and a Power BI dashboard.
- Communicate data-driven observations that may support content catalogue planning.

**Scope note:** The dataset describes catalogue attributes. It does not independently establish customer preferences, viewing behaviour, profitability, or business performance.

## Objectives

- Understand the structure and characteristics of the dataset.
- Inspect data quality, missing values, and duplicate records.
- Perform Exploratory Data Analysis using Python.
- Identify patterns across content types, release years, ratings, genres, and durations.
- Create visualisations to communicate analytical findings.
- Develop a Power BI dashboard for exploring the content catalogue.
- Summarise key observations and potential business implications.

## Dataset Information

| Attribute | Details |
|---|---|
| Dataset | Amazon Prime Video content catalogue |
| Records | 9,668 rows in the analysed dataset |
| Columns | 11 |
| Data type | Structured, tabular data |
| Primary analysis | Movies and TV Shows |
| Tools | Python, Pandas, Matplotlib, Power BI |

### Key Dataset Fields

The dataset includes fields such as:

- `show_id` — content identifier
- `type` — Movie or TV Show
- `title` — content title
- `director` — director information
- `cast` — cast information
- `country` — country information
- `release_year` — release year
- `rating` — content rating
- `duration` — movie duration or TV-show season information
- `listed_in` — genre or category information
- `description` — content description

The original dataset is available as `data.csv` in this repository.

## Tools & Technologies

- **Python** — data exploration and analysis
- **Pandas** — data inspection and manipulation
- **Matplotlib** — data visualisation
- **Power BI Desktop** — dashboard development
- **GitHub** — project versioning and sharing

## Data Cleaning & Preparation

The dataset was inspected before analysis to understand its structure and identify potential data-quality issues.

The preparation workflow included:

1. Loading the CSV dataset into the analysis environment.
2. Inspecting the number of records, columns, and data types.
3. Checking for missing values.
4. Checking for duplicate records.
5. Reviewing fields used in content-type, release-year, rating, genre, and duration analysis.
6. Examining duration values according to content type.
7. Preparing relevant data for exploratory analysis and visualisation.

**Data quality note:** The original EDA reported one missing value in the `director` field and no duplicate rows. These observations describe the inspected dataset; they do not imply that every missing value was removed or that every field was fully cleaned. Refer to the analysis script for the actual transformations performed.

## Exploratory Data Analysis

The analysis examined the following areas:

### 1. Content Type Distribution

Compared the number and proportion of Movies and TV Shows in the catalogue.

### 2. Release-Year Trends

Examined how catalogue titles were distributed across release years and identified years with high title counts.

### 3. Ratings Analysis

Explored the distribution of content-rating categories to understand the composition of the catalogue by rating.

### 4. Genre Analysis

Investigated the genre and category information recorded in the dataset to identify frequently occurring categories.

### 5. Movie Duration Analysis

Examined movie-duration patterns using descriptive statistics, including average and median duration.

### 6. TV Show Seasons

Reviewed season-related duration information for TV Shows where applicable.

## Key Findings

The following findings were recorded during the initial EDA:

- **9,668 records** and **11 columns** were present in the analysed dataset.
- **Movies:** 7,814 titles, approximately **80.82%** of the dataset.
- **TV Shows:** 1,854 titles, approximately **19.18%** of the dataset.
- **2021** was the most represented release year in the initial analysis, with **1,442 titles**.
- The average movie duration was approximately **91.31 minutes**, with a median of **91 minutes**.
- The initial data-quality check identified one missing value in the director field and no duplicate rows.

These results describe the inspected dataset and should be interpreted in the context of its fields, coverage, and data quality.

## Power BI Dashboard

The Power BI dashboard presents the analysed content catalogue through visual summaries and charts.

The dashboard is intended to help viewers explore:

- Movie and TV Show distribution
- Release-year patterns
- Content ratings
- Genre distribution
- Movie-duration information

### Dashboard Preview

![Amazon Prime Video Analytics Dashboard](dashboard.png)

**Interactive dashboard:** The Power BI `.pbix` file is included in this repository where available. Download the file and open it in Power BI Desktop to explore the report.

> Note: The screenshot is a static preview. Interactivity is available in the Power BI report rather than in the screenshot.

## Key Business Insights & Implications

### 1. Catalogue Composition

Movies accounted for approximately 80.82% of the analysed titles, while TV Shows represented approximately 19.18%.

**Potential implication:** Content planners can use this distribution as a starting point when reviewing the balance of different content formats. The distribution alone does not establish whether the mix is optimal.

### 2. Release-Year Patterns

The initial analysis identified 2021 as the most represented release year.

**Potential implication:** Examining release-year patterns can help teams understand how catalogue entries are distributed over time and support further investigation of content acquisition and catalogue coverage.

### 3. Ratings Distribution

The rating analysis provides a view of the categories represented in the catalogue.

**Potential implication:** Rating distributions may help support catalogue classification and content-availability reviews. They should not be treated as direct evidence of audience age or viewing preferences.

### 4. Genre Distribution

Genre analysis highlights categories that occur frequently in the dataset.

**Potential implication:** Genre-level summaries can support further catalogue reviews and help identify areas for deeper analysis. Frequent entries do not necessarily indicate higher audience demand.

### 5. Movie Duration

The average movie duration was approximately 91.31 minutes, and the median was 91 minutes in the initial analysis.

**Potential implication:** Duration statistics provide a useful overview of the catalogue's movie-length characteristics and can support comparisons across relevant content groups.

## Limitations

- The dataset focuses on catalogue metadata rather than user-level viewing behaviour.
- No conclusions about revenue, customer engagement, retention, or profitability can be established from these fields alone.
- Missing or inconsistent metadata may affect certain analyses.
- The findings depend on the dataset's coverage and the accuracy of its recorded fields.
- Genre and rating interpretations should follow the dataset's original definitions.

## Conclusion

This project demonstrates an end-to-end exploratory data analysis workflow using Python and a Power BI dashboard. It examines the composition of an Amazon Prime Video content catalogue, including content types, release years, ratings, genres, and movie durations.

The project highlights how structured data, analytical techniques, and visualisation can turn a raw dataset into understandable findings. It also provides a foundation for further analysis using richer information, such as viewing activity, customer engagement, and content performance metrics.

## Future Enhancements

- Add more detailed comparisons across countries and content categories.
- Improve data validation and document field-level cleaning decisions.
- Publish an interactive version of the dashboard where feasible.
- Incorporate viewing and engagement data if a reliable dataset becomes available.
- Extend the analysis with additional metrics and clearly defined business questions.

## Repository Contents

- `README.md` — project documentation
- `data.csv` — source dataset
- `amazon_prime_eda.py` — Python EDA script
- `dashboard.png` — dashboard screenshot
- Power BI `.pbix` file — dashboard report, if uploaded
- Additional `.png` files — analytical visualisations

## Skills Demonstrated

Python · Pandas · Exploratory Data Analysis · Data Cleaning · Data Visualisation · Power BI · Business Insights · Data Storytelling · GitHub

---

**Project Type:** Data Analytics | Exploratory Data Analysis | Business Intelligence

**Author:** Pradnya Manohar Navale
