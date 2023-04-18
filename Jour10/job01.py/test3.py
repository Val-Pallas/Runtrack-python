def afficher_plateau(plateau):
    print("  ", end="")
    for j in range(3):
        print(j, end=" ")
    print()
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(plateau[i][j], end=" ")
        print()

def verifier_victoire(plateau):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != " ":
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != " ":
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != " ":
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != " ":
        return True
    return False

def jouer():
    plateau = [[" " for j in range(3)] for i in range(3)]
    joueur = "X"
    while not verifier_victoire(plateau):
        afficher_plateau(plateau)
        print("C'est au tour du joueur", joueur)
        ligne = int(input("Entrez le numéro de ligne : "))
        colonne = int(input("Entrez le numéro de colonne : "))
        if plateau[ligne][colonne] != " ":
            print("Case occupée ! Veuillez choisir une autre case.")
            continue
        plateau[ligne][colonne] = joueur
        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"
    afficher_plateau(plateau)
    print("Le joueur", joueur, "a gagné !")

jouer()
