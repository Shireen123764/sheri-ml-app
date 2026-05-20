import streamlit as st
import pickle


st.title("House Price Prediction ml app")

area = pickle.load(open("area.pkl","rb"))# rb run binary
area_sq = st.number_input("Enter an area in SQ-FT", min_value=500)

if st.button("Predict Price"):
    input_data = [[area_sq]]
    predicted_price = area.predict(input_data)
    st.success(f"Your predicted price for {area_sq} is : {predicted_price[0]}")