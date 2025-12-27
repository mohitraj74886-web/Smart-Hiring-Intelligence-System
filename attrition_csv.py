import pandas as pd
import random
employees = []

for emp_id in range(1, 31):  # 30 employees
    experience = random.randint(0, 12)
    salary = random.randint(20000, 120000)
    satisfaction = random.randint(1, 5)
    performance = random.randint(2, 5)

    # realistic attrition probability logic
    attrition_prob = round(
        (0.6 if satisfaction <= 2 else 0.2) +
        (0.2 if salary < 40000 else 0) +
        random.uniform(0, 0.2),
        2
    )

    employees.append({
        "Employee_ID": emp_id,
        "Experience_Years": experience,
        "Salary": salary,
        "Job_Satisfaction": satisfaction,
        "Performance_Rating": performance,
        "Attrition_Probability": min(attrition_prob, 0.95)
    })

df_attrition = pd.DataFrame(employees)
df_attrition.to_csv("attrition_predictions.csv", index=False)

print("attrition_predictions.csv created successfully")
