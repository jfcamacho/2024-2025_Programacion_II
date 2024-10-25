class Persona:
    personas = []
    id = 0

    def crear(self, nombre, apellido):
        Persona.id += 1
        self.nombre = nombre
        self.apellido = apellido
        Persona.personas.append({
            "id": Persona.id,
            "nombre": self.nombre, 
            "apellido": self.apellido
            })
    
    def total(self):
        return len(Persona.personas)

    def listarPersonas(self):
        for p in Persona.personas:
            print(f'Persona {p["id"]} {p["nombre"]} {p["apellido"]}')
    

    def buscarId(self, id):
        for p in Persona.personas:
            if p["id"] == id:
                return p
        return 'No existe persona'