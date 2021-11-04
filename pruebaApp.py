from Usuario import Usuario
from Publicacion import Publicacion
from Publicacion import Publicacion

Usuarios = []  # lista que contedra a mis users
Publicaciones = []

Usuarios.append(Usuario('Carlos Soto', 'M', 'CarlosA',
                'carlos5231fac@gmail.com', 'cesm4561', Publicaciones))
Usuarios.append(Usuario('kevin Reyes', 'M', 'KevinR',
                'reyesK31@gmail.com', '74eds', []))

publicacion1 = Publicacion('video','https://youtu.be/RANXpALNZ4U','22/10/21', 'Corridos tumbados', 0)
publicacion2 = Publicacion(
    'image', 'https://5.imimg.com/data5/RS/VR/GM/SELLER-29296573/bluetooth-headphones-500x500.jpg', '03/10/21', 'Headphones', 0)
publicacion3 = Publicacion(
    'image', 'https://www.hisense.es/wp-content/uploads/2019/06/4-1.jpg', '03/10/21', 'SmartPhones', 0)


def mostrarUsuarios():
    global Usuarios
    for user in Usuarios:
        print(user)
        print('**************************************')


if __name__ == "__main__":
    print('Antes')
    mostrarUsuarios()
    Usuarios[0].agregar_computadora(publicacion1)
    Usuarios[0].agregar_computadora(publicacion2)
    Usuarios[1].agregar_computadora(publicacion3)
    print('Despues')
    mostrarUsuarios()
