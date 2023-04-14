"""Écrire un programme qui créé une liste nommée “L” d’au moins 5 entiers puis
successivement :
- Afficher la valeur de L[1]
- Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
- Puis afficher la valeur du dernier terme de la liste."""


# initialisation de la liste des nombres à saisir
listNombres = []
for i in range(0,5):
    n  = int(input("Tapez la valeur d'un entier : "))
    # ajouter le nombre n à la liste
    listNombres.append(n)
# Afficher la liste des nombres saisis:
print("Voici la liste des nombres saisis : " , listNombres)


L = listNombres

#Afficher la valeur de L[1]
print(L[1])
#Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
L[3] = L[2] + L[4]
print (L)
#Puis afficher la valeur du dernier terme de la liste
print (L[-1])

#------------------

def adition():
    N = [1, 5, 6, 7, 4]
    print(N[1])
    #Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
    N[3] = N[2] + N[4]
    print (N)
    #Puis afficher la valeur du dernier terme de la liste
    print (N[-1]) 
adition()   
