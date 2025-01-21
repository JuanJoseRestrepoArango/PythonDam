from Libro import Libro as lb;
from Biblioteca import Biblioteca as bib;
import copy

book = lb("xxxxxx", "book","Juan",100)
print(book)
book2 = copy.deepcopy(book)
book2.setAutor("Jose")
print(book2)
retiro = bib("Retriro","c/Doctor Ezquerdo")
retiro.addBook(book)
retiro.addBook(book2)
print(retiro)
retiro.deleteBook(lb("xxxxxx", "book","Juan",100))
print(retiro)
latina = copy.deepcopy(retiro)
latina.setNombre("Latina")
latina.addBook(book2)
print(latina)
