#Créer une fonction avec 3 paramètres correspondant à trois longueurs a, b, c. À l'aide de
#ces trois longueurs, déterminer s'il est possible de construire un triangle. Déterminer
#ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque. Attention : un
#triangle rectangle peut être isocèle.
def triangle( a, b, c):
    if a == b == c :
        return "equilateral"
    elif a == b or b == c or c == a:
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return ("rectangle isoceles")
        else:
            return("isocele")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return "saclene(rectangle)"
    else:
        return "you are quelconque"   
print(triangle(4, 5, 5))
print(triangle(5, 5, 5))
print(triangle(3, 5, 6))