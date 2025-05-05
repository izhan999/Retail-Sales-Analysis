import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('data/retail_sales_features.csv')
store_revenue = df.groupby('Store')[['Revenue']].sum()
kmeans = KMeans(n_clusters=2, random_state=0).fit(store_revenue)
store_revenue['Segment'] = kmeans.labels_
store_revenue.to_csv('data/store_segments.csv')
