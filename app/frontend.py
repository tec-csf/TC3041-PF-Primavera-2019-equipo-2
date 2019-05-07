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


app = FlaskAPI(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)
app.jinja_env.filters['zip'] = zip

@app.route('/')
def start():

    return redirect(url_for('login'))

@app.route('/test')
def test():
    string = "Api working"
    return string

@app.route('/login', methods=['POST','GET'])
def login():

    p = persons.Persons()
    a = persons.API()
    if request.method == 'POST':

        user = request.form.get('username')
        print("user:",user)
        password = request.form.get('pass')
        print("password:",password)
        if(a.verify_password(user,password)):
            session['user'] = user
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template("login.html")

@app.route('/index', methods=['POST','GET'])
def index():
    p = persons.Persons()
    names = p.findNames(1)#(user)
    knows = p.findFriends(1)#(user)
    #print("knows",knows[0]['name'])
    if request.method == 'POST':

        search = request.form.get('search')
        #print("agap", search)

        cursor = p.findWhere(search)
        searched = list(cursor)
        #print("searched", searched)

        return render_template("index.html",searched=searched,knows=knows,nombre=names)

    return render_template("index.html")

@app.route('/register', methods=['POST','GET'])
def registro():

    p = persons.Persons()
    a = persons.API()
    if request.method == 'POST':

        user = request.form.get('email')
        print("email",user)
        name = request.form.get('name')
        print("name",name)
        comp = request.form.get('comp')
        print("comp",comp)
        age = request.form.get('age')
        print("age",age)
        phone = request.form.get('phone')
        print("phone",phone)
        password = request.form.get('pass')
        print("pass",password)

        id = 99
        a.insert_user(user,password)
        p.insert_user(id,user,name,comp,age,phone)
        return redirect(url_for('login'))

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
