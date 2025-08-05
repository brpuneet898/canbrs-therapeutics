import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind
from statsmodels.stats.multitest import multipletests

# Load dataset
df = pd.read_csv('C:\My Folder\projects\canbrs-therapeutics\datasets\canbrs_dataset_polish.csv')

# Drop rows with missing Outcome
df = df.dropna(subset=['Outcome'])

# Convert Outcome to binary (if not already)
df['Outcome'] = df['Outcome'].astype('category')

# Collect p-values
p_values = []
features = []

for col in df.columns:
    if col in ['ID', 'Outcome']:
        continue

    if df[col].nunique() <= 10 or df[col].dtype == 'object' or df[col].dtype.name == 'category':
        # Categorical variable - use Chi-square test
        contingency_table = pd.crosstab(df[col], df['Outcome'])
        if contingency_table.shape[0] > 1 and contingency_table.shape[1] > 1:
            try:
                chi2, p, dof, ex = chi2_contingency(contingency_table)
            except ValueError:
                p = 1.0  # fallback for invalid contingency table
        else:
            p = 1.0
    else:
        # Continuous variable - use t-test
        try:
            groups = df.groupby('Outcome')[col]
            if groups.ngroups == 2:
                group1 = groups.get_group(groups.groups.keys()[0])
                group2 = groups.get_group(groups.groups.keys()[1])
                _, p = ttest_ind(group1.dropna(), group2.dropna(), equal_var=False)
            else:
                p = 1.0
        except:
            p = 1.0

    p_values.append(p)
    features.append(col)

# Adjust p-values using Benjamini-Hochberg (FDR) method
rejected, q_values, _, _ = multipletests(p_values, alpha=0.05, method='fdr_bh')

# Create results DataFrame
results_df = pd.DataFrame({
    'Feature': features,
    'p-value': p_values,
    'q-value': q_values
})

# Save results to markdown (optional)
results_df_sorted = results_df.sort_values(by='q-value')
results_df_sorted.to_markdown("../univariate_assoc.md", index=False)

print("Q-values calculated and saved to univariate_assoc.md")
