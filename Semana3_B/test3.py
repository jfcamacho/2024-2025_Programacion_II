from test1 import *
from metodos import Acciones
n = 0
acciones = Acciones()

personas = [
    Persona(1,'Carlos', 'Guzman', 'admin1'),
    Persona(2, 'Anibal', 'Fernandez', 'admin2'),
    Persona(3, 'Esther', 'Dominguez', 'admin3'),
    Persona(4, 'Carlos', 'Peñarreta', 'admin4')
]

while n != 5:
    print(10*"-","MENU DE OPCIONES",10*"-")
    print("1.- Crear Persona")
    print("2.- Leer Persona")
    print("3.- Modificar Persona")
    print("4.- Eliminar Persona")
    print("\n5.- SALIR\n")
    n = int(input('Escoja una opcion.: '))

    if n == 1:
        nombre = input('Ingrese el nombre.: ')
        apellido = input('Ingrese el apellido.: ')
        password = input('Ingrese el password.: ')
        personas = acciones.crear(personas, Persona(len(personas), nombre, apellido, password))
    if n == 2:
        nombre = input('Ingrese el nombre.: ')
        acciones.listar(personas, nombre)
    if n == 3:
        id = int(input('A que usuario desea modificar.: '))
        nombre = input('Ingrese el nombre.: ')
        apellido = input('Ingrese el apellido.: ')
        password = input('Ingrese el password.: ')
        user = Persona(id, nombre, apellido, password)
        personas = acciones.modificar(personas, id, user)
        print('El usuario se ha actualizado...')