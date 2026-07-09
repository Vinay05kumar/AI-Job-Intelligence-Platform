from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume, jd):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume, jd])

    score = cosine_similarity(vectors)[0][1]

    return round(score * 100, 2)