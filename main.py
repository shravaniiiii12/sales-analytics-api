from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("cleaned_sales.csv")

@app.get("/")
def home():
    return {"message": "Sales Analytics API is running"}

@app.get("/top-category")
def top_category():
    result = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False).head(5)
    return result.to_dict()

@app.get("/region-profit")
def region_profit(region: str = None):
    if region:
        result = df[df["Region"] == region]["Profit"].sum()
        return {"region": region, "profit": result}
    else:
        result = df.groupby("Region")["Profit"].sum()
        return result.to_dict()

@app.get("/monthly-trend")
def monthly_trend(month: str = None):
    if month:
        result = df[df["Month"] == month]["Revenue"].sum()
        return {"month": month, "revenue": result}
    else:
        result = df.groupby("Month")["Revenue"].sum()
        return result.to_dict()

import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)