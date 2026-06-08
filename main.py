import pandas as pd
df = pd.read_csv("diabetes.csv")
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
x = df[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]]

y = df["Outcome"]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

pregnancies = int( input("Pregnancies: "))
glucose = int(input("Glucose: "))
blood_pressure = int(input("Blood Pressure:"))
skin_thickness = int(input("Skin Thickness: "))
insulin = int(input("Insulin: "))
bmi = float(input("BMI: "))
dpf = float(input("Diabetes Pedigree Function: "))
age = int(input("Age: "))

user_data = pd.DataFrame([{
    "Pregnancies": pregnancies,
    "Glucose": glucose,
    "BloodPressure": blood_pressure,
    "SkinThickness": skin_thickness,
    "Insulin": insulin,
    "BMI": bmi,
    "DiabetesPedigreeFunction": dpf,
    "Age": age
}])

prediction = model.predict(user_data)

if prediction[0]==1:
    print("\nPrediction: Diabetic")
else:
    print("\nPrediction: Not Diabetic")
