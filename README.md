# 🛍️ ShopInsight

### E-Commerce Sales & Customer Intelligence Dashboard

ShopInsight is an interactive data analytics dashboard built to explore
e-commerce sales performance, customer purchasing behaviour, product
performance, and market trends.

The project uses the **Online Retail II** dataset and transforms raw
transaction data into meaningful business insights through an easy-to-use
Streamlit dashboard.

---

## 📊 Project Overview

E-commerce datasets can contain thousands of transaction records, making it
difficult to identify useful patterns directly from raw data.

ShopInsight solves this by providing an interactive dashboard where users can:

- Monitor total revenue
- Track the number of orders
- Analyse units sold
- Identify unique customers
- Study monthly revenue trends
- Find top-performing products
- Compare revenue across countries
- Analyse customer spending behaviour
- Identify repeat customers
- Download filtered datasets
- Inspect data quality and preprocessing results

---

## ✨ Features

### 📈 Sales Performance

- Total revenue
- Total orders
- Units sold
- Unique customers
- Monthly revenue trends
- Monthly order volume

### 🏆 Product Intelligence

- Top 10 products by revenue
- Product-level revenue analysis
- Product sales volume

### 🌍 Market Analysis

- Revenue by country
- Order volume by country
- Identification of leading markets

### 👥 Customer Intelligence

- Customer spending distribution
- Repeat customer analysis
- Repeat customer rate
- Average revenue per order
- Top customers by revenue

### 🔎 Interactive Filters

Users can filter the dashboard by:

- Country
- Invoice date range

All charts and KPIs update according to the selected filters.

### 📥 Data Export

Users can download:

- Filtered sales data as CSV
- Monthly sales summary as CSV

### 🧹 Data Quality Analysis

The dashboard also provides information about:

- Original records
- Valid sales records
- Cancellation transactions
- Duplicate records
- Missing customer IDs

---

## 🗂️ Dataset

This project uses the **Online Retail II** dataset from Kaggle.

The dataset contains transactional information from an online retail business,
including:

- Invoice number
- Product code
- Product description
- Quantity
- Invoice date
- Unit price
- Customer ID
- Country

The dataset is stored locally in:

```text
data/online_retail_II.xlsx
```
