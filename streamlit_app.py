import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
from streamlit_option_menu import option_menu

from services.dashboard_service import load_dashboard

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Job Intelligence Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD DATA
# ==========================================================

stats = load_dashboard()
df = pd.read_csv("data/raw/jobs.csv")

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("## 💼 AI Job Intelligence")

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Resume Analyzer",
            "Salary Prediction",
            "Analytics Dashboard",
            "Job Search",
            "About"
        ],
        icons=[
            "house",
            "file-earmark-person",
            "currency-dollar",
            "bar-chart",
            "search",
            "info-circle"
        ],
        default_index=0,
    )

# ==========================================================
# HOME
# ==========================================================

if selected == "Home":

    st.title("🤖 AI Job Intelligence Platform")

    st.caption("AI Powered Career Intelligence Platform")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Jobs", stats["jobs"])
    col2.metric("Companies", stats["companies"])
    col3.metric("Skills", stats["skills"])
    col4.metric("Locations", stats["locations"])

    st.divider()

    st.subheader("🚀 Features")

    c1, c2 = st.columns(2)

    with c1:

        st.success("Resume ATS Analysis")
        st.success("Resume Skill Gap Detection")
        st.success("Salary Prediction")
        st.success("Job Search")

    with c2:

        st.success("Hiring Trends")
        st.success("Analytics Dashboard")
        st.success("AI Resume Suggestions")
        st.success("Power BI Dashboard")

    st.divider()

    # ======================================================
    # Jobs by Location
    # ======================================================

    st.subheader("📍 Jobs by Location")

    fig = px.histogram(
        df,
        x="Location",
        color="Location",
        title="Jobs by Location"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ======================================================
    # Top Skills
    # ======================================================

    st.subheader("🔥 Top Skills")

    skills = Counter()

    for row in df["Skills"]:

        skill_list = [
            s.strip()
            for s in row.split(",")
        ]

        skills.update(skill_list)

    top_skills = skills.most_common(10)

    skill_df = pd.DataFrame(
        top_skills,
        columns=[
            "Skill",
            "Count"
        ]
    )

    fig = px.bar(
        skill_df,
        x="Skill",
        y="Count",
        color="Count",
        title="Most In-Demand Skills"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ======================================================
    # Recent Jobs
    # ======================================================

    st.subheader("📋 Recent Jobs")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

# ==========================================================
# RESUME ANALYZER
# ==========================================================

elif selected == "Resume Analyzer":

    st.title("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("Resume Uploaded Successfully!")

        st.info("ATS Analysis will be added in the next step.")

# ==========================================================
# SALARY PREDICTION
# ==========================================================

elif selected == "Salary Prediction":

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

    if st.button("Predict Salary"):

        st.success("Salary Prediction module will be connected next.")

# ==========================================================
# ANALYTICS DASHBOARD
# ==========================================================

elif selected == "Analytics Dashboard":

    st.title("📊 Analytics Dashboard")

    st.write("Interactive analytics will be added in upcoming steps.")

    st.dataframe(df)

# ==========================================================
# JOB SEARCH
# ==========================================================

elif selected == "Job Search":

    st.title("🔍 Search Jobs")

    keyword = st.text_input("Search Role")

    if keyword:

        result = df[
            df["Role"].str.contains(
                keyword,
                case=False
            )
        ]

        st.dataframe(
            result,
            use_container_width=True
        )

# ==========================================================
# ABOUT
# ==========================================================

elif selected == "About":

    st.title("ℹ About")

    st.markdown(
        """
## AI Job Intelligence Platform

A complete AI-powered career assistant built using:

- Python
- Streamlit
- SQLite
- Machine Learning
- Scikit-Learn
- Plotly
- Pandas
- NLP
- ATS Resume Matching

### Upcoming Features

- Resume Upload
- ATS Score
- Skill Gap Analysis
- AI Resume Suggestions
- Salary Prediction
- Interactive Dashboard
- Real Job Dataset (100K+)
- Deployment
"""
    )