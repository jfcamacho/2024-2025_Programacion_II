from src.Functions.Funciones import *

class Operations:
    def selectedOperation(self, n):
        funciones = Functions()
        a = int(input('Ingrese el valor de A.: '))
        b = int(input('Ingrese el valor de B.: '))
        if n == 1:
            print(funciones.suma(a,b))
        if n == 2:
            print(funciones.resta(a,b))
        if n == 3:
            print(funciones.multiplicacion(a,b))
        if n == 4:
            print(funciones.division(a,b))
        if n == 5:
            print(funciones.potencia(a,b))

