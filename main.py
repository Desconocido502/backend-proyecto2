# Se importan las clases y las herramientas a usar
from Usuario import Usuario
from Administrador import Administrador
from Publicacion import Publicacion
from flask import Flask, jsonify, request
from flask_cors import CORS

import json
import re

Usuarios = []  # lista que contedra a mis users
administradorAux = Administrador(
    'Abner Cardona', 'admin', 'admin@ipc1.com', 'admin@ipc1')

publicacion2 = Publicacion(
    'image', 'https://m.media-amazon.com/images/I/61YvHa6o94L._SY355_.jpg', '03/10/21', 'Headphones', 7, 'KevinR')
publicacion3 = Publicacion(
    'image', 'https://s.cdnshm.com/catalog/za/t/73987000/xiaomi-redmi-note-9-128gb.jpg', '03/10/21', 'SmartPhones', 14, 'Carlos74@')
publicacion4 = Publicacion(
    'video', 'https://www.youtube.com/embed/o4J8px-4hww', '25/10/2021', 'Corridos tumbados', 5, 'KevinR')
publicacion5 = Publicacion(
    'video', 'https://www.youtube.com/embed/UOwmbA_tJOY', '25/10/2021', 'Corridos tumbados', 2, 'Carlos74@')

publicaciones = []
publicaciones2 = []

publicaciones2.append(publicacion2)
publicaciones.append(publicacion3)
publicaciones2.append(publicacion4)
publicaciones.append(publicacion5)

Usuarios.append(Usuario('Carlos Soto', 'M', 'Carlos74@',
                'carlos5231fac@gmail.com', 'cesm4561', publicaciones))
Usuarios.append(Usuario('kevin Reyes', 'M', 'KevinR',
                'reyesK31@gmail.com', '74eds', publicaciones2))

app = Flask(__name__)
#* Agregamos el CORS para que esto no nos de
#* problemas a la hora de comunicarnos con el FRONTEND
CORS(app)


def validarUserName(cadena=''):
    # print('Entramos a la funcion de la validacion de usuario')
    textoBuscar = '[\w{8,}]+\W'
    if cadena == '':
        # print('Cadena vacia')
        return None
    elif re.search(textoBuscar, cadena):
        # print('Nombre de usuario valido')
        return True
    else:
        # print('Nombre de usuario no valido')
        return False


def mostrarUsuarios():
    global Usuarios
    for user in Usuarios:
        print(user.password)
        print('*****************************')


@app.route('/', methods=['GET'])
def rutaInicial():
    return("<h1>Hola Crack!</h1>")


@app.route('/Login', methods=['POST'])
def verificarLogueo():
    global Usuarios
    tipoUser = ''
    userName = request.json['userName']
    password = request.json['password']
    print(f'Nombre de usuario: {userName}, password: {password}')
    if userName == administradorAux.userName and password == administradorAux.password:
        tipoUser = 'administrador'
        print('Administrador Encontrado!')
        return jsonify({'Mensaje': f'{tipoUser}', "Usuario": None})
    else:
        for user in Usuarios:
            if user.userName == userName and user.password == password:
                print('Usuario Encontrado!')
                tipoUser = 'usuario'
                return jsonify({'Mensaje': f'{tipoUser}', "Usuario": user.userName})
            else:
                tipoUser = None
                return jsonify({'Mensaje': f'{tipoUser}', "Usuario": "Ningun usuario"})

# *Obtener una lista de usuarios


@app.route('/admin/list', methods=['GET'])
def getUsuarios():
    print("Enviando lista de usuarios")
    global Usuarios
    datos = []
    for user in Usuarios:
        # print(user)
        objeto = {
            'name': user.name,
            'gender': user.gender,
            'userName': user.userName,
            'email': user.email
        }
        datos.append(objeto)
    return(jsonify(datos))

# * crear un usuario nuevo


@app.route('/registro', methods=['POST'])
def createUser():
    print('Entramos a la creacion de usuario')
    global Usuarios
    if validarUserName(request.json['userName']) == None:
        respuesta = jsonify(
            {'error': None, 
                "Mensaje": "Dejo vacio el espacio de su nombre de usuario, agregelo!"})
        return(respuesta)
    elif validarUserName(request.json['userName']) == False:
        respuesta = jsonify(
            {'error': True,
                "Mensaje": "Su nombre de usuario debe tener al menos 8 caracteres en los cuales puede llevar numeros mas un simbolo, corrijalo"})
        return(respuesta)
    elif validarUserName(request.json['userName']) == True:
        userName = request.json['userName']
        for user in Usuarios:
            if user.userName == userName:
                return(jsonify({"error": True, 
                                "Mensaje": "El nombre de usuario se repite, ingrese otro nombre"}))
            else:
                newUser = Usuario(request.json['name'], request.json['gender'],
                                    request.json['userName'], request.json['email'], request.json['password'], [])
                Usuarios.append(newUser)
                return(jsonify({"error": False, "Mensaje": "Usuario creado"}))

