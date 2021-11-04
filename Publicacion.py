class Publicacion:
    contador_publicaciones = 0

    def __init__(self, tipo, url, date, categoria, like, author):
        Publicacion.contador_publicaciones += 1
        self._id_publicacion = Publicacion.contador_publicaciones
        self._tipo = tipo
        self._url = url
        self._date = date
        self._categoria = categoria
        self._like = like
        self._author = author

    @property
    def id_publicacion(self):
        return self._id_publicacion

    @id_publicacion.setter
    def id_publicacion(self, id_publicacion):
        self._id_publicacion = id_publicacion

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property
    def like(self):
        return self._like

    @like.setter
    def like(self, like):
        self._like = like

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    def __str__(self):
        return f'Numero de Publicacion:{self._id_publicacion},\nType: {self._tipo},\nurl: {self._url},\ndate: {self._date},\ncategoria: {self._categoria},\nlikes: {self._like},\nauthor: {self._author}'


if __name__ == '__main__':
    publicacion1 = Publicacion('image',
                                'https://youtube.com/dfmije5f', '03/10/21', 'Flowers', 0, "CarlosA")
    print(publicacion1)
