from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = "heart_secret_key"

model = pickle.load(open("heart_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Accept ANY username & password
        session["user"] = username
        return redirect(url_for("predict"))

    return render_template("login.html")



@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        data = [
            float(request.form["age"]),
            float(request.form["sex"]),
            float(request.form["cp"]),
            float(request.form["trestbps"]),
            float(request.form["chol"]),
            float(request.form["fbs"]),
            float(request.form["restecg"]),
            float(request.form["thalach"]),
            float(request.form["exang"]),
            float(request.form["oldpeak"]),
            float(request.form["slope"]),
            float(request.form["ca"]),
            float(request.form["thal"]),
        ]

        data = np.array(data).reshape(1, -1)
        data = scaler.transform(data)
        prediction = model.predict(data)[0]

        return render_template("result.html", prediction=prediction)

    return render_template("predict.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(debug=True)
