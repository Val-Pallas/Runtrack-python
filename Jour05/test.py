"""rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")"""
    
"""x = int(input(" X width: "))
#y = int(input(" Y height: "))
print("diagonal_triangle : ") """
   
"""# Fonction de chiffrement/déchiffrement 
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
  
message="`me gustan las naranjas!!!" 
chiffre=cesar(message, 6) 
dechiffre=cesar(chiffre, -6) 
print(message, "=>", chiffre, "=>", dechiffre)"""


