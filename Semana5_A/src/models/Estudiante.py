from src.models.Persona import *

class Estudiante(Persona):

    estudiantes = [] 
    id = 0

    def crear(self, idPersona, institucion, matricula):
        Estudiante.id += 1
        persona = super().buscarId(idPersona)
        if persona != 'No existe persona':
            self.personaId = persona["id"]
            self.institucion = institucion
            self.matricula = matricula
            Estudiante.estudiantes.append({
                "id": Estudiante.id,
                "idPersona": self.personaId,
                "institucion": self.institucion,
                "matricula": self.matricula
            })
        else:
            print('Error ', persona)

    def buscarId(self, id):
        for e in Estudiante.estudiantes:
            if e["id"] == id:
                return e
        return 'No existe el estudiante'
    
    def listarEstudiantes(self):
        for e in Estudiante.estudiantes:
            persona = super().buscarId(e["idPersona"])
            print(f'Estudiante {persona["nombre"]} {persona["apellido"]} matriculado en {e["institucion"]} con matricula {e["matricula"]}')
    
    def total(self):
        return len(Estudiante.estudiantes)