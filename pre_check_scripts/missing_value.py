import pandas as pd

df = pd.read_csv("datasets\canbrs_dataset_polish.csv")

overall_missing = df.isnull().mean() * 100
overall_missing = overall_missing.round(2)

if 'Outcome' not in df.columns:
    raise ValueError("The dataset does not contain a column named 'outcome'.")

grouped_missing = df.groupby('Outcome').apply(lambda x: x.isnull().mean() * 100)
grouped_missing = grouped_missing.round(2)

print("\n--- Overall Missing % per Variable ---\n")
print(overall_missing.to_frame(name='% Missing'))

print("\n--- Missing % per Variable by Outcome ---\n")
print(grouped_missing.transpose())

# Insight 

# This script calculates the percentage of missing values for each variable in the dataset and groups them by the 'Outcome' variable.

# It clearly shows that only site_liver has just some entry missing. This adds up to the range check script where it was noted that this entry is not considered an error but is noted for completeness. All other variables have no missing values.