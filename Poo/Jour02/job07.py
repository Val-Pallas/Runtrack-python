import random
from tkinter import*


class Carte():
    def __init__(self, tirage):
        self.tirage = tirage
    #carte aleatoire et la sort du jeu
    def tirage(self, jeu, carte):
        self.jeu = jeu
        self.carte = carte
        if len(jeu) == 0:
            print("Le jeu est vide")
        z = random.randit(0, len(jeu) -1)
        caret = jeu[z]   
        jeu.pop(z)
        return carte 
    #definir ce aue faite la banque durant le tour
    def banque(self, main, calcul_main):
        self.main = main
        self.calcul_main = calcul_main
        s = calcul_main(main)
        while s < 17:
            carte = tirage()
            print("La banque tire une carte")
            main.append(carte)
            print(main)
            s = calcul_main(main)
        return S
    
class Jeu():
    # L'utilisateur veux une carte ou non
    def __init__(self, choix_jouer, joueur): 
        self.choix_jouer = choix_jouer
        self.joueur = joueur
        print("\n\nC'est a", joueur[0], "de jouer")
        continuer = True
        super(s = calcul_main(joueur[2]))
        if s == 1:
            continuer = False
        while continuer == True and s < 21:
            reponse = input("Voulez-vous prendre une autre carte ? [o/n] ")
            reponse = reponse.strip().lower()
            if reponse.startswith('o'):
                carte = tirage()
                print("Voici votre carte:")
                print(carte)
                joueur[2].append(carte)
                s = calcul_main(joueur[2])
            elif reponse.startswith('n') or reponse == '':
                continuer = False
            else:
                print("Répondez par 'o' ou 'n'")
        return joueur

           
def calcul_main(main):  # On calcule la valeur de la main
    somme = 0
    AS = []
    for item in main:
        if item[0] == '1':
            val = 11
            AS.append(1)
        if item[0] == '2':
            val = 2
        if item[0] == '3':
            val = 3
        if item[0] == '4':
            val = 4
        if item[0] == '5':
            val = 5
        if item[0] == '6':
            val = 6
        if item[0] == '7':
            val = 7
        if item[0] == '8':
            val = 8
        if item[0] == '9':
            val = 9
        if item[0] == '0':
            val = 10
        if item[0] == 'J':
            val = 10
        if item[0] == 'Q':
            val = 10
        if item[0] == 'K':
            val = 10
        somme = somme + val
    if somme == 21 and len(main) == 2:
        print("Black Jack!")
        return (1)
    if somme > 21:
        somme = somme - 10 * len(AS)
    if somme > 21:
        print("Vous avez dépassé 21, vous avez donc perdu.")
        return somme
    print("Votre main a une valeur de :", somme)
    return somme
 
 
def tour_jeu(): #Montre le pactole de chaque joueur et lui demande combien veut-il miser
    table = []
    for i in range(joueurs):  # Création des mains
        main = []
        print(nom_joueur[i], "a un pactole de :", pactole_joueur[i])
        mise = -1
        while 0 > mise or mise > pactole_joueur[i]: #Empeche l'utilisateur de mettre une valeur en dessous de 0 et au dessus de son pactole
            mise = int(input("\nCombien voulez vous miser ? "))
        for ite in range(2):
            carte = tirage()
            main.append(carte)
        temp_joueur = [nom_joueur[i], pactole_joueur[i] - mise, main, mise]
        table.append(temp_joueur)
    print(table)
 
    main_banque = [tirage()]
    print("La carte visible de la banque est : ", main_banque)
    for i in range(joueurs):  # Jeu de la carte
        temp_joueur = choix_joueur(table[i])
        table[i] = temp_joueur
    print(table)
 
    # Tour de la banque
    
    carte = tirage()
    main_banque.append(carte)
    val_banque = banque(main_banque)
    print("La banque a une main de valeur :", val_banque)
 
    for i in range(joueurs):  # Qui a gagné ?
        val_joueur = calcul_main(table[i][2])
        if val_joueur > 21:
            print(table[i][0], "a dépassé 21 et a donc perdu")
        elif val_joueur == 1 and val_banque != 1:
            print(table[i][0], "a eu un Black Jack!")
            table[i][1] = table[i][1] + table[i][3] * 2.5
        elif val_joueur == 1 and val_banque == 1:
            print(table[i][0], "a eu un Black Jack en même temps que la banque")
            table[i][1] = table[i][1] + table[i][3]
        elif val_joueur != 1 and val_banque == 1:
            print(table[i][0], "a perdu face au Black Jack de la banque!")
        elif val_banque > 21:
            print(table[i][0], "a gagné car la banque a dépassé 21")
            table[i][1] = table[i][1] + table[i][3] * 2
        elif val_joueur > val_banque:
            print(table[i][0], "a gagné sur la banque")
            table[i][1] = table[i][1] + table[i][3] * 2
        elif val_joueur == val_banque:
            print(table[i][0], "a fait égalité avec la banque")
            table[i][1] = table[i][1] + table[i][3]
        elif val_joueur < val_banque:
            print(table[i][0], "a perdu face à la banque")
        else:
            print('Bizarre si ca arrive revoir la ligne 142 a peu près')
        pactole_joueur[i] = table[i][1]
    return table
 
 
