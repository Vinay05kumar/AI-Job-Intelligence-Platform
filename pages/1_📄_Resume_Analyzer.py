import streamlit as st

from services.resume_service import read_resume
from app.ats.suggestions import matched_skills

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analyzer")

uploaded = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded:

    resume = read_resume(uploaded)

    st.success("Resume Uploaded Successfully")

    st.subheader("Resume Preview")

    st.text_area(
        "",
        resume,
        height=300
    )
    from app.ats.scorer import calculate_similarity

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as f:

    jd = f.read()

score = calculate_similarity(
    resume,
    jd
)

st.metric(
    "ATS Score",
    f"{score}%"
)

st.progress(score/100)
matched = matched_skills(
    resume,
    jd
)

st.subheader("Matched Skills")

for skill in matched:

    st.success(skill.title())
from app.ats.suggestions import missing_skills

missing = missing_skills(
    resume,
    jd
)

st.subheader("Missing Skills")

for skill in missing:

    st.error(skill.title())

from app.ats.suggestions import resume_suggestions

suggestions = resume_suggestions(
    resume,
    jd
)

st.subheader("Suggestions")

for item in suggestions:

    st.info(item)    
        