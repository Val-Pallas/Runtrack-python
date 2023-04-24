"""À l’aide de la classe “Operation” crée au-dessus, imprimer en console la valeur des
attributs “nombre1” et “nombre2”."""

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def chiffre1(self):
        print("Chiffre1 :", self.nombre1)

    def chiffre2(self):
        print("Chiffre2 :", self.nombre2)
        

operation = Operation(12,3)
operation.chiffre1()
operation.chiffre2()