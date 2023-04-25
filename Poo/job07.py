class Livre:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.disponible = True
    
    def droites(self, author, pages):
        self.__author = author
        self.__pages = pages
        
    def get__author(self):
        return self.__author
    
    def get__pages(self):
        return self.pages
    
    def set__author(self, author):
        return self.__author
    
    def set__pages(self, pages):
        return self.pages
    
livre = Livre("Juan salvador Gaviota", 120)

print(livre.title)
print(livre.pages)
livre.author = "Garcia Lorca"
print(livre.author)
livre.set__pages(160)
print(livre.get__pages())
    
    
        