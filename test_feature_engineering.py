import pandas as pd

def test_revenue_per_unit():
    df = pd.read_csv('data/retail_sales_features.csv')
    assert all(df['Revenue_per_Unit'] > 0)
