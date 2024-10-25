from src.models.Persona import *
from src.models.Estudiante import *

class CRUD_ESTUDAINTE:

    estudiante = Estudiante()

    def crear(self, persona, institucion, matricula):
        self.estudiante.crear(persona, institucion, matricula)

    def total(self):
        return self.estudiante.total()
    
    def listarEstudiantes(self):
        self.estudiante.listarEstudiantes() 