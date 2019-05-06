from flask import Flask,jsonify,request,make_response,redirect,url_for,render_template, session
from flask_bootstrap import Bootstrap
from models import sessions, persons
import jinja2
import os
env = jinja2.Environment()
env.globals.update(zip=zip)
SECRET_KEY = os.urandom(32)
id = 9


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)
app.jinj
        id = id + 1
        #a.insert_user(id,email,name,company,age,phone)

        return redirect(url_for('login'))

    return render_template('templates/register.html')
a_env.filters['zip'] = zip


@app.route('/', methods=['GET','POST'])
def root():
    jsons = Persons()
    jsons = jsons.find()
    result=[]
    print(jsons)
    for person in jsons:
        person['_id'] = str(person['_id'])
        result.append(person)

    return jsonify(result)

@app.route('/test', methods=['POST','GET'])
def test():
    return "Api working"

@app.route('/login', methods=['POST','GET'])
def login():

    if request.method == 'POST':

        user = request.form.get('email')

        password = request.form.get('pass')

        #if(a.verify_password(user,password)):
            # user['_id'] = user
        return redirect(url_for('login'))
        #else:
            #print("wrong")

    return render_template('templates/login.html')

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

        return redirect(url_for('login'))

    return render_template('templates/register.html')


if __name__ == "__main__":
    app.run(debug=True)
