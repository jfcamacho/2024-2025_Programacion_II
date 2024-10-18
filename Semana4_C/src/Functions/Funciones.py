class Functions:
    def suma(self, *n):
        resp = 0

        for x in n:
            resp += x

        return resp
    
    def resta(self, a, b):
        return a - b

    def multiplicacion(self, *n):
        resp = 1
        for x in n:
            resp *= x
        
        return resp

    def division(self, a ,b):
        return a/b
    
    def potencia(self, b, e):
        return b**e