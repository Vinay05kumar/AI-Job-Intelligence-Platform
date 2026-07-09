import joblib

from models.salary_model import predict_salary


class SalaryService:

    def __init__(self):

        self.model = joblib.load("models/model.pkl")

        self.company_encoder = joblib.load(
            "models/company_encoder.pkl"
        )

        self.role_encoder = joblib.load(
            "models/role_encoder.pkl"
        )

        self.location_encoder = joblib.load(
            "models/location_encoder.pkl"
        )

        self.experience_encoder = joblib.load(
            "models/experience_encoder.pkl"
        )

    def predict(

        self,

        company,

        role,

        location,

        experience

    ):

        return predict_salary(

            self.model,

            self.company_encoder,

            self.role_encoder,

            self.location_encoder,

            self.experience_encoder,

            company,

            role,

            location,

            experience

        )