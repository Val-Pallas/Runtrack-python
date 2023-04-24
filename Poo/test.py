class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def mesures(self):
        print("Longueur :", self.__longueur)
        print("Largeur :", self.__largeur)
        
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
rectangle = Rectangle(10,23)
rectangle.mesures()
