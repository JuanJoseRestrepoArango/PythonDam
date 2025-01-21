

class Libro:

    def __init__(self,Isbn, titulo, autor, precio, añoPublicacion = 2000):
        self.Isbn = Isbn
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.añoPublicacion = añoPublicacion

    def __str__(self):
        return f'{self.titulo} {self.autor} {self.añoPublicacion}'
    
    def setAutor(self,autor):
        self.autor = autor

