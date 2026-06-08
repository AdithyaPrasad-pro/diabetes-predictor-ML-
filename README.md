# Diabetes Predictor

## About

I built this project to learn how Machine Learning can be used to predict whether a person is likely to have diabetes based on medical information.

Instead of using only one algorithm, I experimented with both a Decision Tree and a Random Forest model to compare their performance on the same dataset. This helped me understand how different Machine Learning algorithms can produce different results even when trained on the same data.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Decision Tree Classifier
* Random Forest Classifier

---

## Features

* Loads a real-world diabetes dataset from a CSV file
* Uses medical measurements as input features
* Splits the data into training and testing sets
* Trains and evaluates Machine Learning models
* Compares Decision Tree and Random Forest performance
* Allows interactive prediction using user input

---

## Dataset Features

Input Features:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

Target:

* Outcome

  * 1 = Diabetic
  * 0 = Not Diabetic

---

## Machine Learning Workflow

```text
Diabetes Dataset
        ↓
Load CSV
        ↓
Create X and y
        ↓
Train-Test Split
        ↓
Train Model
        ↓
Evaluate Accuracy
        ↓
Interactive Prediction
```

---

## Model Comparison

One of the main goals of this project was to compare two different classification algorithms.

### Decision Tree

Accuracy:

```text
81.82%
```

A Decision Tree makes predictions using a single tree structure.

### Random Forest

Accuracy:

```text
88.31%
```

A Random Forest combines the predictions of multiple decision trees and uses voting to make the final decision.

### Observation

The Random Forest model achieved a higher accuracy than the Decision Tree model on the same dataset.

This experiment helped me understand why Random Forest is often preferred for classification problems, as it can reduce mistakes made by a single decision tree.

---

## What I Learned

While building this project, I learned:

* How to work with medical datasets
* How to identify features (X) and targets (y)
* How train-test splitting works
* How Decision Trees make predictions
* How Random Forest uses multiple trees to improve performance
* How to compare Machine Learning algorithms
* How to evaluate models using accuracy
* How to build interactive prediction systems

---

## How to Run

Install the required libraries:

```bash
pip install pandas scikit-learn
```

Run the program:

```bash
python main.py
```

Enter the patient's medical details when prompted, and the model will predict whether the person is likely to have diabetes.

---

## Future Improvements

* Test additional classification algorithms such as KNN and SVM
* Compare multiple evaluation metrics
* Visualize feature importance
* Build a simple web application
* Use larger healthcare datasets


##Author
-Adithya Prasad
