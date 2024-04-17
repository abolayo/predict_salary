import streamlit as st

from pages.explore_page import show_explore_page

from pages.predict_page import show_predict_page

page = st.sidebar.selectbox("Explore Or Predict", ["Predict", "Explore"])

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    st.subheader("This page is under construction")
    show_explore_page()
