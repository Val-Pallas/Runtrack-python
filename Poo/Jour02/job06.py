class Vehicule():
    def __init__(self, marque, anne, prix):
        self.marque = marque
        self.anne = anne
        self.prix = prix
        
    def informationDuVehicule(self, model):
        self.model = model
        return f"{self.marque} {self.model} {self.anne} {self.prix}"
        
vehicule = Vehicule("Mercedes", 2020, 18500)
print(vehicule.informationDuVehicule("classe A"))