# * Obtener un usuario por nombre de usuario


@app.route('/usuarios/<string:userName>', methods=['GET'])
def getUser(userName):
    global Usuarios
    for user in Usuarios:
        if user.userName == userName:
            print('Usuario encontrado')
            objeto = {
                'name': user.name,
                'gender': user.gender,
                'userName': user.userName,
                'email': user.email
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))


# * Actualizar un usuario por nombre de usuario
@app.route('/usuarios/<string:userNameB>', methods=['PUT'])
def updateUser(userNameB):
    global Usuarios
    for i in range(len(Usuarios)):
        if userNameB == Usuarios[i].userName:
            if validarUserName(request.json['userName']) == None:
                respuesta = jsonify(
                    {'error': None, 
                        "Mensaje": "Dejo vacio el espacio del nombre de su nombre usuario, agregelo!"})
                return(respuesta)
            elif validarUserName(request.json['userName']) == False:
                respuesta = jsonify(
                    {'error': True, 
                        "Mensaje": "Su nombre de usuario debe tener al menos 8 caracteres en los cuales puede llevar numeros mas un simbolo, corrijalo"})
                return(respuesta)
            elif validarUserName(request.json['userName']) == True:
                Usuarios[i].name = request.json['name']
                Usuarios[i].gender = request.json['gender']
                Usuarios[i].userName = (request.json['userName'])
                Usuarios[i].email = (request.json['email'])
                mostrarUsuarios()
                return jsonify({'Mensaje': 'Se actualizó su informacion exitosamente'})
    return(jsonify({'Mensaje': 'No se encontró al usuario a actualizar'}))

# *Eliminar un usuario por nombre de usuario


@app.route('/usuarios/<string:userName>', methods=['DELETE'])
def deleteUser(userName):
    global Usuarios
    for i in range(len(Usuarios)):
        if userName == Usuarios[i].userName:
            del Usuarios[i]
            return(jsonify({'Mensaje': 'Se eliminó al usuario exitosamente'}))
    return(jsonify({'Mensaje': 'No se encontró al usuario a eliminar'}))

# * Retornar el arreglo de publicaciones de un usuario indicado


@app.route('/user/<string:userName>', methods=['GET'])
def getPosts(userName):
    print('Entramos a la busqueda de las publicaciones')
    global Usuarios
    posts = []
    for position in range(len(Usuarios)):
        if userName == Usuarios[position].userName:
            for post in Usuarios[position].obtenerPublicaciones:
                print(f'{post}\n')
                objeto = {
                    'tipo': post.tipo,
                    'url': post.url,
                    'date': post.date,
                    'categoria': post.categoria,
                    'like': post.like
                }
                posts.append(objeto)
            return(jsonify({'posts': posts, 'Mensaje': 'Publicaciones enviadas correctamente'}))
    return(jsonify({'posts': posts, 'Mensaje': 'Publicaciones no encontradas'}))


