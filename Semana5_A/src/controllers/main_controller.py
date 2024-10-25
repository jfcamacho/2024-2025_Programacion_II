from src.controllers.CRUD_Persona import *
from src.controllers.CRUD_Estudiante import *

crudPersona = CRUD_PERSONA()
crudEstudiante = CRUD_ESTUDAINTE()

def seederData():
    crudPersona.seederData()

def main_menu(op):
    if op == 1:
        nombre = input('Ingrese el nombre.: ')
        apellido = input('Ingrese el apellido.: ')
        crudPersona.crear(nombre, apellido)
    if op == 2:
        crudPersona.listarPersonas()
        id = int(input('Ingrese el id de la persona.: '))
        institucion = input('Ingrese la institución.: ')
        matricula = input('Número de matricula.: ')
        crudEstudiante.crear(id, institucion, matricula)
    if op == 3:
        print(crudPersona.total())
    if op == 4:
        print(crudEstudiante.total())
    if op == 5:
        crudPersona.listarPersonas()
    if op == 6:
        crudEstudiante.listarEstudiantes()
