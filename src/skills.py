# Skills our system knows about

SKILLS = [
    "python",
    "c++",
    "java",
    "javascript",
    "html",
    "css",
    "sql",
    "machine learning",
    "scikit-learn",
    "data analysis",
    "statistics",
    "git",
    "github",
    "react",
    "deep learning",
    "tensorflow",
    "pytorch",
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills