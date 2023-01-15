import mysql.connector
from flask import Flask, render_template,request,url_for
import numpy as np
from joblib import dump,load


app = Flask(__name__)


# creating a decorate
# create a path of website
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/index')
def index():
    return render_template("index.html")
#id="check-male"

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")


@app.route('/heart')
def heart():
    return render_template("heart.html")


@app.route("/kidney")
def kidney():
    return render_template("kidney.html")



@app.route("/cancer")
def cancer():
    return render_template("cancer.html")

@app.route("/liver")
def liver():
    return render_template("liver.html")


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 6):
        loaded_model = load(
            r'.\models\diabetes_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 6):
        loaded_model = load(
            r'.\models\diabetes_model.pkl')
        result1 = loaded_model.predict(to_predict)
    return result1[0]


def ValuePredictorkidney(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 7):
        loaded_model = load(
            r'.\models\kidney_model.pkl')
        result2 = loaded_model.predict(to_predict)
    return result2[0]


def ValuePredictorliver(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 7):
        loaded_model = load(
            r'.\models\liver_model.pkl')
        result3 = loaded_model.predict(to_predict)
    return result3[0]


def ValuePredictorheart(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 7):
        loaded_model = load(
            r'.\models\heart_model.pkl')
        result4 = loaded_model.predict(to_predict)
    return result4[0]


def ValuePredictorcancer(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 5):
        loaded_model = load(
            r'.\models\cancer_model.pkl')
        result5 = loaded_model.predict(to_predict)
    return result5[0]




@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        # diabetes
        if len(to_predict_list) == 6:
              result = ValuePredictor(to_predict_list, 6)
        #kidney,heart=len(7)
        elif len(to_predict_list) == 7:
            result=ValuePredictorkidney(to_predict_list ,7)
        elif len(to_predict_list) == 7:
            result=ValuePredictorheart(to_predict_list,7)
        elif len(to_predict_list) == 7:
            result=ValuePredictorliver(to_predict_list,7)
        #caancer
        elif len(to_predict_list) == 5:
            result=ValuePredictorcancer(to_predict_list,5)
    if (int(result) == 1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("result.html", prediction_text=prediction))

@app.route('/register')
def register():
    return render_template("register.html")
@app.route('/error')
def error():
    return render_template("error.html")
@app.route('/result1',methods=['POST','GET'])
def result1():
    mydb = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="2002",
                                 database="register"
                                 )
    mycursor = mydb.cursor()

    if request.method == 'POST':
        signup = request.form
        fullname = signup['name1']
        email = signup['email']
        phoneno = signup['phoneno']
        dob = signup['dob']
        gender = signup['gender']
        address = signup['address']
        country = signup['country']
        city = signup['city']
        pincode = signup['pincode']
        disesae = signup['Disease']
        mycursor.execute("insert into reg (name,email,phoneno,birthdate,gender,address,country,city,pincode,disease)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(fullname,email,phoneno,dob,gender,address,country,city,pincode,disesae))

        mydb.commit()
        mycursor.close()
        if disesae=="Heart":
            return render_template("heart.html")
        elif disesae=="Kidney":
            return render_template("kidney.html")
        elif disesae=="Liver":
            return render_template("liver.html")
        elif disesae=="Cancer":
            return render_template("cancer.html")
        elif disesae=="Diabetes":
            return render_template("diabetes.html")
        else :
            return render_template("error.html");
#    name = request.form.get('full_name')
#    email = request.form.get('email')
#    country= request.form.get('country')
#    if country =='India':
#        return "the email is {} and the name is {} and country is {}".format(email,name,country)
#    else:
#        return "error 404"



if __name__ == "__main__":
    app.run(debug=True)

