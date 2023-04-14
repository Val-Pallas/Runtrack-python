"""Écrire un programme qui calcule la somme de toutes les valeurs paires de la liste
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]"""

"""L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
paires = len(L)
p = 0
for i in range(paires) :
    if L[i] % 2 == 0 :
        p = p + 2
    print("Je suis un numbre entier : ", p)"""



L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
long = len(L)

#somme des valeurs paires de L
somp = 0
for i in range (long) :
     if L[i] %2 == 0 :
          somp = somp + L[i]
print ("Somme des valeurs paires : ", somp)

"""L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
sum = sum(L)
print (sum)"""

