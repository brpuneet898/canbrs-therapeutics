# Model Evaluation: Balanced Random Forest

This document summarizes the key performance metrics for the **Balanced Random Forest** model.

---

## 1. Overall Performance Metrics

- **Accuracy:** `0.9117`  
  The model correctly predicts the outcome (Alive/Dead) approximately **91.17%** of the time.

- **ROC AUC Score:** `0.9436`  
  Indicates a strong ability of the model to distinguish between the 'Alive' and 'Dead' classes. A score of **1.0** would represent a perfect classifier.

- **95% Confidence Interval for ROC AUC:** `(0.917, 0.965)`  
  Suggests that if the experiment were repeated many times, the true ROC AUC score would fall within this range **95% of the time**.

- **PR AUC Score (Precision-Recall AUC):** `0.9847`  
  Especially important for imbalanced datasets, as it focuses on the **positive class ('Alive')**. A high PR AUC indicates that the model maintains **high precision as recall increases**, which is desirable for identifying the 'Alive' cases effectively.

- **95% Confidence Interval for PR AUC:** `(0.974, 0.992)`  
  Provides a range for the **true PR AUC score**.

- **Brier Score:** `0.0705`  
  Measures the accuracy of **probabilistic predictions**. A lower score indicates better **calibration**, meaning the predicted probabilities are closer to the actual outcomes. A score of **0** would be a perfect prediction.

---

## 2. Classification Report

The classification report provides a detailed breakdown of **precision**, **recall**, and **F1-score** for each class:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Alive | 0.74      | 0.78   | 0.76     | 108     |
| Dead  | 0.95      | 0.94   | 0.95     | 492     |

- **Accuracy:** `0.91` (600 samples)

| Metric       | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| Macro Avg    | 0.85      | 0.86   | 0.85     | 600     |
| Weighted Avg | 0.91      | 0.91   | 0.91     | 600     |

### Interpretation

#### Alive Class (Minority Class)

- **Precision (0.74):** When the model predicts 'Alive', it is correct 74% of the time.
- **Recall (0.78):** The model correctly identifies 78% of all actual 'Alive' cases.
- **F1-Score (0.76):** The harmonic mean of precision and recall, providing a balanced measure of the model's performance on the 'Alive' class.

#### Dead Class (Majority Class)

- **Precision (0.95):** When the model predicts 'Dead', it is correct 95% of the time.
- **Recall (0.94):** The model correctly identifies 94% of all actual 'Dead' cases.
- **F1-Score (0.95):** A very strong F1-score for the 'Dead' class, indicating excellent performance.

- **Macro Avg:** Calculates metrics independently for each class and then averages them, treating all classes equally.
- **Weighted Avg:** Averages metrics weighted by the number of true instances per class, accounting for class imbalance.

---

## 3. Visualizations (Refer to Provided Images)

### Confusion Matrix

|                    | Predicted Alive | Predicted Dead |
|--------------------|------------------|-----------------|
| **Actual Alive**   | 84 (TP)           | 24 (FP)         |
| **Actual Dead**    | 29 (FN)           | 463 (TN)        |

- This matrix visually confirms the model's ability to **correctly classify 'Dead' instances** more often than 'Alive' instances, as expected given the class imbalance.

### ROC Curve

- Illustrates the trade-off between **True Positive Rate (TPR)** and **False Positive Rate (FPR)** at various threshold settings.
- The curve is well above the diagonal, indicating **strong discriminatory power**.

### Calibration Plot

- Compares predicted probabilities to actual outcomes.
- The reliability curve deviates slightly from the **Perfect Calibration** line, especially in mid-range probabilities.
- However, the **Brier Score** suggests **overall good calibration**.

### Precision-Recall Curve

- Shows the trade-off between **precision and recall** for different thresholds.
- The high **PR AUC** confirms that the model maintains **high precision even as recall increases**, crucial for identifying the minority 'Alive' class.

---

## Conclusion

The **Balanced Random Forest** model demonstrates **strong overall performance**, with high **accuracy**, **ROC AUC**, and **PR AUC** scores.

- While there's a **slight imbalance** in performance between the 'Alive' and 'Dead' classes, the model still performs **reasonably well on the minority 'Alive' class**, as evidenced by its precision, recall, and F1-score.
- The **Brier Score** indicates **good calibration** of predicted probabilities.

---
