import pandas as pd
import random
candidates = [
    "Amit Sharma", "Neha Verma", "Rahul Mehta", "Pooja Singh",
    "Karan Patel", "Anjali Gupta", "Rohit Kumar", "Sneha Iyer",
    "Vikram Rao", "Nisha Malhotra"
]

skill_pool = [
    "Python", "SQL", "Machine Learning", "Data Analysis",
    "Statistics", "Power BI", "Excel", "NLP"
]

data = []

for name in candidates:
    skills = random.sample(skill_pool, random.randint(3, 6))
    match_score = random.randint(30, 90)

    data.append({
        "Candidate_Name": name,
        "Skills": ", ".join(skills),
        "Match_Score": match_score
    })

df = pd.DataFrame(data)
df.to_csv("resume_match_scores.csv", index=False)

print("resume_match_scores.csv created successfully")

