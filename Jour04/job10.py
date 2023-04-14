"""Écrire un programme qui calcule le produit de toutes les valeurs de la liste comprises
dans l’intervalle [25, 90]
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]"""

def sum_list() :
    sumparcial = 0
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    longueur = len(L)
    for i in range(longueur) :
        sumparcial = sumparcial + L[i]
    return sumparcial
print(sum_list())
    
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(L[25:90]) 

"""Additionally, the syntax to slice a list and calculate 
the sum of its elements is incorrect. 
You need to first slice the list using the syntax 
L[start_index:end_index] to get the desired portion of the list, 
and then use the sum() function to calculate the sum of the 
sliced elements."""
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print(L[2:9])  # This will print the slice of the list from index 2 to 8

suminterval = sum(L[2:9])# This will calculate the sum of the sliced elements
print(suminterval)# This will print the sum of the sliced elements

