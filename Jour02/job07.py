#Créez une fonction qui prend en paramètre une String nommée “langage”.
#Si la valeur de “langage” est égal à “javascript” affichez “tu es un developpeur web”
#Sinon si la valeur de “langage” est égal à “python” affichez “tu es un developpeur IA”
#Sinon si la valeur de “langage” est égal à “java” affichez “tu es un developpeur logiciel”
#Sinon si la valeur de “langage” est égal à “reactjs” affichez “tu es un developpeur mobile”
#Sinon, affichez “un jour, je serai le meilleur developpeur... ”

def element(langage):
    if langage == "javascript":
        return "tu es una developpeur web"
    elif langage == "python":
        return "tu es una developpeur IA"
    elif langage == "java":
        return "tu es un developpeur logiciel"
    elif langage == "reactjs":
        return "tu es una developpeur mobile"
    else:
        print("un jour, je serai le meilleur developpeur...")
        
print(element("javascript"))
print(element("python"))
print(element("java"))
print(element("reactjs"))
       