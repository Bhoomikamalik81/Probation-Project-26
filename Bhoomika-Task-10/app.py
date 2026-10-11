from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

folder_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(folder_path, "best_model.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    workclass = request.form["workclass"]
    fnlwgt = float(request.form["fnlwgt"])
    education = request.form["education"]
    education_num = int(request.form["education_num"])
    marital_status = request.form["marital_status"]
    occupation = request.form["occupation"]
    relationship = request.form["relationship"]
    race = request.form["race"]
    sex = request.form["sex"]
    capital_gain = float(request.form["capital_gain"])
    capital_loss = float(request.form["capital_loss"])
    hours_per_week = float(request.form["hours_per_week"])
    native_country = request.form["native_country"]
    input_data = pd.DataFrame({
        "age": [age],
        "workclass": [workclass],
        "fnlwgt": [fnlwgt],
        "education": [education],
        "education.num": [education_num],
        "marital.status": [marital_status],
        "occupation": [occupation],
        "relationship": [relationship],
        "race": [race],
        "sex": [sex],
        "capital.gain": [capital_gain],
        "capital.loss": [capital_loss],
        "hours.per.week": [hours_per_week],
        "native.country": [native_country]
    })
    prediction = model.predict(input_data)[0]
    return render_template("index.html", prediction=prediction)
if __name__ == "__main__":
    app.run(debug=True)
