import pandas as pd

def run_cleaning():
    df = pd.read_csv('data/retail_sales.csv')
    df.drop_duplicates(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.dropna()
    df.to_csv('data/retail_sales_cleaned.csv', index=False)
