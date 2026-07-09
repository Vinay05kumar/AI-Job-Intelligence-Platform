"""
ats_matcher.py

ATS Resume Matching Module
AI Job Intelligence Platform
"""

import re
import pdfplumber

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================================
# EXTRACT TEXT FROM PDF
# ==========================================================

def extract_resume_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text


# ==========================================================
# CLEAN TEXT
# ==========================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text


# ==========================================================
# ATS SCORE
# ==========================================================

def calculate_ats_score(

        resume_text,
        job_description

):

    resume_text = clean_text(resume_text)

    job_description = clean_text(job_description)

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(

        [
            resume_text,
            job_description
        ]

    )

    similarity = cosine_similarity(

        vectors[0:1],
        vectors[1:2]

    )[0][0]

    score = round(

        similarity * 100,

        2

    )

    return score


# ==========================================================
# EXTRACT KEYWORDS
# ==========================================================

def extract_keywords(text):

    text = clean_text(text)

    words = text.split()

    keywords = set(words)

    return keywords


# ==========================================================
# MISSING SKILLS
# ==========================================================

def missing_skills(

        resume_text,
        job_description

):

    resume = extract_keywords(

        resume_text

    )

    job = extract_keywords(

        job_description

    )

    missing = sorted(

        list(job - resume)

    )

    return missing


# ==========================================================
# MATCHED SKILLS
# ==========================================================

def matched_skills(

        resume_text,
        job_description

):

    resume = extract_keywords(

        resume_text

    )

    job = extract_keywords(

        job_description

    )

    matched = sorted(

        list(job.intersection(resume))

    )

    return matched


# ==========================================================
# MATCH PERCENTAGE
# ==========================================================

def match_percentage(

        resume_text,
        job_description

):

    matched = matched_skills(

        resume_text,
        job_description

    )

    total = extract_keywords(

        job_description

    )

    if len(total) == 0:

        return 0

    percentage = round(

        len(matched)

        /

        len(total)

        * 100,

        2

    )

    return percentage


# ==========================================================
# RESUME SUGGESTIONS
# ==========================================================

def resume_suggestions(

        resume_text,
        job_description

):

    missing = missing_skills(

        resume_text,
        job_description

    )

    suggestions = []

    for skill in missing:

        suggestions.append(

            f"Add '{skill}' to your resume if you have experience with it."

        )

    return suggestions


# ==========================================================
# PRINT ATS REPORT
# ==========================================================

def print_ats_report(

        resume_text,
        job_description

):

    print("\n")

    print("=" * 70)

    print("ATS REPORT")

    print("=" * 70)

    score = calculate_ats_score(

        resume_text,

        job_description

    )

    print(f"\nATS Score : {score}%")

    print("\nMatched Skills")

    print("-" * 40)

    for skill in matched_skills(

            resume_text,

            job_description

    ):

        print(skill)

    print("\nMissing Skills")

    print("-" * 40)

    for skill in missing_skills(

            resume_text,

            job_description

    ):

        print(skill)

    print("\nSuggestions")

    print("-" * 40)

    for suggestion in resume_suggestions(

            resume_text,

            job_description

    ):

        print(suggestion)

    print("\n")

    print("=" * 70)