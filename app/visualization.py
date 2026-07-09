"""
visualization.py

Visualization Module
AI Job Intelligence Platform
"""

import os
import matplotlib.pyplot as plt


# ==========================================================
# CREATE DASHBOARD FOLDER
# ==========================================================

os.makedirs("dashboard", exist_ok=True)


# ==========================================================
# TOP SKILLS BAR CHART
# ==========================================================

def plot_top_skills(skill_counter):

    top_skills = skill_counter.most_common(10)

    skills = [item[0] for item in top_skills]
    counts = [item[1] for item in top_skills]

    plt.figure(figsize=(12,6))

    plt.bar(
        skills,
        counts,
        edgecolor="black"
    )

    plt.title("Top 10 Most Demanded Skills")

    plt.xlabel("Skills")

    plt.ylabel("Number of Job Postings")

    plt.xticks(rotation=45)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig(
        "dashboard/top_skills.png",
        dpi=300
    )

    plt.close()

    print("Top Skills Chart Saved")


# ==========================================================
# JOBS BY LOCATION
# ==========================================================

def plot_jobs_by_location(df):

    data = (
        df["Location"]
        .value_counts()
    )

    plt.figure(figsize=(10,6))

    data.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Jobs by Location")

    plt.xlabel("Location")

    plt.ylabel("Number of Jobs")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig(
        "dashboard/jobs_by_location.png",
        dpi=300
    )

    plt.close()

    print("Jobs by Location Chart Saved")


# ==========================================================
# JOBS BY COMPANY
# ==========================================================

def plot_jobs_by_company(df):

    data = (
        df["Company"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(12,6))

    data.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Top Hiring Companies")

    plt.xlabel("Company")

    plt.ylabel("Number of Jobs")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig(
        "dashboard/jobs_by_company.png",
        dpi=300
    )

    plt.close()

    print("Top Companies Chart Saved")


# ==========================================================
# AVERAGE SALARY BY ROLE
# ==========================================================

def plot_salary_by_role(df):

    data = (
        df.groupby("Role")["Salary_LPA"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(12,6))

    data.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Average Salary by Role")

    plt.xlabel("Role")

    plt.ylabel("Salary (LPA)")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig(
        "dashboard/salary_by_role.png",
        dpi=300
    )

    plt.close()

    print("Salary by Role Chart Saved")


# ==========================================================
# EXPERIENCE DISTRIBUTION
# ==========================================================

def plot_experience_distribution(df):

    data = (
        df["Experience"]
        .value_counts()
    )

    plt.figure(figsize=(10,6))

    data.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Experience Distribution")

    plt.xlabel("Experience")

    plt.ylabel("Jobs")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig(
        "dashboard/experience_distribution.png",
        dpi=300
    )

    plt.close()

    print("Experience Distribution Chart Saved")


# ==========================================================
# SALARY DISTRIBUTION
# ==========================================================

def plot_salary_distribution(df):

    plt.figure(figsize=(10,6))

    plt.hist(
        df["Salary_LPA"],
        bins=10,
        edgecolor="black"
    )

    plt.title("Salary Distribution")

    plt.xlabel("Salary (LPA)")

    plt.ylabel("Frequency")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig(
        "dashboard/salary_distribution.png",
        dpi=300
    )

    plt.close()

    print("Salary Distribution Chart Saved")


# ==========================================================
# PIE CHART OF JOB LOCATIONS
# ==========================================================

def plot_location_pie(df):

    data = (
        df["Location"]
        .value_counts()
    )

    plt.figure(figsize=(8,8))

    plt.pie(
        data,
        labels=data.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Job Distribution by Location")

    plt.tight_layout()

    plt.savefig(
        "dashboard/location_pie.png",
        dpi=300
    )

    plt.close()

    print("Location Pie Chart Saved")


# ==========================================================
# GENERATE ALL CHARTS
# ==========================================================

def generate_dashboard(df, skill_counter):

    print("\nGenerating Dashboard...\n")

    plot_top_skills(skill_counter)

    plot_jobs_by_location(df)

    plot_jobs_by_company(df)

    plot_salary_by_role(df)

    plot_experience_distribution(df)

    plot_salary_distribution(df)

    plot_location_pie(df)

    print("\nDashboard Created Successfully")