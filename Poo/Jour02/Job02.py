from job01 import Personne

class Student(Personne):
    def ecole(self):
        print("Je vais en cours")
    def dite_age(self):
        print("en fait non! j'ai bien", self.age+1, "ans")

    
e = Student(14)
e.dite_age()

