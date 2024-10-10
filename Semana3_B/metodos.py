class Acciones:
    def crear(self, arr, user):
        arr.append(user)
        return arr

    def listar(self, arr, name):
        for user in arr:
            if(user.getName().lower() == name.lower()):
                print(user.id, user.getName() + ' ' + user.getLastName())
    
    def modificar(self, arr, id, newUser):
        newArr = []
        for user in arr:
            if user.id == id:
                newArr.append(newUser)
            else:
                newArr.append(user)
        return newArr
