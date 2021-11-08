from Publicacion import Publicacion

class Usuario:
    def __init__(self, name, gender, userName, email, password, publicaciones):
        self._name = name
        self._gender = gender
        self._userName = userName
        self._email = email
        self._password = password
        self._publicaciones = list(publicaciones)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self, userName):
        self._userName = userName

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def agregar_publicacion(self, publicacion):
        self._publicaciones.append(publicacion)

    @property
    def obtenerPublicaciones(self):
        return self._publicaciones

    def __str__(self):
        publicaciones_str = '\n'
        for publicacion in self._publicaciones:
            publicaciones_str += publicacion.__str__() + '\n\n'
        return f'Mi nombre es: {self._name},\n mi genero es: {self.gender},\n mi nombre de usuario es: {self._userName},\n mi correo es: {self._email},\npublicaciones: \n{publicaciones_str}'


if __name__ == '__main__':
    print('Hola')
    publicacion2 = Publicacion(
        'image', 'https://5.imimg.com/data5/RS/VR/GM/SELLER-29296573/bluetooth-headphones-500x500.jpg', '03/10/21', 'Headphones', 0, "CarlosA")
    publicacion3 = Publicacion(
        'image', 'https://www.hisense.es/wp-content/uploads/2019/06/4-1.jpg', '03/10/21', 'SmartPhones', 0, "CarlosA")
    publicaciones = []
    publicaciones.append(publicacion2)
    publicaciones.append(publicacion3)
    usuario1 = Usuario("Carlos", 'M', 'Desconocido987',
                       'carlos5231fac@gmail.com', '123#4efa', publicaciones)
    print(usuario1)
    usuario1.name = 'Eduardo'
    print(f'Me actualizaron el nombre\n {usuario1}')

    print('\nPublicaciones\n')
    for post in usuario1.obtenerPublicaciones:
        print(f'{post}\n')
