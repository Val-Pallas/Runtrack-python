"""Écrivez un programme Python pour supprimer les doublons de la liste
[10,20,30,20,10,50,60,40,80,50,40]."""

#del numbres[3]
#print(numbres)

uniques = [10,20,30,20,10,50,60,40,80,50,40]
for numbres in uniques :
    while(uniques.count(numbres) > 1) :
        uniques.remove(numbres)
print (uniques)

