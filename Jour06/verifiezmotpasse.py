majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chiffres = '0123456789'
 
nb_essais = 2
confirm = False
while not confirm and nb_essais > 0:
    mdp = input("entrez un mdp: ")
    if len(mdp) >= 8 and True in (car in majuscules for car in mdp) and \
       (car in chiffres for car in mdp):
        if input("réentrez le mot de passe pour vérifier: ") == mdp:
            confirm = True
    nb_essais -= 1