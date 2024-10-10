class Animal:
    ### Constructor
    def __init__(self, ecosistema):
        self.ecosistema = ecosistema
        self.pais = 'Ecuador'
    
    def metodo_1(self):
        print('HA accedido al método 1')
        
    def metodo_1(self):
        print('HA accedido al método 1')


pez = Animal('Terrestre')

print(pez.ecosistema)
print(pez.pais)


