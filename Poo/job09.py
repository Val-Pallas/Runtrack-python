class Student():
    def __init__(self, nom, prenom, numemro):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numemro
        self.__montant = 0
        
        
    def addCredits(self, montant):
        self.__montant += montant
        if self.__montant > 0:
            print("You can be evaluated")
        return True
    
    
    def studentEval(self, resultat):
        self.__resultat = resultat
        if self.__resultat >= 90:
            print("Excellent")
        elif self.__resultat  >= 80 <= 90:
            print("Tres bien")
        elif self.__resultat  >= 70 <= 80:
            print("Bien")
        elif self.__resultat  >= 60 <= 70:
            print("Suffisant")
        else:
            if self.__resultat >90:
                print("insufissant")
                
    def get__resultat(self):
        return self.__resultat
    
    def get__montant(self):
        return self.__montant
    
    def get__nom(self):
        return self.__nom
    
    def studentInfo(self):
        return("Student: ", self.__nom, self.__prenom, self.__numero , "niveau: ", self.__montant)
        
student = Student("John", "Doe", 60)      
print(student.studentInfo())
