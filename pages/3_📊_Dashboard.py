import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv("data/raw/jobs.csv")

st.title("📊 Analytics Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Jobs",
    len(df)
)

col2.metric(
    "Companies",
    df["Company"].nunique()
)

col3.metric(
    "Locations",
    df["Location"].nunique()
)

col4.metric(
    "Average Salary",
    f"{df['Salary_LPA'].mean():.2f} LPA"
)
st.subheader("Jobs by Location")

fig = px.histogram(

    df,

    x="Location",

    color="Location"

)

st.plotly_chart(

    fig,

    use_container_width=True

)
st.subheader("Salary Distribution")

fig = px.box(

    df,

    y="Salary_LPA",

    color="Role"

)

st.plotly_chart(

    fig,

    use_container_width=True

)
company = df["Company"].value_counts()

fig = px.pie(

    values=company.values,

    names=company.index,

    title="Top Hiring Companies"

)

st.plotly_chart(

    fig,

    use_container_width=True

)
from collections import Counter

skills = Counter()

for row in df["Skills"]:

    skills.update(

        [

            s.strip()

            for s in row.split(",")

        ]

    )

top = skills.most_common(15)

skill_df = pd.DataFrame(

    top,

    columns=[

        "Skill",

        "Jobs"

    ]

)

fig = px.bar(

    skill_df,

    x="Jobs",

    y="Skill",

    orientation="h"

)

st.plotly_chart(

    fig,

    use_container_width=True

)