from calendar import c
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

clf=pickle.load(open('model.sav','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/detect',methods=['POST','GET'])
def predict():
    gender = int(request.form["gender"])
    sscp = float(request.form["sscp"])
    hsp = float(request.form["hsp"])
    fd = float(request.form["fd"])
    we= int(request.form["we"])
    pep = float(request.form["pep"])
    age = request.form["age"]
    degree = request.form["degree"]
    if age == "1":
        cap=0
        s=1
        a=0
    elif age == "2":
        cap = 0
        s = 0
        a = 1
    elif age == "3":
        cap = 1
        s = 0
        a = 0
    else:
        cap = 0
        s = 0
        a = 0

    if degree == "1":
        x=1
        y=0
        z=0
    elif degree == "2":
        x=0
        y=0
        z=1
    elif degree == "3":
        x=0
        y=1
        z=0
    else:
        x=0
        y=0
        z=0
        

    # print(gender,sscp,hsp,fd,we,pep,cap,s,a,x,y,z) 
    final = [gender,sscp,hsp,fd,we,pep,cap,s,a,x,y,z]
    prediction=clf.predict([final])
    probability = clf.predict_proba([final]).max()*100
    probability = round(probability)
    if probability >= 60:
        prob = "(2.5L - 3.5L)"
    elif probability >=80:
        prob = "(3.5L - 5.5L)"
    else:
        prob = "(7.5L)" 
    nprob = "-"
    
   
    if prediction == 1:
        return render_template('index.html',pred='Congrulations High Chances of Getting Placement', prob=prob)
    if prediction == 0:
        return render_template('index.html',red='You Need To Work Hard', pro=nprob)



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port="33")

