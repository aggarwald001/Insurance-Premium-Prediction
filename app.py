from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
with open('serialized.pkl', 'rb') as f:
    data = pickle.load(f)



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # age
        age = int(request.form["age"])

        #bmi
        bmi = request.form["bmi"]

        #children
        children = int(request.form["children"])

        #smoker
        smoker = request.form["smoker"]

        #expenses
        expenses = request.form["expenses"]

        # sex
        sex = request.form["sex"]
        if (sex == 'Male'):
            male = 1
            female = 0
        elif (sex == 'Female'):
            male = 0
            female = 1

        # smoker
        smoker = request.form["smoker"]
        if (smoker == 'Yes'):
            yes = 1
            no = 0
        elif (smoker == 'No'):
            yes = 0
            no = 1

        # region
        region = request.form["region"]
        if (region == 'Southwest'):
            southwest = 1
            southeast = 0
            northwest = 0
            northeast = 0
        elif (region == 'Southeast'):
            southwest = 0
            southeast = 1
            northwest = 0
            northeast = 0
        elif (region == 'Northwest'):
            southwest = 0
            southeast = 0
            northwest = 1
            northeast = 0
        elif (region == 'Northeast'):
            southwest = 0
            southeast = 0
            northwest = 0
            northeast = 1









        prediction=model.predict([[
            age,
            sex,
            bmi,
            children,
            smoker,
            region,
            expenses
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Insurance Premium is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
