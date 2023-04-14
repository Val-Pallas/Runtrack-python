"""Écrire un programme qui trie dans l’ordre croissant une liste passés en paramètre."""

"""L = [8, 24, 48, 2, 16]
long = len(L)

#affiche à l'envers
p = 1
print ("Affichage à l'envers :")
for i in range (long) :
     print (L[long-1-i], ',', end=" ")"""

colors = ['pink', 'blue', 'white', 'black','think', 'clue', 'zhite', 'flack', ]
colors.sort()
print(colors)


def liste_croissante(colors):
    for i in range(len(colors)-1):
        if colors[i] > colors[i+1]:
            return False
    return True
