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
user = ''
password = ''
ID = []


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
    global user
    global password
    global ID
    if request.method == 'POST':

        user = request.form.get('username')
        password = request.form.get('pass')
        if(a.verify_password(user,password)):
            session['user'] = user
            ID = p.findID(user)


            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template("login.html")

@app.route('/index', methods=['POST','GET'])
def index():
    p = persons.Persons()
    #names = p.findNames(ID[0])
    knows = p.findFriends(ID[0])
    me = p.findME(ID[0])
    if request.method == 'POST':

        search = request.form.get('search')
        cursor = p.findWhere(search)
        searched = list(cursor)


        return render_template("index.html",searched=searched,knows=knows,ID=ID,me=me)

    return render_template("index.html",knows=knows,ID=ID,me=me)

@app.route('/register', methods=['POST','GET'])
def registro():

    p = persons.Persons()
    a = persons.API()
    if request.method == 'POST':

        user = request.form.get('email')
        name = request.form.get('name')
        comp = request.form.get('comp')
        age = request.form.get('age')
        phone = request.form.get('phone')
        password = request.form.get('pass')

        id = id + 1
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
