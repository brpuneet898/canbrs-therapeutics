import pandas as pd
import numpy as np
import sys

def is_structurally_missing(col_data):
    """Heuristic to detect structural missingness"""
    if col_data.isna().all():
        return True
    return False  

def analyze_missingness(df):
    print("Analyzing missingness in dataset...\n")
    total_rows = df.shape[0]
    missing_report = []

    for col in df.columns:
        num_missing = df[col].isna().sum()
        if num_missing == 0:
            continue  

        perc_missing = num_missing / total_rows * 100
        structural_flag = is_structurally_missing(df[col])

        for other_col in df.columns:
            if col == other_col or df[other_col].nunique() > 50:
                continue  

            try:
                group_missing = df.groupby(other_col)[col].apply(lambda x: x.isna().mean())
                if (group_missing == 1.0).any() and (group_missing != 1.0).any():
                    structural_flag = True
                    break
            except Exception:
                continue

        missing_report.append({
            'Column': col,
            'Missing Count': num_missing,
            'Missing %': round(perc_missing, 2),
            'Missingness Type': 'Structural' if structural_flag else 'Random'
        })

    print(f"{'Column':<25} {'Missing Count':<15} {'Missing %':<12} {'Missingness Type'}")
    print("-" * 70)
    for item in missing_report:
        print(f"{item['Column']:<25} {item['Missing Count']:<15} {item['Missing %']:<12} {item['Missingness Type']}")

if __name__ == "__main__":
    try:
        df = pd.read_csv("datasets\canbrs_dataset_polish.csv")
    except FileNotFoundError:
        print("File 'canbrs_dataset_polish.csv' not found. Make sure it's in the same directory.")
        sys.exit(1)

    analyze_missingness(df)

# Insight

# This script analyzes missingness in the dataset, identifying columns with missing values and categorizing them as either structural or random missingness. It provides a detailed report on the extent of missing data for each column.

# It is found that the `site_liver` column has some entries missing, which is consistent with the previous range check script. We here got to know that it is randomly missing. 