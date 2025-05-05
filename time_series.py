import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/retail_sales_features.csv')
df['Date'] = pd.to_datetime(df['Date'])
ts = df.groupby('Date')['Revenue'].sum()

ts.plot(title='Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('visualizations/daily_revenue_trend.png')
plt.show()
