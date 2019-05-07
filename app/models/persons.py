from pymongo import MongoClient
from bson import ObjectId
from flask import request, url_for, jsonify
from flask_wtf import Form
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired, Email,Length,AnyOf
import config
from models import sessions

class Persons(object):

    def __init__(self):
        client = MongoClient(config.MONGO_URI)
        db = client.db
        self.collection = db.person

    def insert_user(self,id,email,name,company,age,phone):

        userJson = { "_id": id, "name": name, "company": company, "email": email, "age":age, "phone":phone, "knows":[]}
        self.collection.insert_one(userJson)


    def find(self):
        """
        Obtener todos
        """

        usuarios = []


        return usuarios

    def findOne(self, name):
        """
        Desplegar toda tu informacion
        """
        pipe = [{"$match":{"email":name}}]

        usuario = self.collection.aggregate(pipe)
        result = list(usuario)
        return result

    def findWhere(self, name):
        """
        Buscar personas que tengan la letra K en su nombre
        """
        where = "{}".format(name)
        pipe = [{"$match":{"name":{ "$regex": where }}}]

        cursor = self.collection.aggregate(pipe)
        result = list(cursor)
        return result


    def findFriends(self, name):
        """
        Despliega a tus conocidos
        """
        cursor = self.collection.distinct("knows", {"_id":name})
        result2 = list(cursor)
        temp = result2[0]
        k2 = []
        for i in range(len(temp)):
            if i%2 == 1:
                temp2 = int(temp[i])
                k =[]
                cursor = self.collection.distinct("name",{"_id":temp2})
                result = list(cursor)
                k.append(result)
                cursor = self.collection.distinct("company",{"_id":temp2})
                result = list(cursor)
                k.append(result)
                cursor = self.collection.distinct("email",{"_id":temp2})
                result = list(cursor)
                k.append(result)
                k2.append(k)

        return k2

    def findNames(self, name):
        """
        Despliega a tus conocidos
        """
        cursor = self.collection.distinct("knows", {"_id":name})
        result2 = list(cursor)
        temp = result2[0]
        k = []
        for i in range(len(temp)):
            if i%2 == 1:
                temp2 = temp[i]
                result3 = list(self.collection.distinct("name",{"_id":int(temp2)}))
                k.append(result3)

        return k

    def findID(self, name):
        """
        Despliega mi id
        """
        cursor = self.collection.distinct("_id", {"email":name})
        result2 = list(cursor)

        return result2

    def findME(self, id):
        """
        Despliega mi info
        """

        k = []
        cursor = self.collection.distinct("name",{"_id":id})
        result = list(cursor)
        k.append(result)
        cursor = self.collection.distinct("company",{"_id":id})
        result = list(cursor)
        k.append(result)
        cursor = self.collection.distinct("email",{"_id":id})
        result = list(cursor)
        k.append(result)
        return k

class LoginForm(Form):
    username = StringField('username', validators=[InputRequired(),Email(message='Invalid email.')])
    password = PasswordField('password', validators=[InputRequired(),Length(min=5,max=15)])

class API(object):

    def update_user(self,user,password):
        red = sessions.Sessions()
        red.set_user(user,password)



    def verify_password(self,user,password):
        red = sessions.Sessions()

        hashedPassword = red.hashed_pass(password)

        redisPassword = red.get_user_password(user)

        if(redisPassword != None):
            if redisPassword.decode() == hashedPassword:
              return True
            return False
        return False

    def insert_user(self,user,password):
         red = sessions.Sessions()

         red.set_user(user,password)
