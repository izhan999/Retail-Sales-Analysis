import pandas as pd

def add_features():
    df = pd.read_csv('data/retail_sales_cleaned.csv')
    df['Revenue_per_Unit'] = df['Revenue'] / df['Units_Sold']
    df['Weekday'] = pd.to_datetime(df['Date']).dt.day_name()
    df.to_csv('data/retail_sales_features.csv', index=False)
