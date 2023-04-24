"""valeurs par défaut. Instancier votre première classe et imprimer l’objet en console."""

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def chiffre1(self):
        print("Chiffre1 :", self.nombre1)

    def chiffre2(self):
        print("Chiffre2 :", self.nombre2)
        

operation = Operation(1,2)
operation.chiffre1()
operation.chiffre2()