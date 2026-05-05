import pickle
from flask import Flask, request, jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

## import ridge regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        try:
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
            scaled_data = standard_scaler.transform(data)
            result = ridge_model.predict(scaled_data)[0]

            # Risk level
            if result < 5:
                level = "Low Risk"
            elif result < 15:
                level = "Moderate Risk"
            else:
                level = "High Risk"

            return render_template("home.html", results=round(result, 2), level=level)

        except:
            return render_template("home.html", error="Invalid Input!")

    return render_template("home.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")