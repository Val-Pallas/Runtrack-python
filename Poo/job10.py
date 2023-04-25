"""Créer une classe “Voiture” qui a pour attributs privés une marque, un modèle , une
année, un kilométrage et un attribut nommé “en_marche” initialisé à défaut sur False.
Cette classe doit posséder des mutateurs et assesseur pour chaque attribut.
Créer une méthode “demarrer” qui change la valeur de l’attribut “en_marche” en True,
une méthode “arreter” qui change la valeur de l’attribut “en_marche” en False.
Ajouter à la classe “Voiture” l’attribut privé “reservoir” qui est initialisé à 50 par défaut
dans le constructeur. Créer une méthode privée “verifier_plein” qui retourne la valeur de
l’attribut “reservoir”. Cette méthode est appelée dans la méthode “demarrer” . Si la
valeur du reservoir est supérieur à 5 la voiture peut demarrer.

Sur vos scripts doit apparaître l’ensemble des méthodes appelées tout au long des
exercices."""

class Voiture():
    def __init__(self, marque, modele, anne, quilometrage, en_marche, reservoir):
        self.__marque = marque
        self.__modele = modele
        self.__anne = anne
        self.__quilometrage = quilometrage
        self.__en_marche = True
        self.__reservoir = 50
    
    def get_marque(self):
        return self.__marque

    def set_marque(self, value):
        self.__marque = value
        
    def get_modele(self):
        return self.__modele

    def set_modele(self, value):
        self.__modele = value
        
    def get_anne(self):
        return self.__anne

    def set_anne(self, value):
        self.__anne = value
        
    def get_quilometrage(self):
        return self.__quilometrage

    def set_quilometrage(self, value):
        self.__quilometrage = value
        
    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, value):
        self.__en_marche = value
        
    def get_reservoir(self):
        return self.__reservoir

    def set_reservoir(self, value):
        self.__reservoir = value

    def demarrer(self):
        if not self.__en_marche:
            if self.__reservoir > 5:
                self.__en_marche = True
                self.__reservoir -= 5
                return "La voiture a démarré"
            else:
                return "La voiture n'a pas assez d'essence pour démarrer"
        else:
            return "La voiture est déjà en marche"

    def arreter(self):
        if self.__en_marche:
            self.__en_marche = False
            return "La voiture a été arrêtée"
        else:
            return "La voiture est déjà arrêtée"

    def __verifier_plein(self):
        if self.__reservoir < 5:
            return False
        else:
            return True
    
    def voitureInfo(self):
        return("voiture: ", self.__marque, self.__modele, self.__anne , self.__quilometrage, self.__en_marche, self.__reservoir)
    
voiture = Voiture("Ford", "Mustang", 1964, 100.000, True, 15)
print(voiture.voitureInfo() )  # output: Ford