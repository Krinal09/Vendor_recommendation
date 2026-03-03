# Vendor Recommendation System (Rule-Based)

A **Streamlit**-based application that recommends the most relevant vendors based on project requirements using a simple **rule-based scoring system**.

## Overview

This system matches vendors by evaluating:

- **Work Type** similarity  
- **Category** match  
- **Rating** proximity  

It uses a **weighted scoring formula** (no machine learning), making it:  
✅ Simple  
✅ Transparent  
✅ Easy to explain and maintain for business users

## ⚙️ Tech Stack

- Python  
- Pandas  
- Streamlit  

## Project Structure

vendor_app/
├── vendors.csv       # Vendor database
├── app.py            # Main Streamlit application
└── README.md         # This file


## Dataset Columns (vendors.csv)

| Column     | Description                  | Example value          |
|------------|------------------------------|------------------------|
| Company    | Vendor/company name          | ABC Constructions      |
| Work_Type  | Type of work they specialize in | Civil, Interior, MEP   |
| Category   | Main business category       | Construction, Design   |
| Rating     | Vendor rating (out of 5)     | 4.2                    |

## How to Run the App

1. Install required packages:

```bash
pip install streamlit pandas
```

2. Run the application:

```bash
streamlit run app.py
```

3. Open your browser at:

```bash
http://localhost:8501
```

## Scoring Formula

Final Score =
  (Work Match Score × 0.5)
+ (Category Match Score × 0.3)
+ (Rating Similarity Score × 0.2)

Vendors are sorted in descending order of final score — highest score = most recommended.

## Purpose

Automate vendor shortlisting and eliminate time-consuming manual searching with a clear, explainable, rule-based logic suitable for business and procurement teams.

Built using Streamlit
