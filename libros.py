'''
Define una clase llamada “Libro” con los siguientes atributos: titulo, autor, genero y
puntuacion (valor numérico que representa la popularidad del libro). Crea un método
__init__ para inicializar estos atributos.
'''

class Libro:
    def __init__(self,titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion
    
# Crea una lista llamada lista_libros donde almacenarás los objetos de la clase Libro.

lista_libros = []

'''Agregar Libro: Solicita al usuario que ingrese el título, autor, género y
puntuación del libro. Crea un objeto Libro con estos atributos y agrega el
objeto a la lista lista_libros.'''

def agregar_libro(lista_libros):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    puntuacion = float(input("Ingrese la puntuación del libro (0-5): "))

# Crear un objeto Libro
nuevo_libro = agregar_libro(lista_libros)

# Agregar el objeto a la lista
lista_libros.append(nuevo_libro)

print("Libro agregado exitosamente!")