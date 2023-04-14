#Créez une fonction qui prend 2 paramètres :
#- Le premier reçoit un String nommé “type”
#- Le second reçoit un String nommé “saison”
#Si la valeur de “type” est égal à “fruits” et que celle de saison est égal à “hiver”, affichez
#“orange, mandarine et kiwi”
#Si la valeur de “type” est égal à “fruits” et que celle de saison est égal à “ete”, affichez
#“Poire, fraise, cassis”
#Si la valeur de “type” est égal à “legume” et que celle de saison est égal à “hiver”,
#affichez “carotte, topinambour, endive”
#Si la valeur de “type” est égal à “legume” et que celle de saison est égal à “ete”, affichez
#“artichaut, aubergine,navet”

def element(type, saison):
    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    if type == "fruits" and saison == "ete":
        return "Poire, fraise, cassis"
    if type == "legume" and saison == "hiver":
        return "carotte, topinambour, endive"
    if type == "legume" and saison == "ete":
        return "artichaut, aubergine,navet"
    else:
        print("no saison no fruit")
    
print(element("fruits", "hiver"))
print(element("legume", "hiver"))
print(element("legume", "printemps"))