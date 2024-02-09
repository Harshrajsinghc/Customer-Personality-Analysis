from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods =["GET","POST"])

def predict():
    if request.method == "POST":
        #Income
        Income = int(request.form["Income"])
        
        #Customer_days
        Customer_days = int(request.form["Customer_days"])

        #Total_Amount
        Total_Amount = int(request.form["Total_Amount"])

        #Total_Purchases
        Total_Purchases = int(request.form["Total_Purchases"])

        #Marital_Status
        Marital_Status = request.form["Marital_Status"]
        if(Marital_Status == "Single"):
            Marital_Status = 1.3508922

        else:
            Marital_Status = -0.74025151

        #Child
        Child = int(request.form["Child"])

        #Total_offer
        Total_offer = int(request.form["Total_offer"])
        
