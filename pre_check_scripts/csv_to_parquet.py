import pandas as pd

df = pd.read_csv('C:\My Folder\projects\canbrs-therapeutics\datasets\canbrs_dataset_polish.csv')

df = df.drop(columns=['ID'])

df_cleaned = df.copy()
unknown_values = ['Unknown', 'unknown', 'UNK']
df_cleaned.replace(unknown_values, pd.NA, inplace=True)
df_cleaned = df_cleaned.dropna(subset=[
    'age', 'year_of_diagnosis', 'race', 'marital_status', 'primary_site',
    'site_bone', 'site_brain', 'site_liver', 'site_lung',
    'er_status', 'pr_status', 'her2_status', 'Outcome'
])

categorical_cols = [
    'race', 'marital_status', 'primary_site',
    'site_bone', 'site_brain', 'site_liver', 'site_lung',
    'subtype', 'er_status', 'pr_status', 'her2_status', 'Outcome'
]
for col in categorical_cols:
    df_cleaned[col] = df_cleaned[col].astype('category')

numeric_cols = ['age', 'year_of_diagnosis', 'regional_nodes_positive', 'regional_nodes_examined']
for col in numeric_cols:
    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')

df_cleaned = df_cleaned.dropna()

df_cleaned.to_parquet("C:\My Folder\projects\canbrs-therapeutics\datasets/analytic_vFINAL.parquet", index=False)

print("Final analytic dataset saved as 'analytic_vFINAL.parquet'")
