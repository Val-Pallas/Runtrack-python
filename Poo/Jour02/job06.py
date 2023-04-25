class Vehicule():
    def __init__(self, marque, anne, prix):
        self.marque = marque
        self.anne = anne
        self.prix = prix
        
    def informationDuVehicule(self, model):
        #self.model = model
        pass
    
    def demarrer(self):
        print("Brum Brum")
    
class Voiture(Vehicule):
        def __init__(self, marque, model, anne, prix, portes):
             super().__init__(marque, anne, prix)
             self.model = model
             self.portes = portes
             
        def informationDuVehicule(self):
            return f"{self.marque} {self.model} {self.anne} {self.prix} {self.portes}"

class Moto(Vehicule):
    def __init__(self, marque, model, anne, prix, roues):
             super().__init__(marque, anne, prix)
             self.model = model
             self.roues = roues
             
    def informationDuVehicule(self):
            return f"{self.marque} {self.model} {self.anne} {self.prix} {self.roues}"

        
voiture = Voiture("Mercedes","classe A", 2020, 18500, 4)
print(voiture.informationDuVehicule())
print(voiture.demarrer())
moto = Moto("Yamaha", "1200 Vamx" , 1987, 4500, 2)
print(moto.informationDuVehicule())
moto.demarrer()