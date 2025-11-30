import streamlit as st
import pandas as pd
import joblib

# Charger le modèle
model = joblib.load('credit_model.pkl')

st.title("Prédiction du risque de crédit")
age = st.number_input("Âge")
income = st.number_input("Revenu")

# Prédiction
if st.button("Prédire"):
    data = pd.DataFrame({'age':[age],'income':[income]})
    pred = model.predict(data)
    st.write("Risque de défaut :", pred[0])