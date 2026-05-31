# Zomato Data Analysis Using Python

## Project Overview

This project performs Exploratory Data Analysis (EDA) on a Zomato restaurant dataset using Python. The objective is to identify customer preferences, restaurant trends, pricing patterns, and the impact of online ordering on restaurant ratings.

The analysis was conducted using Pandas, NumPy, Matplotlib, and Seaborn, with multiple visualizations created to uncover meaningful insights from the dataset.

---

## Objectives

* Analyze different restaurant categories.
* Identify the most popular restaurants based on customer votes.
* Study online ordering trends.
* Examine restaurant rating distributions.
* Determine preferred dining cost ranges.
* Compare ratings between restaurants that accept online orders and those that do not.
* Visualize relationships using charts and heatmaps.

---

## Dataset

The dataset contains information about restaurants including:

* Restaurant Name
* Online Order Availability
* Table Booking Availability
* Rating
* Number of Votes
* Approximate Cost for Two People
* Restaurant Category

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Data Cleaning

The following preprocessing steps were performed:

* Converted restaurant ratings from string format (e.g., 4.1/5) to numerical values.
* Checked dataset structure and data types.
* Verified the dataset for missing values.
* Prepared data for visualization and analysis.

---

## Visualizations

The project includes the following visualizations:

1. Restaurant Type Distribution
2. Votes by Restaurant Type
3. Online Order Availability Analysis
4. Ratings Distribution Histogram
5. Cost Preference Analysis
6. Online vs Offline Rating Comparison (Box Plot)
7. Restaurant Type vs Online Orders (Heatmap)

---

## Key Findings

### Restaurant Categories

Dining restaurants are the most common category in the dataset.

### Customer Preference

Dining restaurants receive the highest number of customer votes.

### Most Popular Restaurant

Empire Restaurant received the maximum number of votes.

### Online Ordering

Most restaurants do not offer online ordering services.

### Ratings

Most restaurant ratings fall between 3.5 and 4.0, indicating generally positive customer experiences.

### Dining Budget

Most couples prefer restaurants with an approximate cost of ₹300 for two people.

### Online Orders and Ratings

Restaurants offering online ordering tend to have higher ratings compared to those that do not.

---

## How to Run

1. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

2. Run the project:

```bash
python project.py
```

3. Generated visualizations will be displayed and saved in the charts folder.

---

## Future Improvements

* Interactive dashboard using Streamlit.
* Additional restaurant ranking analysis.
* Correlation analysis between ratings and votes.
* Advanced data visualizations.
* Deployment as a web application.

---

## Author

Gahana

B.Tech Computer Science Engineering Student

Python | Data Analytics | Data Visualization
