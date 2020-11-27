'''
Base de données SQLite

'''

import sqlite3


#connexion à la bdd "mabdd.db"
conn = sqlite3.connect("mabdd.db")

#lire les données en fonction d'une critère
request = """
DELETE FROM user WHERE nom = 'Aimée'


"""

le_curseur = conn.cursor()
le_curseur.execute(request)




le_curseur.close()

conn.commit()           #pour procéder au changement

#fermeture de la bdd
conn.close()