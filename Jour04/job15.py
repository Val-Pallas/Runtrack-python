"""Écrivez un programme Python qui arrondi les nombres de la liste [22.4, 4.0,
16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]"""

#nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
#print(round(nombres))

nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
nombres_arrondis = [round(nombre) for nombre in nombres]
print(nombres_arrondis)