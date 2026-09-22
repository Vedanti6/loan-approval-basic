from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("loan_model.pkl")
scaler = joblib.load("scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    # Convert categorical values to numbers
    gender = 1 if data["Gender"] == "Male" else 0

    married = 1 if data["Married"] == "Yes" else 0

    dependents = data["Dependents"]

    if dependents == "3+":
        dependents = 3
    else:
        dependents = int(dependents)

    education = 0 if data["Education"] == "Graduate" else 1

    self_employed = 1 if data["Self_Employed"] == "Yes" else 0

    property_area = {
        "Rural": 0,
        "Semiurban": 1,
        "Urban": 2
    }

    property_value = property_area[data["Property_Area"]]

    # Create dataframe
    input_data = pd.DataFrame({
        "Gender": [gender],
        "Married": [married],
        "Dependents": [dependents],
        "Education": [education],
        "Self_Employed": [self_employed],
        "ApplicantIncome": [float(data["ApplicantIncome"])],
        "CoapplicantIncome": [float(data["CoapplicantIncome"])],
        "LoanAmount": [float(data["LoanAmount"])],
        "Loan_Amount_Term": [float(data["Loan_Amount_Term"])],
        "Credit_History": [float(data["Credit_History"])],
        "Property_Area": [property_value]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        result = "Loan Approved"
    else:
        result = "Loan Not Approved"

    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run(debug=True)