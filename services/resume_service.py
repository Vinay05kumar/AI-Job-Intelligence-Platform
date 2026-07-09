import tempfile
from app.ats.parser import extract_resume_text


def save_uploaded_resume(uploaded_file):

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    temp.write(uploaded_file.read())
    temp.close()

    return temp.name


def read_resume(uploaded_file):

    path = save_uploaded_resume(uploaded_file)

    return extract_resume_text(path)