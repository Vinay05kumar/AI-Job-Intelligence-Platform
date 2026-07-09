from app.load_data import load_dataset

from app.database import (
    create_connection,
    create_jobs_table,
    clear_jobs_table,
    insert_jobs,
    execute_query
)

from app.analysis import (
    dataset_info,
    dataset_statistics,
    company_counts,
    average_salary_company,
    role_counts,
    average_salary_role,
    location_counts,
    average_salary_location,
    get_top_paying_jobs,
    get_average_salary,
    get_jobs_by_location
)

from app.skill_analysis import get_skill_frequency
from app.visualization import plot_top_skills

from app.dashboard_data import (
    jobs_by_location,
    salary_by_role,
    top_companies
)

from models.salary_model import (
    train_salary_model,
    predict_salary
)

from app.ats_matcher import (
    extract_resume_text,
    calculate_ats_score,
    missing_skills
)
from app.load_data import (
    load_dataset,
    preview_dataset,
    dataset_shape,
    column_names,
    missing_values,
    duplicate_rows,
    data_types,
    save_dataset,
    remove_duplicates
)

from models.salary_model import (
    train_salary_model,
    predict_salary,
    save_model,
    load_model,
    feature_importance
)

# ==========================================================
# STEP 1 : CONNECT DATABASE
# ==========================================================

print("=" * 70)
print("CONNECTING DATABASE")
print("=" * 70)

connection = create_connection()
print("Database Connected Successfully")


# ==========================================================
# STEP 2 : CREATE TABLE
# ==========================================================

print("\nCreating Jobs Table...")

create_jobs_table(connection)

print("Jobs Table Ready")


# ==========================================================
# STEP 3 : LOAD DATASET
# ==========================================================

print("\nLoading Dataset...")

df = load_dataset("data/raw/jobs.csv")

preview_dataset(df)

dataset_shape(df)

column_names(df)

missing_values(df)

duplicate_rows(df)

data_types(df)
print("Dataset Loaded Successfully")


# ==========================================================
# STEP 4 : CLEAR OLD DATA
# ==========================================================

clear_jobs_table(connection)

print("Old Records Deleted")


# ==========================================================
# STEP 5 : INSERT DATA
# ==========================================================

insert_jobs(connection, df)

print("All Jobs Inserted Successfully")


# ==========================================================
# STEP 6 : SQL QUERY EXAMPLES
# ==========================================================

print("\n")
print("=" * 70)
print("TOP 5 HIGHEST PAYING JOBS (SQL)")
print("=" * 70)

query = """
SELECT company, role, salary
FROM jobs
ORDER BY salary DESC
LIMIT 5;
"""

results = execute_query(connection, query)

for row in results:
    print(row)


# ==========================================================
# STEP 7 : DATABASE ANALYSIS
# ==========================================================

print("\n")
print("=" * 70)
print("DATABASE ANALYSIS")
print("=" * 70)

print("\nTop Paying Jobs")

jobs = get_top_paying_jobs(connection)

for job in jobs:
    print(job)

print("\nAverage Salary")

avg = get_average_salary(connection)

print(f"{avg:.2f} LPA")

print("\nJobs by Location")

locations = get_jobs_by_location(connection)

for row in locations:
    print(row)


# ==========================================================
# STEP 8 : DATASET INFORMATION
# ==========================================================

print("\n")
print("=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

dataset_info(df)

dataset_statistics(df)


# ==========================================================
# STEP 9 : COMPANY ANALYSIS
# ==========================================================

print("\n")
print("=" * 70)
print("COMPANY ANALYSIS")
print("=" * 70)

company_counts(df)

average_salary_company(df)


# ==========================================================
# STEP 10 : ROLE ANALYSIS
# ==========================================================

print("\n")
print("=" * 70)
print("ROLE ANALYSIS")
print("=" * 70)

role_counts(df)

average_salary_role(df)


# ==========================================================
# STEP 11 : LOCATION ANALYSIS
# ==========================================================

print("\n")
print("=" * 70)
print("LOCATION ANALYSIS")
print("=" * 70)

location_counts(df)

average_salary_location(df)


# ==========================================================
# STEP 12 : SKILL ANALYSIS
# ==========================================================

print("\n")
print("=" * 70)
print("TOP SKILLS")
print("=" * 70)

skills = get_skill_frequency(connection)

for skill, count in skills.most_common(10):
    print(f"{skill:<20} {count}")


# ==========================================================
# STEP 13 : VISUALIZATION
# ==========================================================

print("\nGenerating Chart...")

plot_top_skills(skills)

print("Chart Saved Successfully")


# ==========================================================
# STEP 14 : DASHBOARD DATA
# ==========================================================

print("\n")
print("=" * 70)
print("DASHBOARD DATA")
print("=" * 70)

print("\nJobs by Location")

location_df = jobs_by_location(connection)

print(location_df)

print("\nAverage Salary by Role")

role_df = salary_by_role(connection)

print(role_df)

print("\nTop Companies")

company_df = top_companies(connection)

print(company_df)


# ==========================================================
# STEP 15 : SALARY PREDICTION
# ==========================================================

print("\n")
print("=" * 70)
print("SALARY PREDICTION")
print("=" * 70)

(
    model,
    company_encoder,
    role_encoder,
    location_encoder,
    experience_encoder
) = train_salary_model(df)

salary = predict_salary(
    model,
    company_encoder,
    role_encoder,
    location_encoder,
    experience_encoder,
    company="Google",
    role="Data Analyst",
    location="Bangalore",
    experience="0-2"
)

print(f"Predicted Salary : ₹ {salary:.2f} LPA")


# ==========================================================
# STEP 16 : ATS RESUME MATCHING
# ==========================================================

print("\n")
print("=" * 70)
print("ATS RESUME MATCHING")
print("=" * 70)

resume_path = "data/resume/VINAY KUMAR RESUME.pdf"

resume_text = extract_resume_text(resume_path)

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()

score = calculate_ats_score(
    resume_text,
    job_description
)

print(f"\nATS Score : {score:.2f}%")

missing = missing_skills(
    resume_text,
    job_description
)

print("\nMissing Skills")

if len(missing) == 0:

    print("No Missing Skills")

else:

    for i, skill in enumerate(missing, start=1):
        print(f"{i}. {skill.title()}")


# ==========================================================
# PROJECT COMPLETED
# ==========================================================

print("\n")
print("=" * 70)
print("AI JOB INTELLIGENCE PLATFORM EXECUTED SUCCESSFULLY")
print("=" * 70)

connection.close()

save_model(
    model,
    company_encoder,
    role_encoder,
    location_encoder,
    experience_encoder
)

feature_importance(model)