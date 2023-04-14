#À partir de la chaîne "abcdefghijklmnopqrstuvwxyz" * 10, écrivez un programme qui
#récupère et affiche autant de caractères que possible de cette chaîne sous forme de
#suite pyramidale.

    
chaine="abcdefghijklmnopqrstuvwxyz" * 10 
  
# Initialisation indice de croissance 
i=1 
  
# Tant que l'indice de croissance (nb de caractères à afficher) est contenu dans les caractères restants 
while i <= len(chaine): 
	# On affiche les "i" premiers caractères 
	print(chaine[:i]) 
  
	# On ne garde ensuite que les caractères restants à afficher 
	chaine=chaine[i:] 
  
	# On incrémente l'indice de croissance 
	i+=1 