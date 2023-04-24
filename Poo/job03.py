"""Modifier votre classe “Operation” afin d’y ajouter la méthode addition. Cette méthode
additionne “nombre1” et “nombre2” et affiche en console le résultat."""

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __add__(self, other):
        result = self.nombre1 + other.nombre1
        return Operation(result, self.nombre2 + other.nombre2)

operation1 = Operation(12, 3)
operation2 = Operation(8, 4)
result = operation1 + operation2
print(result.nombre1) # 20
print(result.nombre2) # 7