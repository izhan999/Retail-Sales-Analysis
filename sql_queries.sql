-- Total revenue per store
SELECT Store, SUM(Revenue) AS Total_Revenue FROM retail_sales GROUP BY Store;

-- Top 3 products by revenue
SELECT Product, SUM(Revenue) AS Revenue FROM retail_sales GROUP BY Product ORDER BY Revenue DESC LIMIT 3;
