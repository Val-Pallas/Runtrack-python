from job04 import Forme

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        self.calculer_aire()
        print("Radius:", radius,"longeur, aire:", self.aire)
 
    def calculer_aire(self):
        self.aire = self.radius * 3.14
        
cercle = Cercle(6)