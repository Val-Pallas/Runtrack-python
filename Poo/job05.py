"""Créez une classe Animal avec un attribut age initialisé à zéro et prénom initialisé vide
dans son constructeur.
Instancier un objet Animal et écrire en console l’attribut âge. Créer une méthode “vieillir”
qui ajoute 1 à l'âge de l’animal. Faire vieillir votre animal et afficher son âge en console."""

class Animal:
    
    def __init__(self):
        age = 0
        self.age = age
        self.name = "" 
       
    def incrementation(self):
        self.age += 1

    def nommer(self, name):
        self.name = name
        
animal = Animal()    
print("L'age de l'animal :" , animal.age)
animal.incrementation()
print("L'age de l'animal incremente :", animal.age)
animal.nommer("Luna")
print("L'animal se nomme :", animal.name)