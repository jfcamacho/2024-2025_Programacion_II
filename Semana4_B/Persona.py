# Herencias, poliformismo, sobrecarga, sobreescritura
class Persona:
    _count = 0 

    def __init__(self, name, ci):
        Persona._count += 1
        self.name = name
        self.ci = ci
        self.time = 8
    
    def descansar(self):
        print(f'{self.name} descansa {self.time} horas')
    
    def comer(self):
        return f"{self.name} comia con las manos"
    
    def getTotal(self):
        return self._count