"""
analysis.py

Exploratory Data Analysis (EDA)
Business Analysis
SQL Analysis
"""

import pandas as pd

from app.database import execute_query


# ==========================================================
# DATASET INFORMATION
# ==========================================================

def dataset_info(df):

    print("\n")
    print("=" * 70)
    print("DATASET INFORMATION")
    print("=" * 70)

    print(df.info())


# ==========================================================
# DATASET STATISTICS
# ==========================================================

def dataset_statistics(df):

    print("\n")
    print("=" * 70)
    print("DATASET STATISTICS")
    print("=" * 70)

    print(df.describe(include="all"))


# ==========================================================
# COMPANY COUNT
# ==========================================================

def company_counts(df):

    print("\n")
    print("=" * 70)
    print("JOBS BY COMPANY")
    print("=" * 70)

    print(df["Company"].value_counts())


# ==========================================================
# AVERAGE SALARY BY COMPANY
# ==========================================================

def average_salary_company(df):

    print("\n")
    print("=" * 70)
    print("AVERAGE SALARY BY COMPANY")
    print("=" * 70)

    result = (
        df.groupby("Company")["Salary_LPA"]
        .mean()
        .sort_values(ascending=False)
    )

    print(result)


# ==========================================================
# ROLE COUNT
# ==========================================================

def role_counts(df):

    print("\n")
    print("=" * 70)
    print("JOBS BY ROLE")
    print("=" * 70)

    print(df["Role"].value_counts())


# ==========================================================
# AVERAGE SALARY BY ROLE
# ==========================================================

def average_salary_role(df):

    print("\n")
    print("=" * 70)
    print("AVERAGE SALARY BY ROLE")
    print("=" * 70)

    result = (
        df.groupby("Role")["Salary_LPA"]
        .mean()
        .sort_values(ascending=False)
    )

    print(result)


# ==========================================================
# LOCATION COUNT
# ==========================================================

def location_counts(df):

    print("\n")
    print("=" * 70)
    print("JOBS BY LOCATION")
    print("=" * 70)

    print(df["Location"].value_counts())


# ==========================================================
# AVERAGE SALARY BY LOCATION
# ==========================================================

def average_salary_location(df):

    print("\n")
    print("=" * 70)
    print("AVERAGE SALARY BY LOCATION")
    print("=" * 70)

    result = (
        df.groupby("Location")["Salary_LPA"]
        .mean()
        .sort_values(ascending=False)
    )

    print(result)


# ==========================================================
# TOP PAYING JOBS (SQL)
# ==========================================================

def get_top_paying_jobs(connection):

    query = """
    SELECT
        company,
        role,
        location,
        salary
    FROM jobs
    ORDER BY salary DESC
    LIMIT 10;
    """

    return execute_query(connection, query)


# ==========================================================
# AVERAGE SALARY (SQL)
# ==========================================================

def get_average_salary(connection):

    query = """
    SELECT AVG(salary)
    FROM jobs;
    """

    result = execute_query(connection, query)

    return result[0][0]


# ==========================================================
# JOBS BY LOCATION (SQL)
# ==========================================================

def get_jobs_by_location(connection):

    query = """
    SELECT
        location,
        COUNT(*) AS total_jobs
    FROM jobs
    GROUP BY location
    ORDER BY total_jobs DESC;
    """

    return execute_query(connection, query)


# ==========================================================
# HIGHEST SALARY
# ==========================================================

def highest_salary(df):

    print("\n")
    print("=" * 70)
    print("HIGHEST SALARY")
    print("=" * 70)

    print(df["Salary_LPA"].max())


# ==========================================================
# LOWEST SALARY
# ==========================================================

def lowest_salary(df):

    print("\n")
    print("=" * 70)
    print("LOWEST SALARY")
    print("=" * 70)

    print(df["Salary_LPA"].min())


# ==========================================================
# AVERAGE SALARY
# ==========================================================

def average_salary(df):

    print("\n")
    print("=" * 70)
    print("AVERAGE SALARY")
    print("=" * 70)

    print(round(df["Salary_LPA"].mean(), 2))


# ==========================================================
# EXPERIENCE DISTRIBUTION
# ==========================================================

def experience_distribution(df):

    print("\n")
    print("=" * 70)
    print("EXPERIENCE DISTRIBUTION")
    print("=" * 70)

    print(df["Experience"].value_counts())


# ==========================================================
# TOP CITIES
# ==========================================================

def top_locations(df):

    print("\n")
    print("=" * 70)
    print("TOP HIRING CITIES")
    print("=" * 70)

    print(df["Location"].value_counts().head(10))


# ==========================================================
# TOP COMPANIES
# ==========================================================

def top_companies(df):

    print("\n")
    print("=" * 70)
    print("TOP HIRING COMPANIES")
    print("=" * 70)

    print(df["Company"].value_counts().head(10))


# ==========================================================
# DATASET SUMMARY
# ==========================================================

def dataset_summary(df):

    print("\n")
    print("=" * 70)
    print("DATASET SUMMARY")
    print("=" * 70)

    print(f"Total Jobs      : {len(df)}")
    print(f"Companies       : {df['Company'].nunique()}")
    print(f"Roles           : {df['Role'].nunique()}")
    print(f"Locations       : {df['Location'].nunique()}")
    print(f"Average Salary  : {round(df['Salary_LPA'].mean(),2)} LPA")