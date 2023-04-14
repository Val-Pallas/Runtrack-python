"""Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en
fonction des paramètres d’entrées, (width, height), par exemple :
draw_rectangle(10, 3)"""


"""print("|" * y + "#" * x)
 print("-" * y +" ")"""

x = int(input(" X width: "))
y = int(input(" Y heigth: "))
print("draw_rectangle : ")        

for i in range(x):
    if i == 0 or i == x -1 :
        print("|" + "-"* y + "|" )
    else:
        print("|" + " "* y + "|" )
   
   

   
    

                

    
      