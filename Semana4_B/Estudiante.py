from Persona import *

class Estudiante(Persona):
    _countEst = 0

    def __init__(self, name, ci, matricula):
        super().__init__(name, ci)
        self.matricula = matricula
        Estudiante._countEst += 1
    
    def descansar(self, time):
        self.time = time
        return f'{self.name} descansa {self.time} horas; porque estuvo estudiando'

    def comer(self, instruments):
        return f"{self.name} come con {instruments}"

    def getTotal(self):
        return self._countEst
        
    

estudiante1 = Estudiante('Juan', 11111111, 64654)
estudiante2 = Estudiante('Marco', 11111111, 64654)
persona1 = Persona('Esther', 33333)
persona2 = Persona('Esther', 33333)
persona3 = Persona('Esther', 33333)

print(f"hay un total de {persona2.getTotal()} personas")
print(f"hay un total de {estudiante1.getTotal()} estudiantes")