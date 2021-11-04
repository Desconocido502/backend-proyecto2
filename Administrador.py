class Administrador:
    def __init__(self, nombre, userName, email, password):
        self._nombre = nombre
        self._userName = userName
        self._email = email
        self._password = password

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

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
        return self._password

    def __str__(self):
        return f'Mi nombre es: {self._nombre},\n mi nombre de usuario es: {self._userName},\n mi correo es: {self._email}'


if __name__ == '__main__':
    print('Hola')
    administrador1 = Administrador("Carlos", 'Desconocido987',
                                  'carlos5231fac@gmail.com', '123#4efa')
    print(administrador1)
