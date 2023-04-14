"""Luke Skywalker, un professeur de Math, fait passer un test et décide de noter ses élèves
sur une échelle allant de 0 à 100 inclus.
Si un étudiant obtient moins de 40 sur 100, il échoue au test.
S'il a plus de 40, il réussit le test. Luke est un professeur fort sympathique et décide
donc d’arrondir à la hausse les notes des étudiants ayant réussi le test. Mais Luke n’est
quand même pas trop gentil. Cet arrondi à la hausse ne bénéficiera qu’aux étudiants
remplissant certains critères, car tout de même, il ne faut pas exagérer, sans blague.
Le critère est simple : Si un étudiant a eu une note de moins de strictement 3 points de
son prochain multiple de 5, alors sa note est arrondie à ce multiple de 5. Par exemple,
un 83 sera arrondi à 85 alors qu’un 82 restera un 82.
Pour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre une liste
de notes et qui renvoie une liste de notes, arrondies comme il se doit, quand cela est
nécessaire."""
# <40 == echoue 
# >40 == reussit (arrondi a la hausse)
#arrondi a la hausse == 


            
notes = [65, 83, 72, 38, 91, 93]

def arrondir_notes(notes):
    arrondis = []
    for note in notes:
        if note >= 40:
            multSup5 = note + (5 - note % 5) if note % 5 >= 2 else note
            arrondis.append(multSup5)
        else:
            nOmultSup5 = note - (5 - note % 5) if note % 5 >= 2 else note
            arrondis.append(nOmultSup5)
    return arrondis

arrondis = arrondir_notes(notes)
print(arrondis)  # Output: [65, 85, 70, 40, 90, 95]



