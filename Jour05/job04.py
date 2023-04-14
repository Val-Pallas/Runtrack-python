"""Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses
messages. Sa méthode était assez simple : il décalait les lettres de 3 rangs dans
l'alphabet.
Créer une fonction à laquelle on donne un message et un décalage, et la fonction
renvoie alors le message décalé dans l'alphabet. Il faudra gérer le dépassement ('z'
décalé vers la droite revient sur 'a', et 'a' décalé vers la gauche revient sur 'z')."""


"""def tri_par_insertion (tab) :
 for j in range(1,len(tab)) :
 tab[j] = [1,2,3,4]
 elt_a_placer = tab[j]
 i = j – 1
 while i >= 0 and tab[i] > elt_a_placer :
 tab[i+1] = tab[i]
 i = i – 1
 tab[i+1] = elt_a_placer"""
 
# Fonction de chiffrement/déchiffrement 
def cesar(msg="", clef=0): 
	alphabet="abcdefghijklmnopqrstuvwxyz" 
	chiffre="" 
  
	# On prend chaque lettre du mot (converti en minuscules) 
	for l in msg.lower(): 
		# On recherche la position de la lettre dans l'alphabet 
		pos=alphabet.find(l) 
  
		# Gestion du chiffrement selon la présence ou pas de la lettre 
		chiffre+=alphabet[(pos+clef) % len(alphabet)] if pos != -1 else l 
	# for 
	return chiffre 
# cesar() 
  
message="Hello World !!!" 
chiffre=cesar(message, 6) 
dechiffre=cesar(chiffre, -6) 
print(message, "=>", chiffre, "=>", dechiffre)