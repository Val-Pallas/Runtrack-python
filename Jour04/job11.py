"""Écrire un programme qui créer la liste d’entiers L = [7, 11, 42, 39, 2], votre programme
devra pouvoir modifier la liste en augmentant de 1 la valeur de chaque élément de la
liste """



#+ 1 c/element de L
#for i in range (0, 12) :
     #print (L[len(L)-1])

def list_augment() :
    L = [7, 11, 42, 39, 2]
    
    for i in range(len(L)):
        L[i]= L[i] + 1
    print (L)
list_augment()

