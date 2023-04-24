"""Créer une classe “Rectangle” avec des attributs privés, “longueur” et “largeur” initialisé
dans le constructeur.
Créer des assesseurs et mutateurs afin de pouvoir afficher et modifier les attributs de la
classe.
Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5. Changer la
valeur de la longueur et de la largeur et vérifier que les modifications soient bien prises
en compte."""

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur #attribut prive
        
        
    def mesures(self):
        print("longeur : ", self.__longueur)
        print("largeur : ", self.__largeur)
        
    def get__longueur(self):
        return self.__longeur
    
    def get__largeur(self):
        return self.__largeur
    
rectangle = Rectangle(10,23)
rectangle.mesures()