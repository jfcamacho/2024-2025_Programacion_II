# Crear clase Persona 
# Generar tres atributos Name, lastName, password

class Persona:
    id = 0
    def __init__(self, name, lastName, password):
        self.id = self.id+1
        self.__name = name
        self.__lastName = lastName
        self.__password = password
        self.__hashPassword()
# Generar métodos GET y métodos Set

    def getId(self):
        return self.id

    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setLastName(self, lastName):
        self.__lastName = lastName

    def getLastName(self):
        return self.__lastName

    def __hashPassword(self):
        import hashlib
        self.setPassword(hashlib.sha256(self.getPassword().encode('utf-8')).hexdigest())
    
    def comparePassword(self, password):
        import hashlib
        newHash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return self.getPassword() == newHash
    


# Generar un objeto de la clase Persona

juan = Persona('Juan', 'Azteca', 'Ju@n123$_')

juan.setName('Carlos')

print(juan.getName())
print(juan.getLastName())
print(juan.comparePassword('Ju@n123$_'))