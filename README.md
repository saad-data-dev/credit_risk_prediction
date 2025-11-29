# Credit Risk Prediction

## 🎯 Project Overview

Credit Risk Prediction is a machine-learning project that predicts whether a credit card client will default on their payment next month. The project uses demographic data, credit history, payment behavior, and financial information to build predictive models identifying high-risk clients.

This repository includes the full data science pipeline: data cleaning, exploratory data analysis (EDA), feature engineering, model training, evaluation, and interpretation.

---

## 📂 Repository Structure

```
credit_risk_prediction/
│
├── data/                  # Raw & cleaned datasets
├── notebooks/             # Jupyter notebooks (EDA, modeling, analysis)
├── scripts/               # Scripts for data cleaning, preprocessing, utilities
├── visualization/         # Plots, charts, heatmaps for EDA & results
├── requirements.md        # Project dependencies
├── Steps.md               # Workflow / project steps
├── analysis_report.md     # Detailed EDA & analysis report
├── ML_model_report.md     # Final model evaluation & interpretation report
└── README.md              # Project overview and instructions (this file)
```

> *Note:* Adjust directory names if file structure changes.

---

## 🧰 Requirements

To run this project, you need:

* **Python 3.8+**

* Core libraries:

  * `pandas`, `numpy` — data manipulation & numerical operations
  * `matplotlib`, `seaborn` — visualization & plotting
  * `scikit-learn` — preprocessing, model training & evaluation

* Optional / recommended:

  * `jupyter` — interactive notebooks
  * `imbalanced-learn` — handling class imbalance (SMOTE, undersampling)
  * `xgboost`, `lightgbm` — advanced boosting models

* Dataset: `default of credit card clients.csv` (CSV with `;` separator) containing financial, demographic, payment history, and target variable `default payment next month`.

Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
# optionally
pip install imbalanced-learn xgboost lightgbm jupyter
```

---

## 🚀 Workflow / Project Steps

1. **Import required libraries**
2. **Load dataset** — read CSV and preview data
3. **Data cleaning & preprocessing**

   * Remove duplicate headers or incorrect rows
   * Rename columns
   * Convert values to numeric and handle missing/invalid values
   * Clip out-of-range values (ages, payment history, amounts)
   * Drop irrelevant columns (e.g., `ID`)
   * Remove duplicates
4. **Exploratory Data Analysis (EDA)**

   * Statistical summary, distribution plots, correlation heatmap
   * Analyze target variable distribution
5. **Feature engineering & data preparation**

   * Separate features (`X`) and target (`y`)
   * Train/test split with stratification
   * Scale numerical features
   * Optionally engineer new features (interactions, aggregated scores, consistency)
6. **Model training**

   * Baseline model: Logistic Regression
   * Optional advanced models: Random Forest, XGBoost, LightGBM
7. **Evaluation**

   * Compute metrics: accuracy, precision, recall, F1-score, confusion matrix
   * Focus on recall/F1 for default class
8. **Interpretation & insights**

   * Analyze model strengths/weaknesses
   * Identify key features and business implications
9. **Reporting & documentation**

   * Save cleaned data
   * Document findings and limitations in Markdown reports
10. **Future improvements**

    * Handle class imbalance, hyperparameter tuning, advanced features, explainable AI

---

## 📊 Expected Outcomes

* Cleaned dataset ready for analysis
* EDA results including distributions, correlations, and target imbalance checks
* Modeling results with evaluation metrics and confusion matrices
* Detailed Markdown reports summarizing findings and recommendations

---

## ⚠️ Limitations & Considerations

* Dataset is **imbalanced**, biasing models toward majority class
* Baseline model may have **low recall for default class**, risking missed high-risk clients
* Financial and regulatory constraints require careful interpretation before deployment

---

## 🔭 Future Work

* Implement resampling or class-weight strategies to address class imbalance
* Train advanced models with hyperparameter tuning
* Engineer additional features (payment trends, ratios, aggregated scores)
* Add explainable AI techniques (SHAP, feature importance)
* Extend dataset for validation and robustness

---

## 📄 Author & Contact

**Saad EL FATINE** — Data Analyst / Data Scientist
📩 Email: [e.saad@etudiant.edcparis.edu](mailto:e.saad@etudiant.edcparis.edu)
🔗 GitHub: [https://github.com/saad-data-dev](https://github.com/saad-data-dev)
🔗 LinkedIn: [https://www.linkedin.com/in/saad-el-fatine](https://www.linkedin.com/in/saad-el-fatine)

---

## 🔗 References

* UCI Dataset: Default of Credit Card Clients ([link](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients))
