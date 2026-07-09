"""
salary_model.py

Salary Prediction Model
AI Job Intelligence Platform
"""

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.preprocessing import LabelEncoder


# ==========================================================
# TRAIN MODEL
# ==========================================================

def train_salary_model(df):

    data = df.copy()

    # Encode categorical columns
    company_encoder = LabelEncoder()
    role_encoder = LabelEncoder()
    location_encoder = LabelEncoder()
    experience_encoder = LabelEncoder()

    data["Company"] = company_encoder.fit_transform(data["Company"])
    data["Role"] = role_encoder.fit_transform(data["Role"])
    data["Location"] = location_encoder.fit_transform(data["Location"])
    data["Experience"] = experience_encoder.fit_transform(data["Experience"])

    # Features & Target
    X = data[
        [
            "Company",
            "Role",
            "Location",
            "Experience"
        ]
    ]

    y = data["Salary_LPA"]

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Train Model
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\n")
    print("=" * 70)
    print("SALARY MODEL PERFORMANCE")
    print("=" * 70)
    print(f"MAE       : {mean_absolute_error(y_test, predictions):.2f}")
    print(f"MSE       : {mean_squared_error(y_test, predictions):.2f}")
    print(f"R² Score  : {r2_score(y_test, predictions):.2f}")

    # Save model automatically
    save_model(
        model,
        company_encoder,
        role_encoder,
        location_encoder,
        experience_encoder
    )

    return (
        model,
        company_encoder,
        role_encoder,
        location_encoder,
        experience_encoder
    )


# ==========================================================
# PREDICT SALARY
# ==========================================================

def predict_salary(
    model,
    company_encoder,
    role_encoder,
    location_encoder,
    experience_encoder,
    company,
    role,
    location,
    experience
):

    company = company_encoder.transform([company])[0]
    role = role_encoder.transform([role])[0]
    location = location_encoder.transform([location])[0]
    experience = experience_encoder.transform([experience])[0]

    prediction = model.predict([[
        company,
        role,
        location,
        experience
    ]])

    return prediction[0]


# ==========================================================
# SAVE MODEL
# ==========================================================

def save_model(
    model,
    company_encoder,
    role_encoder,
    location_encoder,
    experience_encoder
):

    joblib.dump(model, "models/model.pkl")
    joblib.dump(company_encoder, "models/company_encoder.pkl")
    joblib.dump(role_encoder, "models/role_encoder.pkl")
    joblib.dump(location_encoder, "models/location_encoder.pkl")
    joblib.dump(experience_encoder, "models/experience_encoder.pkl")

    print("\nModel Saved Successfully!")


# ==========================================================
# LOAD MODEL
# ==========================================================

def load_model():

    model = joblib.load("models/model.pkl")

    company_encoder = joblib.load(
        "models/company_encoder.pkl"
    )

    role_encoder = joblib.load(
        "models/role_encoder.pkl"
    )

    location_encoder = joblib.load(
        "models/location_encoder.pkl"
    )

    experience_encoder = joblib.load(
        "models/experience_encoder.pkl"
    )

    return (
        model,
        company_encoder,
        role_encoder,
        location_encoder,
        experience_encoder
    )


# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

def feature_importance(model):

    features = [
        "Company",
        "Role",
        "Location",
        "Experience"
    ]

    importance = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    print("\n")
    print("=" * 70)
    print("FEATURE IMPORTANCE")
    print("=" * 70)
    print(importance)

    return importance