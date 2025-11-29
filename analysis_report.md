# 📊 1. Target Variable Distribution — “Default Payment Next Month”

## ✔ What the Plot Shows
The first plot illustrates the distribution of the target variable:  
**default payment next month**

- **0 = no default payment**
- **1 = default payment**

## ✔ Analysis
Most clients belong to class **0** (no default):

- **≈ 23,000 clients**

Class **1** (clients who defaulted the next month) represents a minority:

- **≈ 7,000 clients**

Default Rate: 22.12%

## ✔ Interpretation
The dataset is **highly imbalanced**, with far more clients paying on time than clients defaulting.

This imbalance can cause issues in Machine Learning classification:
→ A model may learn to always predict **0**, as it is the dominant class.

## ✔ Implications for Machine Learning
To build a robust model, it will be necessary to consider:

- **Oversampling** (e.g., SMOTE)
- **Undersampling**
- **Class-weighted algorithms**
- **Appropriate metrics**: F1-score, Recall, AUC-ROC  
  → Not accuracy alone!

**Summary:**  
This is an imbalanced classification problem that must be addressed before model training.


---

# 🔥 2. Correlation Heatmap — Explanatory Variables

## ✔ What the Plot Shows
The heatmap visualizes the correlations between all numerical variables in the dataset:

- **PAY_X** columns: past payment status  
- **BILL_AMT** columns: bill amounts  
- **PAY_AMT** columns: payment amounts  
- Demographic variables  
- Credit limit  
- The target variable

## ✔ Main Observations

### 🔴 1. Strong Correlation Among PAY_X Variables
The variables PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, and PAY_6 are highly correlated.

This indicates consistent payment behavior over time:  
→ Clients who are late one month are often late the following months.

---

### 🔴 2. Strong Correlation Among BILL_AMT Columns
Bill amounts across months are also strongly correlated.  
→ Logical: clients with high credit limits tend to have high bills every month.

---

### 🔵 3. Moderate Correlations With the Target Variable
The strongest correlations with default are:

- **PAY_0** (most recent payment status)
- **PAY_2 to PAY_6** (previous late payments)

These correlations are positive:  
→ More late payments increase the likelihood of default.

---

### 🔵 4. Weaker Correlations
- **LIMIT_BAL**: weak negative correlation  
- **AGE, SEX, EDUCATION, MARRIAGE**: very weak correlations  
→ These demographic variables have limited predictive power.

---

# 🧠 Overall Interpretation

## ✔ Most important variables for predicting default
- **Payment history (PAY_0 to PAY_6)**  
  → Strongly correlated with the target and with each other.

- **Bill amounts (BILL_AMT)** and **payment amounts (PAY_AMT)**  
  → Highly correlated among themselves, though less directly with the target.

## ✔ Variables with minor influence
- **Demographics:** AGE, SEX, EDUCATION, MARRIAGE  
  → Minimal impact on default prediction.

---

# 💡 Data Scientist Conclusion

Default payment behavior is mainly driven by:

- A client’s recent ability to pay outstanding debt  
- Previous payment delays  

Financial behavioral variables provide much stronger insights than:

- Age  
- Gender  
- Marital status  
- Education level  

The correlation heatmap confirms that the model should rely heavily on:

- ✔ PAY_X variables  
- ✔ Effective feature engineering on payment behavior  
- ✔ Techniques for handling the imbalance in the target variable
