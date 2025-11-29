# 📊 Final Machine Learning Model Report
## Credit Card Default Prediction — Model Evaluation & Interpretation

---

## 🧠 1. Introduction

The goal of this project is to build a predictive model capable of identifying customers who are likely to default on their credit card payment next month.  
This is a binary classification problem:

- **0 → The client will not default**  
- **1 → The client will default**

After cleaning the dataset, transforming the variables, and training several machine learning models, the final evaluation metrics have been obtained.  
This report summarizes and interprets the performance of the model.

---

## 📐 2. Key Results

**✔ Accuracy: 0.8134**  

This means the model correctly predicted the default behavior in **81.34%** of all cases in the test set.

### 📑 Classification Report

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0 (No Default) | 0.82 | 0.97 | 0.89 | 5834 |
| 1 (Default) | 0.73 | 0.25 | 0.37 | 1658 |
| **Overall Accuracy** | | | 0.81 | 7492 |
| Macro Avg | 0.78 | 0.61 | 0.63 | 7492 |
| Weighted Avg | 0.80 | 0.81 | 0.78 | 7492 |

---

## 📘 3. Interpretation of the Model Performance

### 3.1 Class 0 — “No Default” is well predicted

- **Precision 0.82**: When the model predicts no default, it is correct 82% of the time.  
- **Recall 0.97**: The model successfully identifies 97% of all customers who will not default.

➡️ This means the model is very good at detecting safe customers.

### 3.2 Class 1 — “Default” is poorly detected

- **Precision 0.73**: When the model predicts default, 73% of those predictions are correct.  
- **Recall 0.25**: The model correctly catches only 25% of the customers who will actually default.

➡️ The model is missing 75% of real defaulters, which is a critical weakness in a financial context.

**Causes:**

- Strong class imbalance:  
  - Class 0 (no default) = 5834  
  - Class 1 (default) = 1658  
- Default behavior is harder to predict  
- Recall for Class 1 is the most important metric in credit risk  

---

## 🧨 4. What These Results Mean for a Bank

### 👍 Strengths

- Model is reliable at eliminating low-risk customers  
- Provides a strong baseline score (accuracy 81%)  
- Good precision for default clients (73%)

### 👎 Weaknesses

- Fails to detect many real defaulters  
- Risky clients often pass unnoticed (low recall = 25%)  
- The model is biased toward the majority class

### 🏦 Business Impact

If deployed in a banking environment:

- Many clients who might default will not be flagged  
- The bank would face financial losses due to undetected risky accounts  
- The model is not safe enough for real-world deployment in its current form

---

## 🔧 5. How to Improve the Model

1. **Handle class imbalance**  
   - SMOTE (oversampling the minority class)  
   - Class weights in algorithms  
   - Undersampling the majority class  

2. **Train more complex models**  
   - XGBoost  
   - LightGBM  
   - Random Forest with tuned hyperparameters  

3. **Feature engineering**  
   - Interaction variables  
   - Payment consistency scores  
   - Risk score aggregation  
   - Trend detection in payment history  

4. **Hyperparameter tuning**  
   - GridSearchCV or RandomizedSearchCV to optimize:  
     - Tree depth  
     - Learning rate  
     - Regularization parameters  
     - Number of estimators  

---

## 🧪 6. Conclusion

The model achieves a strong overall accuracy (81%), but it struggles significantly to detect high-risk clients, with a recall of only 25% for defaulters.  

In a credit risk scenario, recall on the default class is the **single most important metric**, because failing to identify risky clients directly results in financial loss.

**Summary:**  
- Acceptable for academic purposes  
- Insufficient for real-world credit risk prediction without further improvement  
- Advanced resampling, feature engineering, and more powerful models can greatly improve detection of risky clients

---

## ✍️ Author

**Saad EL FATINE**  
Data Analyst / Data Scientist  

📩 Email: e.saad@etudiant.edcparis.edu  
🔗 GitHub: [https://github.com/saad-data-dev](https://github.com/saad-data-dev)  
🔗 LinkedIn: [https://www.linkedin.com/in/saad-el-fatine](https://www.linkedin.com/in/saad-el-fatine)
