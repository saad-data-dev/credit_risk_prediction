# Credit Risk Prediction

## 🎯 Project Overview

Credit Risk Prediction is a machine-learning project that predicts whether a credit card client will default on their payment next month. The project uses demographic data, credit history, payment behavior, and financial information to build predictive models identifying high-risk clients.

This repository includes the full data science pipeline: data cleaning, exploratory data analysis (EDA), feature engineering, model training, evaluation, interpretation, and a simple interactive Streamlit application for testing predictions.

---

## 📂 Repository Structure

```
credit_risk_prediction/
│
├── data/                  # Raw & cleaned datasets
├── notebooks/             # Jupyter notebooks (EDA, modeling, analysis)
├── scripts/               # Scripts for data cleaning, preprocessing, utilities
├── visualization/         # Plots, charts, heatmaps for EDA & results
├── api/                   # Streamlit application for interactive testing
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
  * `joblib` — saving/loading trained models
  * `streamlit` — interactive web application

* Optional / recommended:

  * `jupyter` — interactive notebooks
  * `imbalanced-learn` — handling class imbalance (SMOTE, undersampling)
  * `xgboost`, `lightgbm` — advanced boosting models

* Dataset: `default of credit card clients.csv` (CSV with `;` separator) containing financial, demographic, payment history, and target variable `default payment next month`.

Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib st
```
