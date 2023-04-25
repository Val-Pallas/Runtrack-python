
from job07 import Livre

class Livre:
    def __init__(self, disponible):
        self.__disponible = disponible
        
    def stock(self, n):
        self.__disponible += n
        
    def get__disponible(self):
        return self.__disponible
        
    def emprunter(self):
        if self.__disponible > 0:
            self.__disponible -= 1
            return True
        else:
            return False

livre = Livre(5)

print("there are :", livre.get__disponible(), "livres available")

if livre.emprunter():
    print("You have borrowed a livre")
else:
    print("There are no livres available to borrow")
    
#print("you take :", livre.get_disponible(), "livre/s available")
print("you take :", livre.get__disponible(), "livres available")

