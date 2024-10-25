from src.controllers.main_controller import *

def menu():
    print(10*"-","Menu Principal", 10*"-")
    print('1.- Ingresar Persona')
    print('2.- Ingresar Estudiante')
    print('3.- Mostrar total personas')
    print('4.- Mostrar total estudiantes')
    print('5.- Mostrar personas')
    print('6.- Mostrar estudiantes')
    print('7.- Salir')

    return int(input('Escoja una opción.: '))

def start():
    seederData()
    while True:
        op = menu()
        if op == 7:
            break
        main_menu(op)