"""Créer un programme qui permet de gérer les mots de passe renseigné par l’utilisateur
en enregistrant les mots de passe hachés dans un fichier.
Le programme doit pouvoir permettre à l’utilisateur d’ajouter de nouveaux mots de
passe ou d’afficher ces derniers.
Pour ce bonus, il est nécessaire d’utiliser la bibliothèque “Json” de python."""

import json
import os
import random
import hashlib

# Définir le nom du fichier JSON
file_name = 'job02_my_passwords.json'

# Vérifier si le fichier existe et le charger
if os.path.isfile(file_name):
    with open(file_name, 'r') as file:
        passwords = json.load(file)
else:
    passwords = {}

# Définir les caractères pour la génération de mot de passe
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:<>,.?/~`'

# Demander les informations pour un nouveau mot de passe
new_password = {}
new_password['name'] = input("Nom du compte: ")
new_password['username'] = input("Nom d'utilisateur: ")

def generate_password():
    print('Longueur du mot de passe: ')
    password_length = int(input())
    password = ''
    for i in range(password_length):
        password += random.choice(characters)
    print('Mot de passe généré:', password)
    hashed_password = sha256(password)
    print('Le mot de passe haché est:', hashed_password)
    return password, hashed_password

def sha256(password_hashed):
    hash_object = hashlib.sha256(password_hashed.encode('utf-8'))
    return hash_object.hexdigest()

password, hashed_password = generate_password()

new_password['my_password'] = hashed_password

# Ajouter la nouvelle entrée de mot de passe
passwords[new_password['name']] = new_password

# Écrire les données dans le fichier JSON
with open(file_name, 'w') as file:
    json.dump(passwords, file, indent=4)

# Afficher les mots de passe
if passwords:
    for password in passwords.values():
        print(f"Nom du compte: {password['name']}")
        print(f"Nom d'utilisateur: {password['username']}")
        print(f"Mot de passe: {password['my_password']}\n")
else:
    print("Aucun mot de passe enregistré.")
