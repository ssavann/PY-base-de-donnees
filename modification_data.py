'''
Base de données SQLite

'''

import sqlite3


#connexion à la bdd "mabdd.db"
conn = sqlite3.connect("mabdd.db")

#lire les données en fonction d'une critère
request = """
UPDATE user
SET password = '9999'
WHERE nom = 'Marielle'


"""

le_curseur = conn.cursor()
le_curseur.execute(request)




le_curseur.close()

conn.commit()           #pour procéder au changement

#fermeture de la bdd
conn.close()