from flask import Flask,jsonify,request,make_response,redirect,url_for,render_template, session
from flask_bootstrap import Bootstrap
from Backend import api
import jinja2
import os
env = jinja2.Environment()
env.globals.update(zip=zip)
SECRET_KEY = os.urandom(32)
id = 9


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)
app.jinja_env.filters['zip'] = zip


@app.route('/', methods=['GET','POST'])
def root():
    jsons = api.API()
    jsons = jsons.get_all_users()
    result=[]
    print(jsons)
    for person in jsons:
        person['_id'] = str(person['_id'])
        result.append(person)

    return #jsonify(result)

@app.route('/test', methods=['POST','GET'])
def test():
    return "Api working"

@app.route('/login', methods=['POST','GET'])
def login():

    a = api.API()
    if request.method == 'POST':

        user = request.form.get('email')

        password = request.form.get('pass')

        if(a.verify_password(user,password)):
             user['_id'] = user
             return redirect(url_for('index'))
        else:
            print("wrong")

    return render_template('login.html')

@app.route('/register', methods=['POST','GET'])
def registro():

    a = api.API()
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
        a.insert_user(id,email,name,company,age,phone)

        return redirect(url_for('login'))

    return render_template('register.html')


'''
@app.route('/index', methods=['GET','POST'])
def index():
    user = session.get('email')
    user = str(user)
    #print(user)
    #libros_array = []
    #ids_libros_array = []
    #titulos_array = []
    #imagenes_array =[]
    #autor_array =[]
    #genero_array=[]
    #fecha_de_publicacion_array=[]
    #descripcion_array=[]
    #num_paginas_array=[]
    #editorial_array=[]
    #pais_array=[]

    jsons = api.API()
    usuarios_array = jsons.get_all_users()
    #libros = jsons.get_user_books(user)
    #print("agap",libros)
    #libros_usuario =libros['libros']
    """
    if libros['libros'] == NoneType:
        libros_usuario =[]
    else:
        libros_usuario = libros['libros']
        """
'''
'''
    if request.form.get("filt"):
        filtro = request.form.get("filt")
        bandera = 1
    elif request.form.get("aut"):
        filtro = request.form.get("aut")
        bandera = 2
    else:
        bandera = 0
        filtro = 'None'
    bandera = str(bandera)

    #print("browser",filtro,bandera)

    anadir = request.form.get("anadir")
    print("añadir",anadir)
    jsons.send_book(user,anadir)
    jsons = jsons.get_all_tasks()
    #print(type(jsons))
    for i in range(len(jsons)):
        autor_array.append(jsons[i]['Autor'])
        libros_array.append(jsons[i]['Libro'])
        titulos_array.append(jsons[i]['Titulo'])
        imagenes_array.append(jsons[i]['Imagen'])
        genero_array.append(jsons[i]['Genero'])
        fecha_de_publicacion_array.append(jsons[i]['Fecha_de_Publicacion'])
        descripcion_array.append(jsons[i]['Descripcion'])
        num_paginas_array.append(int(jsons[i]['numPaginas']))
        editorial_array.append(jsons[i]['Editorial'])
        pais_array.append(jsons[i]['Pais'])
        ids_libros_array.append(jsons[i]['_id'])

    print()
    generos_limpios = []
    autores_limpios = []
    for genero in genero_array:
        if genero not in generos_limpios:
            generos_limpios.append(genero)
    for autor in autor_array:
        if autor not in autores_limpios:
            autores_limpios.append(autor)
    #print(autores_limpios)

    #print(images_array)

    if request.method == 'POST':
        a = api.API()
        password = request.form.get('password')
        a.update_user(user,password)





  return render_template('index.html')
'''

if __name__ == "__main__":
    app.run(debug=True)
