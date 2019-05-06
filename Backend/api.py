from flask import Flask,jsonify,request,make_response,redirect,url_for,render_template
from flask_api import FlaskAPI, status, exceptions
from bson.objectid import ObjectId
from flask_wtf import Form
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired, Email,Length,AnyOf
from .models import login, user
from datetime import datetime
#from .models import libros, usuario




class LoginForm(Form):
    username = StringField('email', validators=[InputRequired(),Email(message='Invalid email.')])
    password = PasswordField('password', validators=[InputRequired(),Length(min=5,max=15)])

class API(object):

    def update_user(self,user,password):
        red = login.Login()
        red.set_user(user,password)



    def verify_password(self,user,password):
        red = login.Login()

        hashedPassword = red.hashed_pass(password)

        redisPassword = red.get_user_password(user)

        if(redisPassword != None):
            if redisPassword.decode() == hashedPassword:
              return True
            return False
        return False

    def insert_user(self,user,password,nombre,apellido,email):
         red = login.Login()
         mongodb = user.User()

         #red.set_user(user,password)
         #mongodb.insert_user(user,nombre,apellido,email)



#view queries
    def get_all_users(self):
        mongodb = user.Users()
        person = mongodb.find()

        return person
'''
    def get_all_tasks_by_genre(self):
        mongodb = libros.Libros()
        libs = mongodb.findByGenre()

        return libs

    def get_all_tasks_by_author(self):
        mongodb = libros.Libros()
        libs = mongodb.findByAuthor()

        return libs

    def get_user_books(self,user):
        mongodb = usuarios.Usuarios()
        libs = mongodb.findOne(user)
        return libs

    def send_book(self,id,libro):
        mongodb = usuarios.Usuarios()
        mongodb.add_book(id,libro)
'''
