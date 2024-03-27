import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        info = pickle.load(file)
    return info


class Predict:
    data = load_model()
    regressor = data["model"]
    le_country = data["le_country"]
    le_education = data["le_education"]

    def show_predict_page(self, le_country=None, le_education=None, regressor=None):
        st.title("Software Developer Salary Prediction")

        st.write("""### We need some information to predict the salary""")

        countries = (
            "United States of America",
            "India",
            "United Kingdom of Great Britain and Northern Ireland",
            "Germany",
            "Canada",
            "Brazil",
            "France",
            "Spain",
            "Australia",
            "Netherlands",
            "Poland",
            "Italy",
            "Russian Federation",
            "Sweden",
            "Switzerland"
        )

        education = (
            "Less than a Bachelors",
            "Bachelor’s degree",
            "Master’s degree",
            "Post grad",
        )

        country = st.selectbox("Country", countries)
        education = st.selectbox("Education Level", education)

        expericence = st.slider("Years of Experience", 0, 50, 3)

        ok = st.button("Calculate Salary")
        if ok:
            x = np.array([[country, education, expericence]])
            x[:, 0] = le_country.transform(x[:, 0])
            x[:, 1] = le_education.transform(x[:, 1])
            x = x.astype(float)

            salary = regressor.predict(x)
            st.subheader(f"The estimated salary is ${salary[0]:.2f}")
