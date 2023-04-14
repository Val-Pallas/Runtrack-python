#Écrire un programme qui itère les nombres entiers de 1 à 100. Pour les multiples de
#trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz". Pour
#les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".

for num in range(1, 101):
    if num%3==0 and num%5==0:
        print('FizzBuzz', num) 
    elif num % 3 == 0:
        print('Fizz', num) 
    elif num % 5==0:
        print('Buzz', num) 
    else:
        print(num)



#if value x == any value in list y: python