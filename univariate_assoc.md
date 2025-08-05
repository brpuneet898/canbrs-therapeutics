| Feature                 |     p-value |     q-value |
|:------------------------|------------:|------------:|
| site_liver              | 1.62993e-16 | 2.44489e-15 |
| race                    | 1.51257e-11 | 1.13443e-10 |
| site_lung               | 4.80558e-11 | 2.40279e-10 |
| primary_site            | 8.66042e-07 | 3.24766e-06 |
| site_brain              | 8.23734e-06 | 2.4712e-05  |
| pr_status               | 2.41829e-05 | 6.04573e-05 |
| er_status               | 6.892e-05   | 0.000129225 |
| subtype                 | 6.29529e-05 | 0.000129225 |
| her2_status             | 0.00106555  | 0.00177592  |
| marital_status          | 0.00484685  | 0.00727027  |
| site_bone               | 0.408058    | 0.556443    |
| age                     | 1           | 1           |
| regional_nodes_examined | 1           | 1           |
| regional_nodes_positive | 1           | 1           |
| year_of_diagnosis       | 1           | 1           |

## Understanding the Table Columns 

- **Feature**: Variable from the dataset tested for association with the outcome.
- **p-value**: The raw statistical significance from the univariate test.
- **q-value**: The FDR-adjusted p-value using the Benjamini-Hochberg procedure to account for multiple testing.

## Strongly Significant Features (q-value < 0.05)

These variables show **statistically significant association** with the outcome even after multiple test correction:

- **`site_liver`**  
  - 🔥 Extremely significant  
  - Strongly associated with outcome; liver involvement may indicate worse prognosis.

- **`race`**  
  - Demographic factor significantly associated with the outcome.

- **`site_lung`**  
  - Lung metastasis or involvement is highly significant.

- **`primary_site`**  
  - Origin of the cancer is significantly linked to the outcome.

- **`site_brain`**  
  - Brain involvement shows meaningful outcome differences.

- **`pr_status`**, **`er_status`**, **`her2_status`**  
  - Hormone receptor statuses are key predictors of outcome, consistent with oncological literature.

- **`subtype`**  
  - Subtype of cancer is significantly associated with the outcome.

- **`marital_status`**  
  - Borderline significant; social factors may influence health outcomes.

## Non-Significant Features (q-value ≈ 1)

These features did **not** show statistically significant association with the outcome:

- **`site_bone`**  
  - No strong association found.

- **`age`**  
  - No significant univariate relationship with the outcome.

- **`regional_nodes_examined`**, **`regional_nodes_positive`**  
  - No meaningful difference in outcome detected based on node involvement alone.

- **`year_of_diagnosis`**  
  - No time-based trend detected in outcome variation.

## Interpretation Notes

- **Low q-values** (e.g., < 0.05): Indicate reliable and statistically significant features after correcting for multiple comparisons.
- **High q-values** (e.g., ≈ 1): Suggest no strong evidence of association.
- **Univariate limitations**: These results do not account for confounding or feature interactions.
