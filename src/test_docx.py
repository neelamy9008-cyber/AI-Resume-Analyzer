import sys

sys.path.append("src")

from docx_reader import extract_text_from_docx


text = extract_text_from_docx("data/resume.docx")


print("================================")
print("       EXTRACTED RESUME")
print("================================")

print(text)