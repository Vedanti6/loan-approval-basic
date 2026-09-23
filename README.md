# Loan Approval Prediction

## Project Overview

Loan Approval Prediction is a Machine Learning project that predicts whether a loan application is likely to be approved or not based on applicant and loan-related information.

The project uses two Machine Learning classification algorithms:

- Logistic Regression
- Decision Tree Classifier

The trained models are connected to a Flask web application where users can enter their details and receive loan approval predictions.

---

## Features

- Predicts loan approval status using Machine Learning
- Uses two different classification algorithms
- Compares Logistic Regression and Decision Tree predictions
- Interactive web interface
- Flask-based backend
- Real-time prediction through the web application
- Displays predictions from both algorithms

---

## Machine Learning Algorithms

### 1. Logistic Regression

Logistic Regression is a classification algorithm used to predict the probability of a binary outcome.

In this project:

- `1` = Loan Approved
- `0` = Loan Not Approved

### 2. Decision Tree Classifier

Decision Tree is a classification algorithm that makes predictions by creating a tree-like structure based on the input features.

Both algorithms are trained using the same dataset and their predictions are displayed in the web application.

---

## Dataset

The dataset contains information about loan applicants and their loan applications.

The features used in the project include:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

The target variable is:

- `Loan_Status`

Where:

- `Y` = Loan Approved
- `N` = Loan Not Approved

### Dataset Source

The dataset used in this project was obtained from the resources provided by the creator of the following YouTube tutorial:

**Source:** [Loan Approval Prediction – YouTube](https://youtu.be/x2NrPeHSPU0?si=TSMEY8jaj_xuaG3n)

The dataset was used for educational and machine learning project purposes.

---

## Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Logistic Regression
- Decision Tree Classifier

### Data Processing
- Pandas
- NumPy

### Backend
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Model Saving
- Joblib

---

## Project Structure

```text
Loan-Approval-Project/
│
├── app.py
├── loan_model.pkl
├── decision_tree_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── notebook/
│   └── Loan_Approval_Prediction.ipynb
│
├── dataset/
│   └── loan_prediction.csv
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
