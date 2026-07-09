from app.load_data import load_dataset
from models.salary_model import train_salary_model

df = load_dataset("data/raw/jobs.csv")

train_salary_model(df)

print("\nModel Training Completed Successfully!")