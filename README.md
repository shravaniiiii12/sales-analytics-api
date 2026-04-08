# 📊 Sales Analytics API

This project is an end-to-end data analytics system built using FastAPI and Pandas. It processes sales data and exposes business insights through REST APIs.

---

## 🚀 Features

- Data cleaning and preprocessing
- Revenue and profit analysis
- Dynamic filtering using query parameters
- REST API using FastAPI

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Pandas
- Uvicorn

data-api-project/
│
├── main.py
├── cleaned_sales.csv


---

## ▶️ How to Run

```bash
pip install fastapi uvicorn pandas
python main.py
```


🌐 API Endpoints
1. Top Categories
/top-category
2. Region-wise Profit
/region-profit?region=West
3. Monthly Revenue Trend
/monthly-trend?month=Jan


📈 Example Use Case

This API allows users to:

Analyze top-performing product categories
Compare profit across regions
Track monthly revenue trends dynamically


👩‍💻 Author
Shravani Karambelkar



