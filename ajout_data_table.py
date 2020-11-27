'''
Base de données SQLite

'''

import sqlite3


#connexion à la bdd "mabdd.db"
conn = sqlite3.connect("mabdd.db")

#ajout de données à la table
#pour ajouter des données dans la BDD
#request = "INSERT INTO 'user' VALUES ('admin', '1234')"


#pour inserer plusieurs données en même temps
request = """
INSERT INTO user (nom, password)
 VALUES
 ('Rébecca', 'Arm9879'),
 ('Aimée', 'Heb456'),
 ('Marielle', 'Rib999'),
 ('Hilaire', 'Sava555');

"""


le_curseur = conn.cursor()
le_curseur.execute(request)
le_curseur.close()

conn.commit()       #pour lui indiquer de procéder


#fermeture de la bdd
conn.close()