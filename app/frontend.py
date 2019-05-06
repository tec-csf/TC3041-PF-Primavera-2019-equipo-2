from flask import Flask,jsonify,request,make_response,redirect,url_for,render_template, session
from flask_bootstrap import Bootstrap
from models import sessions, persons
from pymongo import MongoClient
from flask_api import FlaskAPI, status, exceptions
import jinja2
import os

env = jinja2.Environment()
env.globals.update(zip=zip)
SECRET_KEY = os.urandom(32)
id = 9

app = FlaskAPI(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)
app.jinja_env.filters['zip'] = zip

@app.route('/test', methods=['POST','GET'])
def test():
    string = "Api working"
    return string

@app.route('/login', methods=['POST','GET'])
def login():

    if request.method == 'POST':

        user = request.form.get('email')

        password = request.form.get('pass')

        #if(a.verify_password(user,password)):
            # user['_id'] = user
        return redirect(url_for('index'))
        #else:
            #print("wrong")

    return render_template("login.html")

@app.route('/index', methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST','GET'])
def registro():

    if request.method == 'POST':

        user = request.form.get('email')
        print("agap",user)
        name = request.form.get('name')
        print("agap",name)
        comp = request.form.get('comp')
        print("agap",comp)
        age = request.form.get('age')
        print("agap",age)
        phone = request.form.get('phone')
        print("agap",phone)
        password = request.form.get('password')
        print("agap",password)

        id = id + 1
        #a.insert_user(id,email,name,company,age,phone)

        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/obtener')#, methods=['GET'])
def obtener():
    p = persons.Persons()
    one = p.findOne('Wendi Mcdonald')
    k = []
    k.append(one)
    two = p.findWhere('k')
    k.append(two)
    three = p.findFriends(1)
    k.append(three)
    return k


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
