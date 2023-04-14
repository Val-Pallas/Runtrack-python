"""Écrivez un programme Python pour trouver la liste des mots qui sont plus longs que n à
partir d'une chaine de caractères.
Exemple :
my_long_word(3, “ La peur est le chemin vers le côté obscur la peur mène à la colère la
colère mène à la haine la haine mène à la souffrance”)
Output : “peur chemin vers côté obscur peur mène colère colère mène haine haine mène
souffrance”"""

n = 4
my_long_word = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"

new_list = []
text = my_long_word.split(" ")
for x in text:
        if len(x) > n:
                new_list.append(x)
print(new_list)
