#Créez une fonction qui affiche tous les nombres de 0 à 100 compris SAUF 26, 37, 88

  
#mon_objet_range = range(0, 100) # 0 1 2 3

#print(mon_objet_range![26,37,88]) # 1


list = [26, 37, 88]
for i in range(101):
  if i not in list  :
   print(i) 
  
for i in range(0, 101):

    if i == 26 or i == 37 or i == 88:
      continue 
print(i)

