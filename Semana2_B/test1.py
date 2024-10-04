class Animal:
    pais = 'Ecuador'
    ### Constructor
    def __init__(self, ecosistema):
        self.ecosistema = ecosistema
        self.pais = self.pais


pez = Animal('Terrestre')

print(pez.ecosistema)
print(pez.pais)


