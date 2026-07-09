"""
skill_analysis.py

Skill Analysis Module
AI Job Intelligence Platform
"""

from collections import Counter

import pandas as pd

from app.database import execute_query


# ==========================================================
# GET SKILL FREQUENCY FROM DATABASE
# ==========================================================

def get_skill_frequency(connection):

    query = """
    SELECT skills
    FROM jobs;
    """

    results = execute_query(connection, query)

    all_skills = []

    for row in results:

        skills = row[0].split(",")

        for skill in skills:

            all_skills.append(skill.strip())

    counter = Counter(all_skills)

    return counter


# ==========================================================
# DISPLAY TOP SKILLS
# ==========================================================

def print_top_skills(counter, top_n=10):

    print("\n")
    print("=" * 70)
    print(f"TOP {top_n} SKILLS")
    print("=" * 70)

    for skill, count in counter.most_common(top_n):

        print(f"{skill:<25} {count}")


# ==========================================================
# SKILL DATAFRAME
# ==========================================================

def skills_dataframe(counter):

    df = pd.DataFrame(

        counter.items(),

        columns=[

            "Skill",

            "Frequency"

        ]

    )

    df = df.sort_values(

        by="Frequency",

        ascending=False

    )

    return df


# ==========================================================
# SAVE SKILLS CSV
# ==========================================================

def save_skills_csv(counter):

    df = skills_dataframe(counter)

    df.to_csv(

        "data/processed/top_skills.csv",

        index=False

    )

    print("\nTop Skills CSV Saved Successfully")


# ==========================================================
# SKILL PERCENTAGE
# ==========================================================

def skill_percentage(counter):

    total = sum(counter.values())

    percentage = {}

    for skill, count in counter.items():

        percentage[skill] = round(

            (count / total) * 100,

            2

        )

    return percentage


# ==========================================================
# PRINT SKILL PERCENTAGE
# ==========================================================

def print_skill_percentage(counter):

    print("\n")
    print("=" * 70)
    print("SKILL PERCENTAGE")
    print("=" * 70)

    percentage = skill_percentage(counter)

    percentage = sorted(

        percentage.items(),

        key=lambda x: x[1],

        reverse=True

    )

    for skill, value in percentage:

        print(f"{skill:<25} {value}%")


# ==========================================================
# SEARCH A SKILL
# ==========================================================

def search_skill(counter, skill_name):

    skill_name = skill_name.strip()

    if skill_name in counter:

        print(

            f"\n{skill_name} appears in "

            f"{counter[skill_name]} job postings."

        )

    else:

        print(

            f"\n{skill_name} not found."

        )


# ==========================================================
# TOP N SKILLS
# ==========================================================

def top_n_skills(counter, n=5):

    return counter.most_common(n)


# ==========================================================
# UNIQUE SKILLS
# ==========================================================

def total_unique_skills(counter):

    return len(counter)


# ==========================================================
# TOTAL SKILL OCCURRENCES
# ==========================================================

def total_skill_occurrences(counter):

    return sum(counter.values())


# ==========================================================
# EXPORT SKILL SUMMARY
# ==========================================================

def export_skill_summary(counter):

    df = skills_dataframe(counter)

    df["Percentage"] = (

        df["Frequency"]

        /

        df["Frequency"].sum()

    ) * 100

    df["Percentage"] = df["Percentage"].round(2)

    df.to_csv(

        "data/processed/skill_summary.csv",

        index=False

    )

    print("\nSkill Summary Exported Successfully")


# ==========================================================
# TOP SKILL
# ==========================================================

def most_demanded_skill(counter):

    return counter.most_common(1)[0]


# ==========================================================
# LEAST DEMANDED SKILL
# ==========================================================

def least_demanded_skill(counter):

    return counter.most_common()[-1]


# ==========================================================
# SKILL SUMMARY
# ==========================================================

def skill_summary(counter):

    print("\n")
    print("=" * 70)
    print("SKILL SUMMARY")
    print("=" * 70)

    print(

        "Total Unique Skills :",

        total_unique_skills(counter)

    )

    print(

        "Total Skill Occurrences :",

        total_skill_occurrences(counter)

    )

    top_skill = most_demanded_skill(counter)

    print(

        f"Most Demanded Skill : "

        f"{top_skill[0]} ({top_skill[1]})"

    )

    least_skill = least_demanded_skill(counter)

    print(

        f"Least Demanded Skill : "

        f"{least_skill[0]} ({least_skill[1]})"

    )