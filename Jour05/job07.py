"""Créer un programme qui demandera à l’utilisateur de renseigner un mot et un seul, sans
espace ni aucun autre caractère que les 26 lettres de l’alphabet (sans accent ni
majuscule).
Votre programme devra modifier ce mot, en y changeant de place certains caractères
(ou tous) afin de donner un mot plus “loin” dans l’ordre alphabétique que le mot
renseigné par l'utilisateur.
Attention: Le nouveau mot doit être le mot le plus proche possible, dans l’ordre
alphabétique, du mot original !
Par exemple, “abcde” donnerait “abced”. “acedb” est aussi “valide” mais n’est PAS le
plus proche du mot original dans l’ordre alphabétique."""

#in put mot: input seul ("") == lowercase


def mot_decale():
    mot = input("Entrez un mot : ")
    result = ""
    for lettre in mot:
        lettre_decalee = chr(ord(lettre) + 1)
        result += lettre_decalee
    return result

# Example usage:
print(mot_decale())
