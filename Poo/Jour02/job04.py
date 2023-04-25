class Forme():
    def __init__(self):
        self.aire = 0
        
    def calculer_aire(self):
        pass

class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        super().__init__()
        self.largeur = largeur
        self.longueur = longueur
        self.calculer_aire()
        print("Rectangle:", self.largeur,"largeur,", self.longueur,"longeur, aire:", self.aire)
 
    def calculer_aire(self):
        self.aire = self.largeur * self.longueur
    
rectangle = Rectangle(2,5)
    
    
    
    
    
    
        
    