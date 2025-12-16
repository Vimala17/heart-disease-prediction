# ❤️ Heart Disease Prediction Web App

A **Flask-based Machine Learning web application** that predicts whether a person has **heart disease** based on medical input parameters. This project is built with a clean UI using **HTML, CSS**, and a trained ML model in **Python**.

---

## Features

*  User Login & Logout system
*  Input medical details via form
*  Machine Learning based prediction
*  Displays result: *Heart Disease Detected / No Heart Disease*

---

## Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Machine Learning:** Scikit-learn, NumPy, Pandas
* **Model Type:** Logistic Regression
* **Tools:** Git, GitHub

---

## Project Structure

```
heart-disease-prediction/
│
├── static/
│   ├── style.css
│   └── heart.png
│
├── templates/
│   ├── login.html
│   ├── predict.html
│   ├── result.html
│   └── logout.html
│
├── app.py
├── heart_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/Vimala17/heart-disease-prediction.git
cd heart-disease-prediction
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000/
```

---

## How It Works

1. User logs in
2. Enters health details (age, BP, cholesterol, etc.)
3. Data is scaled and sent to ML model
4. Model predicts heart disease risk
5. Result is displayed on UI

---



## Author

**Vanaparthi Vimala**
B.Tech CSE (AI) Student
GitHub: [https://github.com/Vimala17](https://github.com/Vimala17)

---

