'''
Base de données SQLite

'''

import sqlite3


#connexion à la bdd "mabdd.db"
conn = sqlite3.connect("mabdd.db")

#lire les données
request = "SELECT * FROM user"

le_curseur = conn.cursor()
le_curseur.execute(request)




ligne = le_curseur.fetchone()   #afficher les données de la première ligne

while ligne != None:            #Si ce n'est pas vide, veuillez l'afficher
    print(ligne)
    ligne = le_curseur.fetchone() 




le_curseur.close()






#fermeture de la bdd
conn.close()