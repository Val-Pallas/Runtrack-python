"""Créez une classe Animal avec un attribut age initialisé à zéro et prénom initialisé vide
dans son constructeur.
Instancier un objet Animal et écrire en console l’attribut âge. Créer une méthode “vieillir”
qui ajoute 1 à l'âge de l’animal. Faire vieillir votre animal et afficher son âge en console."""

    #def vieillir(self, other):
     #   result = self.age + other.age
      #  return Animal(result, self.age + other.age)

class Animal:
    def __init__(self, age, pas):
        self.age = age
        self.pas = pas
       
    
    
    def incrementation(self):
        self.age += self.pas

age = 0
    
inc = Animal(age, 1)

print("L'age de l'animal :" , inc.age)
inc.incrementation()
print("L'age de l'animal incremente :", inc.age)

