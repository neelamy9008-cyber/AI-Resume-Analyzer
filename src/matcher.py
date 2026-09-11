from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from skills import extract_skills


# Read resume
with open("data/resume.txt", "r", encoding="utf-8") as file:
    resume = file.read()


# Read job description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


# -----------------------------
# MATCH SCORE
# -----------------------------

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform([
    resume,
    job_description
])

similarity = cosine_similarity(vectors[0], vectors[1])

score = similarity[0][0] * 100


# -----------------------------
# SKILL ANALYSIS
# -----------------------------

resume_skills = extract_skills(resume)
job_skills = extract_skills(job_description)


# Skills present in both
matched_skills = []

for skill in job_skills:
    if skill in resume_skills:
        matched_skills.append(skill)


# Skills required by job but missing from resume
missing_skills = []

for skill in job_skills:
    if skill not in resume_skills:
        missing_skills.append(skill)


# -----------------------------
# DISPLAY RESULTS
# -----------------------------

print("================================")
print("       AI RESUME ANALYZER")
print("================================")

print(f"\n🎯 Match Score: {score:.2f}%")

print("\n✅ Matched Skills:")

for skill in matched_skills:
    print("-", skill)


print("\n❌ Missing Skills:")

for skill in missing_skills:
    print("-", skill)