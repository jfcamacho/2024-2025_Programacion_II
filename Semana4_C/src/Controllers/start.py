from src.views.menu import *
from src.Controllers.operations import *

class Start:
    def start(self):
        i = 0
        menu = Menu()
        operations = Operations()
        while True:
            i = menu.main_menu()
            if i == 10:
                break
            operations.selectedOperation(i)
            # menu.sub_menu()