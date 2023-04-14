
"""Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de n+1
lignes/n+1 colonnes traversé par une diagonale."""

"""rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")"""
    
x = int(input(" Taille: "))
#y = int(input(" Y height: "))
print("Tapis : ") 
   
#y = (int(input(" Y height: ")))
#for i in range(x):
    #if i == 0 or i == x -1 :
print("+" + "-"* x + "+" )
    #else:
for j in range(x):
            #if j == 0 or j == x -1:
                #j == j+1 and x/j+1  
            print("|" + "#"* (x -1 -j) + " "+ "#"* j + "|" ) 
print("+" + "-"* x + "+" )  
        
       

  

 
    
 