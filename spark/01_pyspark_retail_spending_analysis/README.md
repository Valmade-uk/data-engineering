# goit-de-hw-03

Homework 03 for the **GoIT Neoversity Data Engineering course**.

This repository contains a PySpark homework project focused on loading, cleaning, joining, aggregating, and analyzing data with **Apache Spark**.

## Homework Objectives

The assignment consists of six stages:

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

The homework uses three CSV files provided by the course:

- `users.csv` — user information
- `purchases.csv` — purchase transactions
- `products.csv` — product information

The source datasets are **not included in this repository** because they are provided separately as course materials.

The notebook uses local file paths to access these datasets. If the project is run on another machine, the paths may need to be adjusted to match the local directory structure.

## Project Structure

```text
goit-de-hw-03/
├── screenshots/
│   ├── p1_...
│   ├── p2_...
│   ├── p3_...
│   ├── p4_...
│   ├── p5_...
│   └── p6_...
├── goit_de_hw_03.ipynb
├── README.md
└── .gitignore
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
6. Open `goit_de_hw_03.ipynb`.
7. Run all cells from top to bottom.

Example dependency installation:

```bash
python -m pip install pyspark jupyter
```

> Note: the local Spark/Java configuration used in the notebook may need to be adjusted for a different operating system or installation path.

## Screenshots

The `screenshots/` directory contains the required `df.show()` outputs for the six homework stages.

Suggested naming convention:

```text
p1_users_dataframe.png
p1_purchases_dataframe.png
p1_products_dataframe.png

p2_cleaning_counts.png
p2_cleaned_users.png
p2_cleaned_purchases.png
p2_cleaned_products.png

p3_total_purchases_by_category.png
p4_purchases_by_category_age_18_25.png
p5_spending_share_age_18_25.png
p6_top_3_categories.png
```
