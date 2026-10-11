# PySpark Retail Spending Analysis

A PySpark data analysis project completed as **Homework 03** of the GoIT Neoversity Data Engineering course.

The project demonstrates data loading, cleaning, joins, aggregations, filtering, and spending analysis using **Apache Spark and PySpark**.

## Objectives

The project consists of six stages:

1. Load three CSV datasets into separate Spark DataFrames.
2. Remove rows containing missing values.
3. Calculate the total purchase amount for each product category.
4. Calculate purchase amounts by category for users aged 18–25 inclusive.
5. Calculate each category's share of total spending for users aged 18–25.
6. Select the top 3 product categories by spending share.

## Technologies

- Python
- Apache Spark
- PySpark
- Jupyter Notebook

## Input Data

The project uses three CSV files provided as course materials:

- `users.csv` — user information
- `purchases.csv` — purchase transactions
- `products.csv` — product information

The source datasets are not included in this repository.

The notebook uses local file paths to access the datasets. These paths may need to be adjusted when running the project on another machine.

## Project Structure

```text
01_pyspark_retail_spending_analysis/
├── README.md
├── pyspark_retail_spending_analysis.ipynb
└── screenshots/
    ├── 01_load_input_dataframes.png
    ├── 02_remove_missing_values.png
    ├── 03_total_purchase_amount_by_category.png
    ├── 04_purchase_amount_age_18_25.png
    ├── 05_spending_share_age_18_25.png
    └── 06_top_3_categories_by_spending_share.png
```

## Data Processing Pipeline

```text
users
  │
  │ user_id
  ▼
purchases
  │
  │ product_id
  ▼
products
  │
  ▼
quantity × price
  │
  ▼
purchase_amount
  │
  ├── total spending by category
  │
  └── spending by category for users aged 18–25
          │
          ▼
     spending share (%)
          │
          ▼
       Top 3 categories
```

## Results

After removing rows with missing values:

| Dataset | Rows before | Rows after |
|---|---:|---:|
| Users | 100 | 95 |
| Purchases | 200 | 195 |
| Products | 50 | 47 |

### Total Purchase Amount by Category

| Category | Total purchase amount |
|---|---:|
| Sports | 1802.50 |
| Home | 1523.50 |
| Electronics | 1174.80 |
| Clothing | 790.30 |
| Beauty | 459.90 |

### Spending by Users Aged 18–25

| Category | Spending 18–25 | Share of 18–25 spending |
|---|---:|---:|
| Home | 361.10 | 29.90% |
| Sports | 310.50 | 25.71% |
| Electronics | 249.60 | 20.67% |
| Clothing | 245.00 | 20.29% |
| Beauty | 41.40 | 3.43% |

### Top 3 Categories by Spending Share

1. Home — 29.90%
2. Sports — 25.71%
3. Electronics — 20.67%

## Running the Notebook

1. Install Java and Apache Spark.
2. Create and activate a Python virtual environment.
3. Install PySpark and Jupyter support.
4. Make the course CSV files available locally.
5. Adjust the dataset paths in the notebook if necessary.
6. Open `pyspark_retail_spending_analysis.ipynb`.
7. Run all cells from top to bottom.

Example dependency installation:

```bash
python -m pip install pyspark jupyter
```

> Note: the local Spark and Java configuration used in the notebook may need to be adjusted for a different operating system or installation path.

## Screenshots

The `screenshots/` directory contains the output for each stage of the assignment:

1. `01_load_input_dataframes.png`
2. `02_remove_missing_values.png`
3. `03_total_purchase_amount_by_category.png`
4. `04_purchase_amount_age_18_25.png`
5. `05_spending_share_age_18_25.png`
6. `06_top_3_categories_by_spending_share.png`