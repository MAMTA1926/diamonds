import streamlit as st
import pandas as pd
import pickle
with open("diamond_knn_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💎 Diamond Price Prediction App")
st.write("Enter diamond details to predict price")

# User Inputs
carat = st.number_input("Carat", min_value=0.1, step=0.01)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])
depth = st.number_input("Depth", min_value=0.0)
table = st.number_input("Table", min_value=0.0)
x = st.number_input("X dimension")
y = st.number_input("Y dimension")
z = st.number_input("Z dimension")

# Create input dataframe
input_data = pd.DataFrame({
    "carat": [carat],
    "cut": [cut],
    "color": [color],
    "clarity": [clarity],
    "depth": [depth],
    "table": [table],
    "x": [x],
    "y": [y],
    "z": [z]
})

# Predict
if st.button("Predict Price 💰"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Diamond Price: 💵 ${prediction[0]:.2f}")