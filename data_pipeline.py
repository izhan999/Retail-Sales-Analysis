from scripts import data_cleaning, feature_engineering

data_cleaning.run_cleaning()
feature_engineering.add_features()
print("Data pipeline executed successfully.")
