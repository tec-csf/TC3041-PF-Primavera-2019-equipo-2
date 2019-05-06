from pymongo import MongoClient
from bson import ObjectId
from flask import request, url_for, jsonify
import config

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
        cursor = self.collection.find()

        usuarios = []

        for usuario in cursor:
            # Se adicionó para poder manejar ObjectID
            usuario['_id'] = str(usuario['_id'])
            usuarios.append(usuario)

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
        k = []
        for i in range(len(temp)):
            if i%2 == 1:
                temp2 = temp[i]
                result3 = list(self.collection.find({"_id":int(temp2)}))
                k.append(result3)
        return k
