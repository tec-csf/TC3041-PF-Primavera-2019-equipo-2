from pymongo import MongoClient
from bson import ObjectId
from flask import request, url_for, jsonify
from backend import config

class Users(object):

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

    def findOne(self, email):
        """
        Desplegar toda tu informacion
        """
        usuario = self.collection.find({'email': email})

        if usuario is not None:
            usuario['_id'] = str(usuario['_id'])

        return usuario

    def findWhere(self, name):
        """
        Buscar personas que tengan la letra K en su nombre
        """
        where = "/{}/".format(name)

        usuario = self.collection.find({'name': where})
        usuarios = []

        if usuario is not None:
            usuario['_id'] = str(usuario['_id'])
            usuarios.append(usuario)

        return usuarios

    def findFriends(self, name):
        """
        Despliega a tus conocidos
        """
        friends = [{$match:{ 'name': {} }}, {$project:{'_id':0, 'knows':1}}]);
        #QUERY NO TERMINADO

        usuario = self.collection.aggregate(friends)

        if usuario is not None:
            usuario['_id'] = str(usuario['_id'])

        return usuario

#DEFINIR
    def create(self, usuario):
        """
        Insertar una nota nueva
        """
        result = self.collection.insert_one(usuario)

        return result

    def delete(self, id):
        """
        Eliminar una nota
        """
        result = self.collection.delete_one({'_id': ObjectId(id)})

        return result
