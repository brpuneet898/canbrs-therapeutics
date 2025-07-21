import pandas as pd

df = pd.read_csv("datasets\canbrs_dataset_polish.csv")

print("Duplicate Check Report for canbrs_dataset_polish.csv\n")

if 'ID' not in df.columns:
    print("Column 'ID' not found in the dataset.")
else:
    duplicate_ids = df[df.duplicated('ID', keep=False)]
    if not duplicate_ids.empty:
        print(f"Found {duplicate_ids['ID'].nunique()} duplicate patient IDs.")
        print("Here are the duplicate patient IDs:")
        print(duplicate_ids['ID'].value_counts())
    else:
        print("No duplicate patient IDs found.")

duplicate_rows = df[df.duplicated(keep=False)]

if not duplicate_rows.empty:
    print(f"\nFound {duplicate_rows.shape[0]} fully duplicate rows in the dataset.")
else:
    print("\nNo fully duplicate rows found.")

# Insight

# This script checks for duplicate patient IDs and fully duplicate rows in the dataset `canbrs_dataset_polish.csv`. 

# It is clear that there are no duplicate patient IDs, also, there are none of the rows are fully duplicated.