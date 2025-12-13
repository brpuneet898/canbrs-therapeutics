# CanBRs Therapeutics — Predictive Modeling of Clinical Outcome

Short description
This repository contains the data processing, feature engineering, model development, evaluation, and explainability artifacts used to build predictive models for clinical outcomes in the CanBRs dataset (breast cancer cohort). The primary objective is to predict patient `Outcome` (Alive / Dead) using demographic, tumor, receptor-status, and metastasis variables while carefully handling class imbalance and model calibration.

Table of contents
- Overview
- Repository structure
- Quickstart (reproduce main model)
- Data (files, provenance, privacy)
- Data dictionary
- Pre-check scripts (what they do, how to use)
- Notebooks (ordered list, purpose, inputs/outputs)
- Modeling pipeline (design, preprocessing, balancing, algorithms)
- Model evaluation summary (key metrics and interpretation)
- Reproducibility & environment
- Outputs and artifacts
- Limitations and caveats
- Recommended repository improvements
- Authors & contact
- Appendix: commands & references

Overview
- Context: This project explores the CanBRs clinical dataset to (1) prepare and validate input data, (2) engineer features relevant to breast cancer prognosis, (3) train and evaluate classifiers that predict patient outcome, and (4) explain model behavior using SHAP.
- Goals:
	- Build robust, reproducible predictive pipelines that handle class imbalance.
	- Produce well-calibrated probability estimates.
	- Provide interpretable local and global explanations for model predictions.
- High-level finding (summary): The lead model, a Balanced Random Forest pipeline with sampling (SMOTE in experimentation) and cross-validation, achieved:
	- Accuracy: 0.9117
	- ROC AUC: 0.9436 (95% CI: 0.917–0.965)
	- PR AUC: 0.9847 (95% CI: 0.974–0.992)
	- Brier score: 0.0705
	See `model_eval_vFINAL.md` for full evaluation tables, confusion matrix, and diagnostic plots.

Repository structure (high-level)
- Root:
	- `README.md` (this file)
	- `requirements.txt` — Python dependencies used for notebooks and scripts
	- `variables.yaml` — canonical data dictionary and variable types
	- `model_eval_vFINAL.md` — final model evaluation and interpretation
- Notebooks (analysis & modeling):
	- `CanBrs_Therapeutics_*.ipynb` (multiple versions; see Notebooks section below)
	- `corr_final.ipynb`, `final_modeling.ipynb`, `summary_counts.ipynb`
- Data:
	- `datasets/canbrs_dataset_raw.csv` — original CSV (source)
	- `datasets/canbrs_dataset_polish.csv` — curated / polished CSV used in analysis
- Pre-check scripts:
	- `pre_check_scripts/` — utilities for validation, conversions, and reports
- (recommended) Artifacts (not present yet): `models/`, `outputs/` — for saving trained models and figures

