import sqlite3


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def create_connection():

    connection = sqlite3.connect("database/jobs.db")

    return connection


# ==========================================================
# CREATE TABLE
# ==========================================================

def create_jobs_table(connection):

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        company TEXT,

        role TEXT,

        location TEXT,

        salary REAL,

        experience TEXT,

        skills TEXT

    )
    """)

    connection.commit()


# ==========================================================
# DELETE OLD RECORDS
# ==========================================================

def clear_jobs_table(connection):

    cursor = connection.cursor()

    cursor.execute("DELETE FROM jobs")

    connection.commit()


# ==========================================================
# INSERT DATASET
# ==========================================================

def insert_jobs(connection, df):

    cursor = connection.cursor()

    for _, row in df.iterrows():

        cursor.execute("""

        INSERT INTO jobs(

            company,
            role,
            location,
            salary,
            experience,
            skills

        )

        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (

            row["Company"],
            row["Role"],
            row["Location"],
            row["Salary_LPA"],
            row["Experience"],
            row["Skills"]

        )

        )

    connection.commit()


# ==========================================================
# EXECUTE SELECT QUERY
# ==========================================================

def execute_query(connection, query):

    cursor = connection.cursor()

    cursor.execute(query)

    results = cursor.fetchall()

    return results


# ==========================================================
# GET COMPLETE TABLE
# ==========================================================

def fetch_all_jobs(connection):

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM jobs")

    return cursor.fetchall()


# ==========================================================
# TOTAL JOBS
# ==========================================================

def total_jobs(connection):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM jobs

    """)

    return cursor.fetchone()[0]


# ==========================================================
# AVERAGE SALARY
# ==========================================================

def average_salary(connection):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT AVG(salary)

    FROM jobs

    """)

    return cursor.fetchone()[0]


# ==========================================================
# MAX SALARY
# ==========================================================

def highest_salary(connection):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT MAX(salary)

    FROM jobs

    """)

    return cursor.fetchone()[0]


# ==========================================================
# MIN SALARY
# ==========================================================

def lowest_salary(connection):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT MIN(salary)

    FROM jobs

    """)

    return cursor.fetchone()[0]


# ==========================================================
# JOBS BY LOCATION
# ==========================================================

def jobs_by_location(connection):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT

        location,

        COUNT(*)

    FROM jobs

    GROUP BY location

    ORDER BY COUNT(*) DESC

    """)

    return cursor.fetchall()


# ==========================================================
# JOBS BY ROLE
# ==========================================================

def jobs_by_role(connection):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT

        role,

        COUNT(*)

    FROM jobs

    GROUP BY role

    ORDER BY COUNT(*) DESC

    """)

    return cursor.fetchall()


# ==========================================================
# AVERAGE SALARY BY ROLE
# ==========================================================

def salary_by_role(connection):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT

        role,

        ROUND(AVG(salary),2)

    FROM jobs

    GROUP BY role

    ORDER BY AVG(salary) DESC

    """)

    return cursor.fetchall()


# ==========================================================
# TOP PAYING COMPANIES
# ==========================================================

def top_companies(connection):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT

        company,

        ROUND(AVG(salary),2)

    FROM jobs

    GROUP BY company

    ORDER BY AVG(salary) DESC

    """)

    return cursor.fetchall()


# ==========================================================
# SEARCH COMPANY
# ==========================================================

def search_company(connection, company):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT *

    FROM jobs

    WHERE company = ?

    """,

    (company,)

    )

    return cursor.fetchall()


# ==========================================================
# SEARCH ROLE
# ==========================================================

def search_role(connection, role):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT *

    FROM jobs

    WHERE role = ?

    """,

    (role,)

    )

    return cursor.fetchall()


# ==========================================================
# SEARCH LOCATION
# ==========================================================

def search_location(connection, location):

    cursor = connection.cursor()

    cursor.execute("""

    SELECT *

    FROM jobs

    WHERE location = ?

    """,

    (location,)

    )

    return cursor.fetchall()


# ==========================================================
# CLOSE DATABASE
# ==========================================================

def close_connection(connection):

    connection.close()