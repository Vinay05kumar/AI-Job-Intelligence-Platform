"""
load_data.py

Loads the jobs dataset into a Pandas DataFrame.
"""

import os
import pandas as pd


# ==========================================================
# LOAD DATASET
# ==========================================================

def load_dataset(file_path):

    """
    Load CSV dataset.

    Parameters
    ----------
    file_path : str
        Path to CSV file

    Returns
    -------
    pandas.DataFrame
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"\nDataset not found:\n{file_path}"
        )

    try:

        df = pd.read_csv(file_path)

        print("Dataset Loaded Successfully")
        print(f"Total Rows    : {df.shape[0]}")
        print(f"Total Columns : {df.shape[1]}")

        return df

    except Exception as e:

        print("\nError while loading dataset")
        print(e)

        raise


# ==========================================================
# DISPLAY FIRST ROWS
# ==========================================================

def preview_dataset(df, rows=5):

    print("\n")
    print("=" * 60)
    print("DATASET PREVIEW")
    print("=" * 60)

    print(df.head(rows))


# ==========================================================
# DATASET SHAPE
# ==========================================================

def dataset_shape(df):

    print("\n")
    print("=" * 60)
    print("DATASET SHAPE")
    print("=" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")


# ==========================================================
# COLUMN NAMES
# ==========================================================

def column_names(df):

    print("\n")
    print("=" * 60)
    print("COLUMN NAMES")
    print("=" * 60)

    for column in df.columns:
        print(column)


# ==========================================================
# MISSING VALUES
# ==========================================================

def missing_values(df):

    print("\n")
    print("=" * 60)
    print("MISSING VALUES")
    print("=" * 60)

    print(df.isnull().sum())


# ==========================================================
# DUPLICATE ROWS
# ==========================================================

def duplicate_rows(df):

    print("\n")
    print("=" * 60)
    print("DUPLICATE ROWS")
    print("=" * 60)

    duplicates = df.duplicated().sum()

    print(f"Duplicate Rows : {duplicates}")


# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

def remove_duplicates(df):

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print("\nDuplicates Removed :", before - after)

    return df


# ==========================================================
# DATA TYPES
# ==========================================================

def data_types(df):

    print("\n")
    print("=" * 60)
    print("DATA TYPES")
    print("=" * 60)

    print(df.dtypes)


# ==========================================================
# SAVE PROCESSED DATASET
# ==========================================================

def save_dataset(df, output_path):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)

    print("\nProcessed Dataset Saved Successfully")
    print(output_path)