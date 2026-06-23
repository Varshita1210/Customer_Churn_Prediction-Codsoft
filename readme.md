# Bank Customer Churn Prediction

## Overview

This project predicts whether a bank customer is likely to leave the bank (churn) or stay based on customer demographics and banking behavior.

The model is trained using Machine Learning techniques on the Bank Customer Churn Dataset and deployed using Flask.

---

## Problem Statement

Customer churn is one of the major challenges faced by banks and subscription-based businesses. Identifying customers who are likely to leave helps organizations take preventive actions and improve customer retention.

This project develops a predictive model that classifies customers into:

* Customer Likely To Stay
* Customer Likely To Leave

---

## Dataset

Dataset: Bank Customer Churn Prediction Dataset

Features:

* CreditScore
* Geography
* Gender
* Age
* Tenure
* Balance
* NumOfProducts
* HasCrCard
* IsActiveMember
* EstimatedSalary

Target Variable:

* Exited

  * 0 = Customer Stays
  * 1 = Customer Leaves

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Flask
* Joblib
* HTML
* CSS

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Model Deployment using Flask

---

## Data Preprocessing

### Removed Columns

The following columns were removed because they do not contribute to churn prediction:

* RowNumber
* CustomerId
* Surname

### Encoding

Gender:

* Female → 0
* Male → 1

Geography:

* Geography_Germany
* Geography_Spain

### Feature Scaling

StandardScaler was used to normalize numerical features.

---

## Models Used

### Logistic Regression

Accuracy: 81.10%

### Random Forest Classifier

Accuracy: 86.65%

Random Forest performed better and was selected as the final model.

---

## Model Performance

### Logistic Regression

Accuracy: 81.10%

### Random Forest

Accuracy: 86.65%

Selected Model: Random Forest Classifier

---

## Flask Web Application

The Flask application allows users to enter customer details and predict whether the customer is likely to churn.

### Input Fields

* Credit Score
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card Status
* Active Member Status
* Estimated Salary
* Geography

### Output

* Customer Likely To Stay
* Customer Likely To Leave

---

## Project Structure

Customer_Churn_Prediction/

├── apps/

│   ├── app.py

│   ├── templates/

│   │   └── index.html

│   └── static/

│       └── style.css

├── dataset/

│   └── Churn_Modelling.csv

├── models/

│   ├── churn_model.pkl

│   └── scaler.pkl

├── notebooks/

│   └── churn_prediction.ipynb

├── requirements.txt

└── README.md

---

## Screenshots to Add

### Screenshot 1 – Dataset Preview

Add screenshot of:

df.head()

Image:

screenshots/dataset_preview.png

---

### Screenshot 2 – Churn Distribution

Add screenshot of churn distribution graph.

Image:

screenshots/churn_distribution.png

---

### Screenshot 3 – Logistic Regression Results

Add screenshot of:

* Accuracy
* Confusion Matrix
* Classification Report

Image:

screenshots/logistic_regression_results.png

---

### Screenshot 4 – Random Forest Results

Add screenshot of:

* Accuracy
* Classification Report

Image:

screenshots/random_forest_results.png

---

### Screenshot 5 –Prediction Result

Add screenshot showing:

Customer Likely To stay
or 
Customer Likely To leave

Image:

screenshots/prediction_result.png

---


## Future Improvements

* XGBoost Implementation
* Hyperparameter Tuning
* Improved UI Design
* Customer Retention Recommendation System
* Cloud Deployment

---

## Author

Varshita Pallapothu

B.Tech CSE (AI & ML)

Mahatma Gandhi Institute of Technology (MGIT)
