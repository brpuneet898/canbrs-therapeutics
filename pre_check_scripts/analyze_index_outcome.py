import pandas as pd

df = pd.read_csv("datasets\canbrs_dataset_polish.csv")

print("\n--- Dataset Overview ---")
print(f"Total records: {len(df)}")
print("Columns:", list(df.columns))

print("\n--- Index Date Candidate ---")
if 'year_of_diagnosis' in df.columns:
    print("Found 'year_of_diagnosis' column.")
    print("Year range:", df['year_of_diagnosis'].min(), "-", df['year_of_diagnosis'].max())
else:
    print("No diagnosis date column found.")

print("\n--- Outcome Column Analysis ---")
if 'Outcome' in df.columns:
    print("Unique Outcome values:", df['Outcome'].unique())
    print("Value counts:\n", df['Outcome'].value_counts())
else:
    print("No 'Outcome' column found.")

date_like = [col for col in df.columns if 'date' in col.lower() or 'year' in col.lower()]
print("\n--- Other Potential Time/Index Columns ---")
print(date_like)

keywords = ['surgery', 'treatment', 'therapy']
possible_treatment_cols = [col for col in df.columns if any(k in col.lower() for k in keywords)]

if possible_treatment_cols:
    print("\nPossible treatment/surgery columns found:", possible_treatment_cols)
    print("Sample values from these columns:")
    for col in possible_treatment_cols:
        print(f"\n{col}:\n", df[col].value_counts(dropna=False).head())
else:
    print("\nNo obvious treatment or surgery columns found.")

print("\n--- Inference ---")
if 'year_of_diagnosis' in df.columns:
    print("✔ 'year_of_diagnosis' is the most likely index date.")
    print("Recommendation: Align the 'Outcome' interpretation as occurring after diagnosis year.")
else:
    print("✘ Unable to determine index date confidently. Review metadata or add date columns.")

print("\n--- Done ---")

# Insight

# This script provides an overview of the dataset `canbrs_dataset_polish.csv`, checking for potential index dates, outcome columns, and treatment-related columns. It identifies the year of diagnosis as a likely index date and suggests aligning the outcome interpretation accordingly. 