# CanBRs Therapeutics Project

This project focuses on analyzing and modeling data from the CanBRs dataset, which includes various patient attributes and clinical outcomes. The goal is to develop predictive models that can assist in understanding breast cancer treatment responses.

## Data Preparation and Analysis

- **Duplicate Checks:** The dataset `canbrs_dataset_polish.csv` has been thoroughly checked for duplicate patient IDs and fully duplicated rows. No duplicates were found in either category, ensuring data uniqueness at both the patient and record level.
- **Missingness Analysis:** A comprehensive analysis of missing values revealed that only the `site_liver` column contains missing entries. This missingness is random and has been noted for completeness rather than being flagged as an error, aligning with observations from the range check script. All other variables in the dataset are complete.
- **Range Checks:** Values within the dataset were validated against predefined expected ranges. The only deviation observed was a single missing entry in the `site_liver` column, which, consistent with the missingness analysis, is not considered an error but is acknowledged for a complete understanding of the data.