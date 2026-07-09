import pandas as pd


def load_dashboard():

    df = pd.read_csv("data/raw/jobs.csv")

    return {

        "jobs": len(df),

        "companies": df["Company"].nunique(),

        "locations": df["Location"].nunique(),

        "skills": len(

            set(

                ",".join(df["Skills"]).split(",")

            )

        )

    }