class Personne():
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("J'ai", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=30):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee


personne = Personne()
eleve = Eleve()
print("L'âge par défaut de l'élève est :", eleve.age)