# * Envio de usuario al admin para actualizar los datos el usuario
@app.route('/admin/usuarios/<string:userName>', methods=['GET'])
def getUserToAdmin(userName):
    global Usuarios
    for user in Usuarios:
        if user.userName == userName:
            print(f'user.password')
            objeto = {
                'name': user.name,
                'gender': user.gender,
                'userName': user.userName,
                'email': user.email,
                'password': user.password
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

# *Datos actualizados por el administrador


@app.route('/admin/updateUsuarios/<string:userNameB>', methods=['PUT'])
def updateUsuario(userNameB):
    global Usuarios
    for updateUser in Usuarios:
        if updateUser.userName == userNameB:
            if validarUserName(request.json['userName']) == None:
                respuesta = jsonify(
                    {'error': None, 
                        "Mensaje": "Dejo vacio el espacio del nombre de usuario, agregelo!"})
                return(respuesta)
            elif validarUserName(request.json['userName']) == False:
                respuesta = jsonify(
                    {'error': True, 
                        "Mensaje": "El nombre de usuario debe tener al menos 8 caracteres"})
                return(respuesta)
            elif validarUserName(request.json['userName']) == True:
                # * Se actualizan los datos del usuario
                updateUser.name = request.json['name']
                updateUser.gender = request.json['gender']
                updateUser.userName = request.json['userName']
                updateUser.email = request.json['email']
                updateUser.password = request.json['password']
                print('Datos actualizados!!')
                mostrarUsuarios()
                respuesta = jsonify(
                    {"error": False, "Mensaje": "Usuario actualizado"})
                return(respuesta)
    respuesta = jsonify({"error": True, "Mensaje": "Usuario no encontrado"})
    return(respuesta)

# * asignar una nueva publicacion a un usuario por su username


@app.route('/user/postPublicaciones/<string:userName>', methods=['POST'])
def agregarPublicacion(userName):
    global Usuarios
    tipo = str(request.json['tipo'])
    url = str(request.json['url'])
    date = str(request.json['date'])
    categoria = str(request.json['category'])
    like = int(request.json['like'])
    for user in Usuarios:
        if user.userName == userName:
            print(userName)
            print(user.userName)
            publicacionNueva = Publicacion(
                tipo, url, date, categoria, like, userName)
            user.agregar_publicacion(publicacionNueva)
    return(jsonify({"Mensaje": "agregada la nueva publicacion al Usuario"}))

# * Agregamos usuarios de forma masiva


@app.route('/admin/agregarUsers', methods=['POST'])
def cargaMasivaUsers():
    listaUsuariosACargar = request.json['usuarios']
    for newUsuario in listaUsuariosACargar:
        Usuarios.append(Usuario(newUsuario["name"], newUsuario["gender"],
                        newUsuario["username"], newUsuario["email"], newUsuario["password"], []))
    return(jsonify({"Mensaje": "Todos los usuarios fueron cargados al servidor"}))

# * Cargamos las publicaciones del json y se las asignamos al usuario


@app.route('/admin/agregarPostAUser', methods=['POST'])
def cargarPublicaciones():
    global Usuarios
    listaImg = request.json['image']
    listaVideo = request.json['video']

    for img in listaImg:
        for user in Usuarios:
            if img['author'] == user.userName:
                user.agregar_publicacion(Publicacion(
                    "image", img["url"], img["date"], img["category"], 0, img["author"]))

    for video in listaVideo:
        for user in Usuarios:
            if video['author'] == user.userName:
                user.agregar_publicacion(Publicacion(
                    "video", video["url"], video["date"], video["category"], 0, video["author"]))
    return(jsonify({"Mensaje": "Todas las publicaciones fueron cargadas al servidor"}))

# * Vamos a obtener todas las publicaciones para enviarlas al front


@app.route('/allPosts', methods=['GET'])
def getAllPosts():
    global Usuarios
    listaPostsGlobal = []
    '''
    Lo que vamos a hacer es iterar en cada uno de los usuarios, por cada usuario
    iteremos la lista de publicaciones que posee cada uno, y se va agregando a
    una lista global, esa lista global se ordena por el numero de likes, y luego
    se manda al front, para que los datos se puedan mostrar.
    '''
    for user in Usuarios:
        for publicacion in user.obtenerPublicaciones:
            listaPostsGlobal.append(publicacion)

    # listaPostsGlobal.sort(reverse= lambda post: int(post.like))
    listaGlobalPosts2 = sorted(
        listaPostsGlobal, key=lambda post: post.like, reverse=True)
    listaPostsGlobal = []
    for publicacion in listaGlobalPosts2:
        # print(f'{publicacion}\n')
        objeto = {
            'id_publicacion': publicacion.id_publicacion,
            'tipo': publicacion.tipo,
            'url': publicacion.url,
            'date': publicacion.date,
            'categoria': publicacion.categoria,
            'like': publicacion.like,
            'author': publicacion.author
        }
        listaPostsGlobal.append(objeto)
    return(jsonify({"allPost": listaPostsGlobal, "Mensaje": "Se cargaron correctamente las publicaciones al arreglo"}))

# * Vamos a aumentar el numero de likes de cierta publicacion


@app.route('/aumentoLikes', methods=["POST"])
def aumentarLikePublicacion():
    id_publicacion = int(request.json['id_publicacion'])
    # print(f'id_publicacion es: {id_publicacion}')
    userName = request.json['userName']
    contadorAuxiliar = 0
    global Usuarios
    for user in Usuarios:
        if user.userName == userName:
            for post in user.obtenerPublicaciones:
                if post.id_publicacion == id_publicacion:
                    post.like += 1
                    contadorAuxiliar = int(post.like)
    # print(f'\nEl contador de likes es: {contadorAuxiliar}\n')
    return(jsonify({"Mensaje": "Se asigno el like a {userName} correctamente", "id_publicacion": id_publicacion, "cantidadLike": contadorAuxiliar}))

# * Se mandan los top 5 post con mas likes


@app.route('/admin/topPost', methods=['GET'])
def getTopPost():
    global Usuarios
    listaPostsG = []

    for user in Usuarios:
        for publicacion in user.obtenerPublicaciones:
            listaPostsG.append(publicacion)
    listaGlobalPosts2 = sorted(
        listaPostsG, key=lambda post: post.like, reverse=True)
    listaPostsG = []

    if len(listaGlobalPosts2) < 5:
        return(jsonify({"Mensaje": "No se puede realizar el top Publicaciones, debido a falta de datos", "error": True}))
    else:
        for x in range(0, 5):
            listaPostsG.append(listaGlobalPosts2[x])

        lista_top = []
        for publicacion in listaPostsG:
            #print(f'id publicacion: {publicacion.id_publicacion}')
            objeto = {
                'id_publicacion': publicacion.id_publicacion,
                'tipo': publicacion.tipo,
                'url': publicacion.url,
                'date': publicacion.date,
                'categoria': publicacion.categoria,
                'like': publicacion.like,
                'author': publicacion.author
            }
            lista_top.append(objeto)
        return(jsonify({"Mensaje": "El top ha sido realizado con exito", "top": lista_top, "error": False}))

# * Vamos a hacer un conteo de publicaciones de cada usuario, para hacer un top 5


@app.route("/admin/topUsers")
def topUsersPost():
    global Usuarios
    lista_contador_publicaciones = []
    listaUsersG = []
    for user in Usuarios:
        print(f'nombre:{user.name}')
        lista_contador_publicaciones.append({
            "name": user.name,
            "userName": user.userName,
            "gender": user.gender,
            "email": user.email,
            "publicaciones": len(user.obtenerPublicaciones)
        })

    listaUsersG = sorted(
        lista_contador_publicaciones, key=lambda user: user['publicaciones'], reverse=True)

    if len(listaUsersG) < 5:
        return(jsonify({"Mensaje": "No se puede realizar el top Usuarios, debido a falta de datos", "error": True}))
    else:
        lista_top_usuarios = []
        for x in range(0, 5):
            lista_top_usuarios.append(listaUsersG[x])
            # print((lista_top_usuarios[x]))
        lista_contador_publicaciones = []
        for user in lista_top_usuarios:
            objeto = {
                "name": user['name'],
                "userName": user['userName'],
                "gender": user['gender'],
                "email": user['email'],
                "publicaciones": user['publicaciones']
            }
            lista_contador_publicaciones.append(objeto)
        return(jsonify({"Mensaje": "Todo sin problemas", "usuarios": lista_contador_publicaciones, "error": False}))


# * Vamos a pedir la lista de todos los usuarios, y los vamos a pasar a una tabla


@app.route("/admin/allDates")
def getAllDates():
    global Usuarios
    lista_a_enviar = []
    for user in Usuarios:
        objeto = {
            'name': user.name,
            'gender': user.gender,
            'userName': user.userName,
            'email': user.email,

        }
        lista_a_enviar.append(objeto)

    listaPostsGlobal = []
    for user in Usuarios:
        for publicacion in user.obtenerPublicaciones:
            listaPostsGlobal.append(publicacion)

    lista_a_enviar_post = []
    for publicacion in listaPostsGlobal:
        objeto = {
            'id_publicacion': publicacion.id_publicacion,
            'tipo': publicacion.tipo,
            'url': publicacion.url,
            'date': publicacion.date,
            'categoria': publicacion.categoria,
            'like': publicacion.like,
            'author': publicacion.author
        }
        lista_a_enviar_post.append(objeto)

    return(jsonify({"Mensaje": "Se envia la lista de usuarios", "usuarios": lista_a_enviar, "publicaciones": lista_a_enviar_post}))

# * Vamos a mandar las publicaciones rankeadas de un solo usuario


@app.route('/userRanked/<string:userName>', methods=['GET'])
def getRankedPostUser(userName):
    global Usuarios
    lista_post = []
    for user in Usuarios:
        if userName == user.userName:
            lista_post = user.obtenerPublicaciones
            break
    lista_ordenada = sorted(
        lista_post, key=lambda post: post.like, reverse=True)
    lista_post = []
    for post in lista_ordenada:
        objeto = {
            'id_publicacion': post.id_publicacion,
            'tipo': post.tipo,
            'url': post.url,
            'date': post.date,
            'categoria': post.categoria,
            'like': post.like,
            'author': post.author
        }
        lista_post.append(objeto)
    return(jsonify({"Mensaje": "Todo correcto", "publicaciones": lista_post}))

# *Eliminar una publicacion por nombre de su id


@app.route('/usuarios/publicaciones/<int:id_publicacion>', methods=['DELETE'])
def deletePost(id_publicacion):
    global Usuarios
    for user in Usuarios:
        publicaciones = user.obtenerPublicaciones
        for x in range(0, len(user.obtenerPublicaciones)):
            if id_publicacion == publicaciones[x].id_publicacion:
                del publicaciones[x]
                return(jsonify({'Mensaje': 'Se elimino la publicación'}))
    return(jsonify({'Mensaje': 'No se encontró la publicación a eliminar'}))


if __name__ == "__main__":
    # Le decimos que el host es 0.0.0.0 para que corra en Localhost
    # Le indicamos el puerto (Tema pendiente por ver) para indicarle en que puerto levantara la aplicacion
    app.run(host="0.0.0.0", port=4000, debug=True)
