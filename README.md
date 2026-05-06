# 🌲 Forest Fire Prediction Web Application

## 📌 Overview

This project is a Machine Learning-based web application that predicts the **Fire Weather Index (FWI)**, which indicates the potential severity of forest fires. The system helps estimate fire risk based on environmental and weather conditions.

## 🎯 Objective

To develop an intelligent system that analyzes weather parameters and predicts forest fire risk, helping in early prevention and decision-making.

## 🚀 Features

* Predicts Fire Weather Index (FWI) using ML model
* User-friendly web interface built with Flask
* Real-time prediction based on user input
* Displays fire risk level (Low / Medium / High)

## 📊 Input Features

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* FFMC (Fine Fuel Moisture Code)
* DMC (Duff Moisture Code)
* ISI (Initial Spread Index)
* Classes
* Region

## ⚙️ Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy

## 🧠 Machine Learning Model

* **Ridge Regression** algorithm used for prediction
* Data preprocessing performed using **StandardScaler**
* Model trained and evaluated using train-test split

## 🖥️ System Workflow

1. User inputs environmental parameters
2. Data is preprocessed using trained scaler
3. Model predicts Fire Weather Index
4. Result is displayed with risk level

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python application.py
```

## 📌 Future Enhancements

* Integration with real-time weather APIs
* Advanced models (Random Forest, XGBoost)
* Deployment on cloud platforms
* Mobile-friendly UI


