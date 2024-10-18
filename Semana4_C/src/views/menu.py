class Menu:
    def main_menu(self):
        # print('This is the main menu')
        print('--------- Operaciones Basicas ---------')
        print('1.- Suma')
        print('2.- Resta')
        print('3.- Multiplicacion')
        print('4.- Division')
        print('5.- Potencia')
        print('10.- Salir')
        return int(input('Ingrese un valor.: '))
    
    def sub_menu(self):
        print('This is a sub menu')
        return 0