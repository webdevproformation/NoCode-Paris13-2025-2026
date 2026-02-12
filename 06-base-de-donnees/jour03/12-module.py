# quand vous allez écrire du javascript 
# fichier html
#   <script src="module.js" type="module"></script>
#   <script src="diaporama.js"></script>
#   <script src="formulaire.js"></script>
#   <script src="menu-deroulant.js"></script>

# dans le fichier module.js
# const a = 2
# const b = 3
# function toto(){}

# dans le fichier formulaire.js
# toto()

# dans le fichier menu-deroulant.js
# console.log(a)

# from lib import a  , b , bonjour

# print(a)
# print(b)
# bonjour()

import lib 
# import api.client
from api.client import URL
# par défault python est livré avec de très nombreux modules 
# qui ne sont pas activés disponibles par défaut 
import datetime # module natif de python 
import sqlite3

# module créé par la communauté des développeurs Python 
# flask
# requests 
# télécharger via l'outil interne de téléchargement de module
# pip install flask requests 
# le site internet pip va cherche les librairies
# pypi.org
# pip install <flask> # install moi de manière globale la librairie flask
# pour préparer l'installation de notre site sur AWS 
# installer nos librairies en local (dans un environnement virtuel)
# dossier qui contient des librairies qui ne vont fonctionner QUE sur 1 projet 
# pip install flask
# pip install flask@0.1.13
# commande qui permet de créer un environement virtuel
# python -m venv .venv
# .venv\Scripts\activate


print(lib.a)
print(lib.b)
lib.bonjour()
#print (api.client.URL)
print (URL)
print(datetime.datetime.now())