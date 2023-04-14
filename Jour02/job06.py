#Créez une fonction qui prend en paramètre un nombre nommé “nombre”.
#Afficher “positif” si le nombre est supérieur à 0
#Afficher “negatif” si le nombre est inférieur à 0
#appelez cette fonction plusieurs fois en y passant des paramètres différents pour
#afficher ces résultats.

def element(nombre):
    if nombre > 0:
        return "positif"
    elif nombre < 0:
        return "negatif"
    else:
        return("cero is a number neutro")

print(element(4))
print(element(9))
print(element(-4))
print(element(-19))
print(element(0))
