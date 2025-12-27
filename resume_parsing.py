import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

resume_text = """
3 years experience in Python, SQL, Machine Learning.
Worked on data analysis and predictive models.
"""
nltk.download('punkt_tab')

tokens = word_tokenize(resume_text.lower())

#remove stopwords
stop_words = set(stopwords.words('english'))
clean_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
print(clean_tokens)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform([resume_text])

#shows a numerical matrix
print(X.toarray())
#get_feature_names_out() → shows words used as features
print(vectorizer.get_feature_names_out())

SKILLS = [
    "python", "sql", "machine learning", "data analysis",
    "deep learning", "power bi", "tableau",
    "statistics", "excel", "nlp"
]

def extract_skills(clean_tokens, skill_list):
    #Empty list to store matched skills
    extracted_skills = []

    for skill in skill_list:
        #Handles multi-word skills like "machine learning"
        skill_words = skill.split()

        #Checks if all words of a skill exist in resume
        if all(word in clean_tokens for word in skill_words):
            #adds matched skill
            extracted_skills.append(skill)

    return extracted_skills

skills_found = extract_skills(clean_tokens, SKILLS)
print(skills_found)

import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iamvegeta@2110",
    database="smart_hiring"
)
#Cursor allows executing SQL queries
cursor = conn.cursor()
resume_id = 1  # assume resume ID

for skill in skills_found:
    cursor.execute(
        "INSERT INTO resume_skills (resume_id, skill_name) VALUES (%s, %s)",
        (resume_id, skill)
    )

conn.commit()

#Resume Scoring Logic
#Resume scoring=(Matched skills/Required skills) *100

def calculate_resume_score(candidate_skills, job_skills):
    #intersection means finding common skills
    matched = set(candidate_skills).intersection(set(job_skills))
    score = (len(matched) / len(job_skills)) * 100
    #round means rounding off the score
    return round(score, 2)

job_required_skills = ["python", "sql", "machine learning", "statistics"]

score = calculate_resume_score(skills_found, job_required_skills)
print("Resume Score:", score)

job_text = """
Looking for a Data Scientist with strong Python, SQL,
Machine Learning and Statistics skills.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')

#cleaning the resume and job
resume_clean = " ".join(clean_tokens)
job_clean = "python sql machine learning statistics"

#fit → learns vocabulary
#transform → converts text
tfidf_matrix = vectorizer.fit_transform([resume_clean, job_clean])
print(tfidf_matrix.toarray())

#cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

#tfidf_matrix[0:1] → resume vector
#tfidf_matrix[1:2] → job vector
#Output = similarity between 0 and 1
similarity_score = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
)

match_percentage = similarity_score[0][0] * 100
print("Match Score:", round(match_percentage, 2))

#For multiple job resumes
resumes = [
    "Python SQL Machine Learning Data Analysis",
    "Java Spring Boot Microservices",
    "Python SQL Statistics Machine Learning"
]

job_desc = "Looking for Python SQL Machine Learning professional"
tfidf = vectorizer.fit_transform(resumes + [job_desc])
scores = cosine_similarity(
    tfidf[:-1],
    tfidf[-1:]
)

#Ranking candidates
ranking = sorted(
    enumerate(scores),
    key=lambda x: x[1],
    reverse=True
)

for idx, score in ranking:
    print(f"Candidate {idx+1} Score: {round(score[0]*100, 2)}")

