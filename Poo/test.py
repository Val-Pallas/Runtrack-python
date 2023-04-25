class Livre:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.disponible = True
    
    def droites(self, author, pages):
        self.author = author
        self.pages = pages
        
    def get_author(self):
        return self.author
    
    def get_pages(self):
        return self.pages
    
    def set_author(self, author):
        self.author = author
    
    def set_pages(self, pages):
        self.pages = pages
    
livre = Livre("Juan salvador Gaviota", 120)

print(livre.title)
print(livre.pages)

livre.author = "Richard Bach"
print(livre.author)

livre.set_pages(150)
print(livre.get_pages())

