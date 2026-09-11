from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Read resume
with open("data/resume.txt", "r", encoding="utf-8") as file:
    resume = file.read()


# Read job description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


# Convert text into embeddings
resume_embedding = model.encode([resume])
job_embedding = model.encode([job_description])


# Calculate semantic similarity
similarity = cosine_similarity(
    resume_embedding,
    job_embedding
)


score = similarity[0][0] * 100


print("================================")
print("    SEMANTIC RESUME MATCHER")
print("================================")

print(f"\n🧠 Semantic Match: {score:.2f}%")