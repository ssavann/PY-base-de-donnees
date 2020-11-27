'''
Base de données SQLite

'''

import sqlite3


#connexion à la bdd "mabdd.db"
conn = sqlite3.connect("mabdd.db")


request = " CREATE TABLE IF NOT EXISTS 'user' ('nom' TEXT,'password' TEXT); "

le_curseur = conn.cursor()
le_curseur.execute(request)
le_curseur.close()


#fermeture de la bdd
conn.close()