import streamlit as st
from predict_page import Predict
from explore_page import Explore


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    Predict.show_predict_page()
else:
    print("sorting it")
    Explore.show_explore_page()
