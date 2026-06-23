from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(current_dir, "..", "models", "churn_model.pkl")
scaler_path = os.path.join(current_dir, "..", "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = [
        float(request.form["CreditScore"]),
        int(request.form["Gender"]),
        int(request.form["Age"]),
        int(request.form["Tenure"]),
        float(request.form["Balance"]),
        int(request.form["NumOfProducts"]),
        int(request.form["HasCrCard"]),
        int(request.form["IsActiveMember"]),
        float(request.form["EstimatedSalary"]),
        int(request.form["Geography_Germany"]),
        int(request.form["Geography_Spain"])
    ]

    features = np.array([data])

    features = scaler.transform(features)

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Customer Likely To Leave"
    else:
        result = "Customer Likely To Stay"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)