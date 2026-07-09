"""
dashboard_data.py

Dashboard Data Preparation
AI Job Intelligence Platform
"""

import os
import pandas as pd

from app.database import execute_query

# ==========================================================
# CREATE PROCESSED DATA FOLDER
# ==========================================================

os.makedirs("data/processed", exist_ok=True)


# ==========================================================
# JOBS BY LOCATION
# ==========================================================

def jobs_by_location(connection):

    query = """
    SELECT
        location,
        COUNT(*) AS total_jobs
    FROM jobs
    GROUP BY location
    ORDER BY total_jobs DESC;
    """

    results = execute_query(connection, query)

    df = pd.DataFrame(
        results,
        columns=[
            "Location",
            "Total Jobs"
        ]
    )

    df.to_csv(
        "data/processed/jobs_by_location.csv",
        index=False
    )

    return df


# ==========================================================
# AVERAGE SALARY BY ROLE
# ==========================================================

def salary_by_role(connection):

    query = """
    SELECT
        role,
        ROUND(AVG(salary),2) AS average_salary
    FROM jobs
    GROUP BY role
    ORDER BY average_salary DESC;
    """

    results = execute_query(connection, query)

    df = pd.DataFrame(
        results,
        columns=[
            "Role",
            "Average Salary (LPA)"
        ]
    )

    df.to_csv(
        "data/processed/salary_by_role.csv",
        index=False
    )

    return df


# ==========================================================
# TOP COMPANIES
# ==========================================================

def top_companies(connection):

    query = """
    SELECT
        company,
        COUNT(*) AS total_jobs
    FROM jobs
    GROUP BY company
    ORDER BY total_jobs DESC;
    """

    results = execute_query(connection, query)

    df = pd.DataFrame(
        results,
        columns=[
            "Company",
            "Jobs Posted"
        ]
    )

    df.to_csv(
        "data/processed/top_companies.csv",
        index=False
    )

    return df


# ==========================================================
# AVERAGE SALARY BY LOCATION
# ==========================================================

def salary_by_location(connection):

    query = """
    SELECT
        location,
        ROUND(AVG(salary),2) AS average_salary
    FROM jobs
    GROUP BY location
    ORDER BY average_salary DESC;
    """

    results = execute_query(connection, query)

    df = pd.DataFrame(
        results,
        columns=[
            "Location",
            "Average Salary (LPA)"
        ]
    )

    df.to_csv(
        "data/processed/salary_by_location.csv",
        index=False
    )

    return df


# ==========================================================
# JOBS BY ROLE
# ==========================================================

def jobs_by_role(connection):

    query = """
    SELECT
        role,
        COUNT(*) AS total_jobs
    FROM jobs
    GROUP BY role
    ORDER BY total_jobs DESC;
    """

    results = execute_query(connection, query)

    df = pd.DataFrame(
        results,
        columns=[
            "Role",
            "Total Jobs"
        ]
    )

    df.to_csv(
        "data/processed/jobs_by_role.csv",
        index=False
    )

    return df


# ==========================================================
# EXPERIENCE DISTRIBUTION
# ==========================================================

def experience_distribution(connection):

    query = """
    SELECT
        experience,
        COUNT(*) AS total_jobs
    FROM jobs
    GROUP BY experience
    ORDER BY experience;
    """

    results = execute_query(connection, query)

    df = pd.DataFrame(
        results,
        columns=[
            "Experience",
            "Total Jobs"
        ]
    )

    df.to_csv(
        "data/processed/experience_distribution.csv",
        index=False
    )

    return df


# ==========================================================
# TOP PAYING JOBS
# ==========================================================

def top_paying_jobs(connection):

    query = """
    SELECT
        company,
        role,
        location,
        salary
    FROM jobs
    ORDER BY salary DESC
    LIMIT 20;
    """

    results = execute_query(connection, query)

    df = pd.DataFrame(
        results,
        columns=[
            "Company",
            "Role",
            "Location",
            "Salary (LPA)"
        ]
    )

    df.to_csv(
        "data/processed/top_paying_jobs.csv",
        index=False
    )

    return df


# ==========================================================
# DASHBOARD SUMMARY
# ==========================================================

def dashboard_summary(connection):

    print("\n")
    print("=" * 70)
    print("GENERATING DASHBOARD FILES")
    print("=" * 70)

    jobs_by_location(connection)
    salary_by_role(connection)
    salary_by_location(connection)
    jobs_by_role(connection)
    experience_distribution(connection)
    top_companies(connection)
    top_paying_jobs(connection)

    print("\nAll dashboard CSV files created successfully.")