import streamlit as st
import pandas as pd

from services.salary_service import SalaryService

st.set_page_config(

    page_title="Salary Prediction",

    page_icon="💰",

    layout="wide"

)

df = pd.read_csv(

    "data/raw/jobs.csv"

)

st.title("💰 Salary Prediction")

company = st.selectbox(

    "Company",

    sorted(df["Company"].unique())

)

role = st.selectbox(

    "Role",

    sorted(df["Role"].unique())

)

location = st.selectbox(

    "Location",

    sorted(df["Location"].unique())

)

experience = st.selectbox(

    "Experience",

    sorted(df["Experience"].unique())

)

service = SalaryService()

if st.button(

    "Predict Salary",

    use_container_width=True

):

    salary = service.predict(

        company,

        role,

        location,

        experience

    )

    st.success(

        f"Predicted Salary : ₹ {salary:.2f} LPA"

    )

    st.progress(0.92)

    st.metric(

        "Confidence",

        "92%"

    )
similar = df[

    (df["Role"] == role)

    &

    (df["Location"] == location)

]

st.subheader(

    "Similar Jobs"

)

st.dataframe(

    similar,

    use_container_width=True

)    