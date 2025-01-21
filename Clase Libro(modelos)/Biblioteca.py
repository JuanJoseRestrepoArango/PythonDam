class Biblioteca:
    def __init__(self,nombre,direccion,libros = []) :
        self.nombre = nombre
        self.direccion = direccion
        self.libros = libros
    def __str__(self) :
        cadena = f'{self.nombre} - {self.direccion}\n'
        for l in self.libros:
            cadena = cadena + '-'+l.__str__() + '\n'
        return cadena
    def addBook(self,li):
        self.libros.append(li)
    def deleteBook(self,li):
        for i, l in enumerate(self.libros):
            if l.titulo == li.titulo and l.autor == li.autor and l.añoPublicacion == li.añoPublicacion:
                del(self.libros[i])
                break

    def setNombre(self,nombre):
        self.nombre = nombre