def melange(jeu_donne, nb):
    talon = []
    for _ in range(nb):
        talon += jeu_donne
    return talon
 
 
def recup():
    global joueurs, num_q, pactole_depart
    if num_q==1 :
        joueurs=int(entree.get())
        texte_question.set("Quel est le pactole initial?")
        texte.set("")
        num_q=2
    elif num_q==2 :
        pactole_depart=int(entree.get())
        texte_question.set("Quel est le nom du joueur 1?")
        texte.set("")
        num_q=3
    elif num_q==3 :
        #if len(nom_joueur<joueurs) :
        if len(nom_joueur) < joueurs:
    # Do something

            nom_joueur.append(entree.get())
            pactole_joueur.append(pactole_depart)
        else :
            pass
 
 
 
# Construction de la fenêtre principale «root»
root = Tk()
root.title('Black Jack')
 
photo = PhotoImage(name="balance.jpeg")
#photo = PhotoImage(file="/path/to/balance.jpeg")
Largeur = 1000
Hauteur = 504
Canevas = Canvas(root,width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0,anchor=NW, image=photo)
print("Image de fond (item",item,")")
Canevas.pack()
texte=StringVar()
texte_question=StringVar()
texte_question.set("Combien de joueurs?")
question=Label(root,textvariable=texte_question)
question.pack(side=LEFT)
entree=Entry(root, textvariable=texte)
entree.pack(side=LEFT)
ok=Button(root, text="OK", command=recup)
ok.pack(side=LEFT)
num_q=1
joueurs=0
pactole_depart=0
nom_joueur = []
pactole_joueur = []
jeu_initial = ['1T', '2T', '3T', '4T', '5T', '6T', '7T', '8T', '9T', '0T', 'JT', 'QT', 'KT', '1C', '2C', '3C', '4C',
               '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC', '1P', '2P', '3P', '4P', '5P', '6P', '7P', '8P',
               '9P', '0P', 'JP', 'QP', 'KP', '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD',
               'KD']
affichage={'1T':"1.gif", '1P':"2.gif", '1C':"3.gif", '1D':"4.gif", '2T':"5.gif", '2P':"6.gif", '2C':"7.gif", '2D':"8.gif", '3T':"9.gif", '3P':"10.gif", '3C':"11.gif", '3D':"12.gif", '4T':"13.gif", '4P':"14.gif", '4C':"15.gif", '4D':"16.gif", '5T':"17.gif", '5P':"18.gif", '5C':"19.gif", '5D':"20.gif", '6T':"21.gif", '6P':"22.gif", '6C':"23.gif", '6D':"24.gif", '7T':"25.gif", '7P':"26.gif", '7C':"27.gif", '7D':"28.gif", '8T':"29.gif", '8P':"30.gif", '8C':"31.gif", '8D':"32.gif", '9T':"33.gif", '9P':"34.gif", '9C':"35.gif", '9D':"36.gif", '0T':"37.gif", '0P':"38.gif", '0C':"39.gif", '0D':"40.gif", 'JT':"41.gif", 'JP':"42.gif", 'JC':"43.gif", 'JD':"44.gif", 'QT':"45.gif", 'QP':"46.gif", 'QC':"47.gif", 'QD':"48.gif", 'KT':"49.gif", 'KP':"50.gif", 'KC':"51.gif", 'KD':"52.gif"}
nombre_jeux = 2
# Lancement de la «boucle principale»
root.mainloop()
 
 
 
 
#print("Combien de joueurs pour cette partie ?")  # Création des joueurs
#joueurs = int(input())
 
# print("Quelle est le pactole inital ?")
# pactole_depart = int(input())
 
# for ite in range(joueurs):
#     print("\nNom du joueur numéro ", ite + 1)
#     temp_name = input()
#     nom_joueur.append(temp_name)
#     pactole_joueur.append(pactole_depart)
 
continuer = True
while continuer:
    jeu = melange(jeu_initial, nombre_jeux)
    print(jeu)
    table = tour_jeu()
    joueurs_elimines = []
    for i in range(joueurs):
        if table[i][1] == 0:
            print(table[i][0], "est éliminé de cette partie.")
            joueurs_elimines.append(i)  # on liste tous les joueurs éliminés
    joueurs_elimines.reverse()  # on inverse la liste pour commencer a supprimer par la fin (pb d'indices)
    if len(joueurs_elimines) == joueurs:  # Vérification de fin de la partie
        continuer = False
        print('La banque a gagné ! Fin de la partie')
    else:
        for item in joueurs_elimines:  # Suppression des joueurs éliminés
            joueurs -= 1  # réduction du nombre de joueurs
            table.pop(item)  # suppression de la liste joueur dans la table
            nom_joueur.pop(item)  # suppresion du nom du joueur (pour ne pas recréer dans tour_jeu())
            pactole_joueur.pop(item)  # suppresion du pactole du joueur (pour ne pas recréer dans tour_jeu())
        reponse = input("Voulez-vous continuer de jouer ? [o/n] ")
        reponse = reponse.strip().lower()
        if reponse.startswith('o'):
            print("\n\n\tNouvelle mise !")
        elif reponse.startswith('n') or reponse == '':
            continuer = False
        else:
            print("Répondez par 'o' ou 'n'")