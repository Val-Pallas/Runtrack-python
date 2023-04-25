class Vehicule():
    def __init__(self, marque, anne, prix):
        self.marque = marque
        self.anne = anne
        self.prix = prix
        
    def informationDuVehicule(self, model):
        #self.model = model
        pass
    
class Voiture(Vehicule):
        def __init__(self, marque, model, anne, prix, portes):
             super().__init__(marque, anne, prix)
             self.model = model
             self.portes = portes
             
        def informationDuVehicule(self):
            return f"{self.marque} {self.model} {self.anne} {self.prix} {self.portes}"
             
        
voiture = Voiture("Mercedes","classe A", 2020, 18500, 4)
print(voiture.informationDuVehicule())