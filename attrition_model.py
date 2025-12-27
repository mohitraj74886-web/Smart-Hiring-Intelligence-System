import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="smart_hiring"
)
query = "SELECT * FROM employees"

#read_sql() → converts SQL table → pandas DataFrame
df = pd.read_sql(query, conn)
print(df)

#x=input features,y=target variable
X = df[['experience_years', 'salary', 'job_satisfaction', 'performance_rating']]
y = df['attrition']

#These  features directly influence employee satisfaction & retention.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LogisticRegression

#Logistic Regression → binary classification
#Outputs probability, not just yes/no
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
#predicts 0 and 1
y_pred = model.predict(X_test)
#predicts probability
y_prob = model.predict_proba(X_test)

#MODEL EVALUATION
from sklearn.metrics import accuracy_score, classification_report
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

#FEATURE IMPORTANCE
importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.coef_[0]
})

print(importance)

#This tells us
#Which factor increases attrition most
#Salary? Satisfaction? Experience?
