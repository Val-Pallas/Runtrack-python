#Créez une fonction nommée “calcule” qui prend 3 paramètres :
#● le premier, “num1”, est un nombre,
#● le deuxième, "operator", est un caractère (string) contenant le type d’opération
#(+, -, *, /, %),
#● le troisième, “num2”, est un nombre.
#La fonction doit retourner le résultat de l’opération.

def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        print('You have not typed a valid operator, please run the program again.')
    

print(calcule(2, "+", 5))
print(calcule(34, "/", 5))

