from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

from docx_reader import extract_text_from_docx
from skills import extract_skills
from recommendations import generate_recommendations

import sys
sys.path.append("src")


# -----------------------------
# 1. READ RESUME FROM DOCX
# -----------------------------

resume = extract_text_from_docx("data/resume.docx")


# -----------------------------
# 2. READ JOB DESCRIPTION
# -----------------------------

with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


# -----------------------------
# 3. TF-IDF SIMILARITY
# -----------------------------

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform([
    resume,
    job_description
])

tfidf_similarity = cosine_similarity(
    vectors[0],
    vectors[1]
)

tfidf_score = tfidf_similarity[0][0] * 100


# -----------------------------
# 4. SEMANTIC SIMILARITY
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

resume_embedding = model.encode([resume])
job_embedding = model.encode([job_description])

semantic_similarity = cosine_similarity(
    resume_embedding,
    job_embedding
)

semantic_score = semantic_similarity[0][0] * 100


# -----------------------------
# 5. SKILL MATCHING
# -----------------------------

resume_skills = extract_skills(resume)
job_skills = extract_skills(job_description)

matched_skills = []

for skill in job_skills:
    if skill in resume_skills:
        matched_skills.append(skill)


missing_skills = []

for skill in job_skills:
    if skill not in resume_skills:
        missing_skills.append(skill)


if len(job_skills) > 0:
    skill_score = (
        len(matched_skills) / len(job_skills)
    ) * 100
else:
    skill_score = 0


# -----------------------------
# 6. FINAL SCORE
# -----------------------------

final_score = (
    semantic_score * 0.40
    + skill_score * 0.30
    + tfidf_score * 0.30
)


# -----------------------------
# 7. RECOMMENDATIONS
# -----------------------------

recommendations = generate_recommendations(
    missing_skills
)


# -----------------------------
# 8. DISPLAY RESULTS
# -----------------------------

print("================================")
print("       AI RESUME ANALYZER")
print("================================")

print(f"\n📄 TF-IDF Score:      {tfidf_score:.2f}%")
print(f"🧠 Semantic Score:    {semantic_score:.2f}%")
print(f"🛠️ Skill Match:       {skill_score:.2f}%")

print("--------------------------------")
print(f"🎯 FINAL SCORE:       {final_score:.2f}%")
print("--------------------------------")


print("\n✅ MATCHED SKILLS:")

for skill in matched_skills:
    print("-", skill)


print("\n❌ MISSING SKILLS:")

for skill in missing_skills:
    print("-", skill)


print("\n💡 RECOMMENDATIONS:")

for recommendation in recommendations:
    print("-", recommendation)