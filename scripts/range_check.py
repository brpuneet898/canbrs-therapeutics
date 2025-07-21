import pandas as pd

df = pd.read_csv("datasets\canbrs_dataset_polish.csv")

expected_ranges = {
    "age": (22, 85),
    "year_of_diagnosis": (2010, 2021),
    "race": {"w1", "b2", "as3", "ain4", "r0"},
    "marital_status": {"m1", "s3", "w5", "d4", "udp6", "s2", "m0"},
    "primary_site": (500, 509),
    "regional_nodes_positive": (0, 99),
    "regional_nodes_examined": (0, 99),
    "site_bone": {"No", "Yes", "Unknown"},
    "site_brain": {"No", "Yes", "Unknown"},
    "site_liver": {"No", "Yes", "Unknown"},
    "site_lung": {"No", "Yes", "Unknown"},
    "subtype": {1, 2, 3, 4},
    "er_status": {"Positive", "Negative", "Unknown", "Borderline/Unknown"},
    "pr_status": {"Positive", "Negative", "Unknown", "Borderline/Unknown"},
    "her2_status": {"Positive", "Negative", "Unknown"},
}

def check_numeric_range(series, min_val, max_val):
    invalid = series[(series < min_val) | (series > max_val)]
    return invalid

def check_categorical_values(series, allowed_values):
    invalid = series[~series.isin(allowed_values)]
    return invalid

for column, rule in expected_ranges.items():
    print(f"\nChecking column: {column}")
    if isinstance(rule, tuple):  
        invalid_values = check_numeric_range(df[column], *rule)
    else: 
        invalid_values = check_categorical_values(df[column], rule)
    
    if invalid_values.empty:
        print("  ✔ All values within expected range/domain.")
    else:
        print(f"  ✘ {len(invalid_values)} invalid values found:")
        print(invalid_values.value_counts())


# Insight

# This notebook checks the ranges of values in the dataset against expected ranges defined in `expected_ranges`. It identifies any values that fall outside these ranges and reports them.

# It is found that there is one entry missing in the `site_liver` column, which is not included in the expected ranges. This entry is not considered an error but is noted for completeness.