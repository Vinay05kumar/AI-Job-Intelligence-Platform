from .skills import SKILLS


def extract_skills(text):

    found = []

    text = text.lower()

    for skill in SKILLS:

        if skill in text:

            found.append(skill)

    return found


def matched_skills(resume, jd):

    resume_skills = set(extract_skills(resume))

    jd_skills = set(extract_skills(jd))

    return sorted(resume_skills & jd_skills)


def missing_skills(resume, jd):

    resume_skills = set(extract_skills(resume))

    jd_skills = set(extract_skills(jd))

    return sorted(jd_skills - resume_skills)


def resume_suggestions(resume, jd):

    missing = missing_skills(resume, jd)

    suggestions = []

    for skill in missing:

        suggestions.append(
            f"Add projects or experience related to {skill.title()}."
        )

    return suggestions