Quickstart — reproduce the main model (concise)
1. Create and activate a virtual environment (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
2. Convert raw CSV to parquet for faster I/O (optional but recommended):
```powershell
python pre_check_scripts/csv_to_parquet.py datasets/canbrs_dataset_raw.csv datasets/canbrs_dataset_polish.parquet
```
3. Run pre-checks (duplicates, missingness, range checks):
```powershell
python pre_check_scripts/check_duplicates.py datasets/canbrs_dataset_polish.csv
python pre_check_scripts/missingness_report.py datasets/canbrs_dataset_polish.csv
python pre_check_scripts/range_check.py datasets/canbrs_dataset_polish.csv
```
4. Execute the main modeling notebook (recommended order described later) or run headless:
```bash
jupyter nbconvert --to notebook --execute CanBrs_Therapeutics_21_04_27_04_SMOTE+BalancedRF+CrossValidation.ipynb --ExecutePreprocessor.timeout=1800
```

Data
- Files:
	- `datasets/canbrs_dataset_raw.csv`: raw input with original encodings.
	- `datasets/canbrs_dataset_polish.csv`: cleaned and standardized CSV used downstream.
- Quality & notes:
	- Duplicate checks show no duplicate patient IDs or fully duplicated records.
	- Missingness: only `site_liver` shows missing entries; missingness appears random and is documented in pre-check outputs.
	- Range validation: performed using `pre_check_scripts/range_check.py`; only `site_liver` had missingness; no other range violations noted.
- Provenance & governance:
	- If this dataset contains PHI or is restricted, follow local data governance for storage and sharing. The repository does not include personal identifiers beyond the `ID` field and should remain under appropriate access controls if sensitive.

Data dictionary
- Source: `variables.yaml` — this file contains types and short descriptions for all variables used in the notebooks.
- Key variables (high-level):
	- `ID` — patient identifier
	- `age`, `year_of_diagnosis`
	- `race`, `marital_status`, `primary_site`
	- `regional_nodes_positive`, `regional_nodes_examined`
	- `site_bone`, `site_brain`, `site_liver`, `site_lung`
	- `subtype`, `er_status`, `pr_status`, `her2_status`
	- `Outcome` — target variable (Alive/Dead)
- Note on encodings: many categorical fields are encoded numerically (e.g., `subtype` values `1,3,4`); refer to notebook cells where decodings/mappings are applied if you need human-readable labels.

Pre-check scripts (what they do)
All scripts are located in `pre_check_scripts/`. Short descriptions and usage:
- `analyze_index_outcome.py` — analyzes distribution of index and outcome variables; usage: `python pre_check_scripts/analyze_index_outcome.py datasets/canbrs_dataset_polish.csv`
- `check_duplicates.py` — checks duplicates at ID and row level; usage: `python pre_check_scripts/check_duplicates.py datasets/canbrs_dataset_polish.csv`
- `compute_q_values.py` — helper to compute q-values for multiple testing corrections; usage depends on the statistics notebook.
- `csv_to_parquet.py` — converts CSV to parquet; usage: `python pre_check_scripts/csv_to_parquet.py <input.csv> <output.parquet>`
- `missing_value.py` — imputation helper functions and small pipelines; used by imputation notebooks.
- `missingness_report.py` — generates a missingness summary and optional plots; usage: `python pre_check_scripts/missingness_report.py datasets/canbrs_dataset_polish.csv`
- `range_check.py` — validates numeric ranges and reports anomalies; usage: `python pre_check_scripts/range_check.py datasets/canbrs_dataset_polish.csv`

Notebooks — ordered workflow and purpose
These notebooks capture the evolution of the analysis. Recommended order to reproduce or review findings:
1. `CanBrs_Therapeutics_01_07.ipynb` — initial exploratory data analysis (EDA), visualizations, and raw variable inspection.
2. `CanBrs_Therapeutics_02_07.ipynb` — additional EDA, missingness visuals, initial transformations.
3. `CanBrs_Therapeutics_04_06_11_06.ipynb` — intermediate feature engineering and baseline modeling experiments.
4. `CanBrs_Therapeutics_17_04_20_04.ipynb` — feature engineering iterations and selection logic.
5. `CanBrs_Therapeutics_21_04_27_04_FE_ER_PR_Bins.ipynb` — feature engineering concentrating on ER/PR variables and binning strategies.
6. `CanBrs_Therapeutics_21_04_27_04_Imputation_Pipelines.ipynb` — imputation strategy comparisons and pipeline patterns.
7. `CanBrs_Therapeutics_21_04_27_04_SMOTE+BalancedRF+CrossValidation.ipynb` — main modeling notebook that implements SMOTE + Balanced Random Forest with cross-validation; this notebook is the core to reproduce the lead model.
8. `CanBrs_Therapeutics_21_07.ipynb` — consolidated model runs and final parameter choices.
9. `CanBrs_Therapeutics_26_05_30_05_explain_shap_plots.ipynb` — local SHAP explanation examples and detailed plots for illustrative cases.
10. `CanBrs_Therapeutics_28_04_04_05_extended_feature_engineering.ipynb` — extended feature engineering experiments.
11. `CanBrs_Therapeutics_28_04_04_05_global_shap.ipynb` — global SHAP analyses for feature importance summary.
12. `CanBrs_Therapeutics_28_04_04_05_model_quality_deep_dive.ipynb` — calibration curves, reliability analysis, error case studies.
13. `CanBrs_Therapeutics_28_04_04_05_model_zoo_expansion_and_tuning.ipynb` — testing multiple model types and hyperparameter grids.
14. `corr_final.ipynb` — correlation analysis and multicollinearity checks.
15. `final_modeling.ipynb` — consolidated final modeling pipeline; this notebook contains the final steps to produce the model reported in `model_eval_vFINAL.md`.
16. `summary_counts.ipynb` — tables of cohort sizes, filters applied, and summary counts.

For each notebook include:
- Inputs: typically `datasets/canbrs_dataset_polish.csv` (or parquet) and any saved intermediate artifacts.
- Outputs: figures (ROC, PR, calibration), tables (confusion matrices, classification reports), and serialized models/SHAP explainers where applicable.
- Runtime: variable by notebook; heavy modeling and SHAP notebooks can take minutes to tens of minutes depending on CPU.

Modeling pipeline — design and implementation
- Preprocessing steps applied across pipelines:
	- Standard missing-value handling (imputation pipelines explored in `*_Imputation_Pipelines.ipynb`). Categorical unknown vs explicit NA handling documented in notebooks.
	- Categorical encoding: mix of one-hot and label/ordinal encodings depending on model and cardinality (notebook cells show exact encoders used).
	- Numeric transformations: standard scaling for tree-agnostic models where required; trees often used without scaling.
	- Feature selection: correlation checks (`corr_final.ipynb`) and feature importance-driven pruning.
- Class imbalance handling:
	- SMOTE (Synthetic Minority Oversampling) used in experimentation and combined with cross-validation pipelines.
	- BalancedRandomForest (from `imbalanced-learn`) used as a primary model that natively addresses imbalance by reweighting samples during tree building.
- Algorithms explored:
	- Balanced Random Forest (lead model)
	- Random Forest variants, Gradient Boosted Trees (where applicable)
	- Baselines: logistic regression, simple decision trees
- Explainability:
	- SHAP used for local and global explanations — notebooks produce force plots, summary beeswarm plots, and dependence plots.
	- Calibration plots and Brier score used to evaluate probability quality.

Model evaluation summary (concise, interpreted)
Full evaluation is in `model_eval_vFINAL.md`. Key takeaways for the lead Balanced Random Forest:
- Accuracy: 0.9117 — high overall correctness across the dataset, influenced by class distribution.
- ROC AUC: 0.9436 (95% CI: 0.917–0.965) — strong discrimination between Alive vs Dead.
- PR AUC: 0.9847 (95% CI: 0.974–0.992) — strong precision/recall trade-off, indicates good performance on the positive class in the precision–recall plane.
- Brier score: 0.0705 — suggests reasonably good probability calibration.
- Confusion matrix (from `model_eval_vFINAL.md`):
	- True Positives (Alive predicted Alive): 84
	- False Positives: 24
	- False Negatives: 29
	- True Negatives: 463
- Class-level nuance:
	- The minority class (`Alive`) has lower precision/recall than the majority (`Dead`) due to class imbalance, but SMOTE & balanced classifiers improve minority-class detection.
- Calibration & reliability:
	- Slight deviation from perfect calibration in mid-range probabilities; however Brier score supports good overall calibration.

Reproducibility & environment
- Recommended Python versions: 3.9–3.11 (confirm locally). If you need an exact lockfile, run `pip freeze > pinned-requirements.txt`.
- Core dependencies: listed in `requirements.txt` (includes `pandas`, `numpy`, `scikit-learn`, `imbalanced-learn`, `shap`, `statsmodels`, `pyarrow`, `fastparquet`, `matplotlib`, `seaborn`, `ipykernel`).
- Setup commands (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
- Execute notebooks headlessly:
```bash
pip install nbconvert
jupyter nbconvert --to notebook --execute <notebook.ipynb> --ExecutePreprocessor.timeout=1800
```
- Determinism:
	- Use fixed random seeds in notebooks/pipelines (search for `random_state` or `seed` usage).
	- If replicating results exactly, capture environment with `pip freeze` and record Python version.

Outputs and artifacts
- Expected outputs after running notebooks:
	- Figures: ROC curves, PR curves, calibration plots, SHAP summary and local plots, confusion matrices.
	- Tables: classification reports, cross-validated metric tables, cohort summaries.
	- Model artifacts: trained model objects and SHAP explainers (recommend saving to `models/` with version tags).
- Suggested artifact directory structure (not currently present):
	- `outputs/models/` — serialized models (`.pkl` or `joblib`)
	- `outputs/figures/` — PNG/SVG or notebook-native plots
	- `outputs/tables/` — CSV/TSV summary tables

Limitations, assumptions and caveats
- Data limitations:
	- Missingness: only `site_liver` showed missing entries; the extent and mechanism of missingness should be considered when generalizing.
	- Encoding: some categorical variables are numerically encoded; human-meaningful labels may require mapping.
	- External validity: model trained on CanBRs cohort — may not generalize to different populations without external validation.
- Modeling caveats:
	- Class imbalance influences metrics; high accuracy is partly due to class distribution — inspect class-wise metrics (precision/recall) not just accuracy.
	- SMOTE introduces synthetic examples; while helpful for minority-class learning, it can introduce artifacts if feature space assumptions are violated.
- Operational caution:
	- If models are used in clinical settings, undertake prospective validation and calibration checks. Consult domain experts for variables affecting treatment decisions.
    