#======================================
#|        Data Cleaning Step          |
#======================================

# ===============================
# 1. Import required libraries
# ===============================

import pandas as pd
import numpy as np


# ===============================
# 2. Load the dataset
# ===============================

df = pd.read_csv('default of credit card clients.csv', sep=';')

# Preview the first rows
print(df.head())

# First cleaning data
new_cols = df.iloc[0].tolist()
df = df.iloc[1:].reset_index(drop=True)
df.columns = new_cols

# Convert relevant columns to numeric types
numeric_cols = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE',
                'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6',
                'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
                'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
                'default payment next month']

for col in numeric_cols:
    # Convert to numeric, coercing errors will turn non-convertible values into NaN
    df[col] = pd.to_numeric(df[col], errors='coerce')

print(df.head())

# ===============================
# 3. Inspect dataset structure
# ===============================
print("Dataset Info:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumber of duplicated rows:", df.duplicated().sum())

#================================
# 4. Cleaning dataset
#================================

#replace the out-of-context data in the marriage column
df['MARRIAGE'] = df['MARRIAGE'].replace({0:3})

#replace out-of-range values ​​from PAY_X
for col in ['PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']:
    df[col] = df[col].clip(-2, 8)

#check the consistency of the BILL_AMT and PAY_AMT columns
bill_cols = [c for c in df.columns if "BILL_AMT" in c]
pay_cols = [c for c in df.columns if "PAY_AMT" in c]

for col in bill_cols + pay_cols:
    df[col] = df[col].clip(lower=0)

#AGE column normalization
df['AGE'] = df['AGE'].clip(18, 80)

#delete ID column
df = df.drop(columns=['ID'])

#check for duplicates
df = df.drop_duplicates()

#Inspect dataset structure

print("Dataset Info:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumber of duplicated rows:", df.duplicated().sum())

# ===============================
# 4. Save Cleaned Dataset
# ===============================
df.to_csv("default_of_credit_card_clients_clean.csv", index=False)
print("\n💾 Clean dataset saved as default_of_credit_card_clients_clean.csv")

#======================================
#|      Exploratory Data Analysis     |
#======================================

import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# 1. Basic statistical summary
# ===============================
print("Statistical Summary:")
display(df.describe())

# ===============================
# 2. Distribution of target variable
# ===============================
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='default payment next month')
plt.title("Target Variable Distribution")
plt.xlabel("Default Payment Next Month (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# Percentage default
default_rate = df['default payment next month'].mean() * 100
print(f"📌 Default Rate: {default_rate:.2f}%")

# ===============================
# 3. Correlation heatmap
# ===============================
plt.figure(figsize=(16,10))
sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap")
plt.show()

#============================================
#|   Feature Engineering & Data Preparation |
#============================================

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ===============================
# 1. Feature / Target separation
# ===============================
X = df.drop(columns=["default payment next month"])
y = df["default payment next month"]

# ===============================
# 2. Train-test split
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# ===============================
# 3. Scaling numerical features
# ===============================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Data Scaling Completed ✔")

#======================================
#|      Machine Learning Models       |
#======================================

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ===============================
# 1. Logistic Regression Model
# ===============================
model = LogisticRegression(max_iter=200)
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)

# ===============================
# 2. Evaluation
# ===============================

acc = accuracy_score(y_test, y_pred)
print(f"📌 Accuracy: {acc:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()