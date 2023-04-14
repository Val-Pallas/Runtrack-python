#Créez une fonction nommée “Add”. Cette fonction devra prendre 2 nombres entiers en
#paramètres et afficher la somme de ces 2 entiers.
#Depuis votre programme, appelez cette fonction plusieurs fois en y passant des
#paramètres différents pour afficher ces résultats.

def add(num1, num2):
  print(num1+num2)

add(1,3)
add(4,5)

#________

def add(numbers):
  return sum(numbers)
  
numbers = [1, 2, 3, 4, 5]
  
numbers = [1, 2, 3, 4, 5, 7, 10]
print(add(numbers))

print(add)()



