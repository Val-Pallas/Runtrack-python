"""Créer une classe “Rectangle” avec comme attribut privé longueur et largeur. Créer la
méthode “périmètre” permettant de calculer le périmètre du rectangle ainsi que la
méthode “surface“ permettant de calculer la surface du rectangle.
Créer les accesseurs et mutateurs permettant de manipuler les attributs de la classe.
Créer une classe “Parallélépipède“ héritant de la classe Rectangle avec en plus un
attribut hauteur et une autre méthode volume permettant de calculer le volume du
parallélépipède.
Instancier la classe Rectangle et assurez-vous que toutes les méthodes fonctionnent."""

class Rectangle():
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get__longueur(self):
        return self.__longueur
    def set__longueur(self, value):
        return self.__longueur == value
    def get__largeur(self):
        return self.__largeur
    def set__largeur(self, value):
        return self.__largeur == value
    
    def perimetre(self):
        perimetre = 2 *(self.__longueur + self.__largeur)
        return perimetre
    
    def aire(self):
        aire = self.__longueur + self.__largeur
        return aire
    
        #base = float(input("Ecrivez la base du rectangle :"))
        #altura = float(input("Ecrivez l'hauteur du rectangle"))
        #area = base * altura

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        
    def hauteur(self):
        return self.__hauteur
    
    def volumen(self):
        volumen = self.get__longueur() * self.get__largeur() * self.__hauteur
        return volumen        
    
    

rectangle = Rectangle(3,5)
print("Le perimetre su rectangle est : ", rectangle.perimetre())
print("L'aire du rectangle est: ", rectangle.aire())
parallelepipede = Parallelepipede(3, 5, 6)
print("Le perimetre du rectabgle est :", parallelepipede.perimetre())
print("L'area du rectangle est :", parallelepipede.aire())
print("L'hauteur du rectangle est :", parallelepipede.hauteur())
print("Le volumen du parallelipede est :", parallelepipede.volumen())
