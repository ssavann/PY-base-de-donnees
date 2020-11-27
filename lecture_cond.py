'''
Base de données SQLite

'''

import sqlite3


#connexion à la bdd "mabdd.db"
conn = sqlite3.connect("mabdd.db")

#lire les données en fonction d'une critère
request = "SELECT nom, password FROM user WHERE nom = 'Marielle'"

le_curseur = conn.cursor()
le_curseur.execute(request)


ligne = le_curseur.fetchone()   #afficher les données de la première ligne
print(ligne)


print(f"Username : {ligne[0]}       Password : {ligne[1]}")

le_curseur.close()
#fermeture de la bdd
conn.close()