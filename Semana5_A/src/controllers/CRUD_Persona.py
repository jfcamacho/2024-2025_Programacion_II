from src.models.Persona import *

class CRUD_PERSONA:
    persona = Persona()

    def crear(self, nombre, apellido):
        self.persona.crear(nombre, apellido)

    def total(self):
        return self.persona.total()
    
    def listarPersonas(self):
        self.persona.listarPersonas()
    
    def seederData(self):
        self.persona.crear('Carlos', 'Armijos')
        self.persona.crear('Esther', 'Dominguez')
        self.persona.crear('Gonzalo', 'Enrriquez')
        self.persona.crear('Camilo', 'Samaniego')
        self.persona.crear('Sofia', 'Berrú')