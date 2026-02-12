# rappel 

- Base de données 3 niveaux
    - base de données
    - tables
    - enregistrements

tables sont en relation les unes avec les autres 

OneToOne
OneToMany ManyToOne
ManyToMany 


article peut avoir 1 ou plusieurs commentaire(s)
commentaire ne peut être associé que à 1 seul article

```sql
CREATE TABLE IF NOT EXISTS article(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titre VARCHAR(255) NOT NULL ,
    contenu TEXT
);
 
CREATE TABLE IF NOT EXISTS commentaire(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL ,
    message TEXT,
    article_id INTEGER NOT NULL ,
    FOREIGN KEY article_id REFERENCES article(id)
)
```
        article 
-----------------------------
id  |   titre   | contenu   |
1   |  PHP      | apprendre |
2   |  Python   | découvrir |


        commentaire  
----------------------------------------
id  |   email   | message   | article_id
1   |  a@y.fr   | super     |    1
2   |  b@y.fr   | cool      |    2

Réaliser une JOINTURE 

```sql
SELECT article.title , article.contenu , commentaire.message
FROM article
JOIN commentaire
ON article.id = commentaire.article_id 
```


=> Baserow


- Installation de Python

- Python 

```py
# commentaire

"""
commentaire multiligne
coucou
"""

# variable
premier_etudiant = "Alain"

# constante
URL = "https://google.fr"


# valeur 

# chiffre

duree = 10 
reduction = 0.5


# texte

auteur = 'Victor'
nom    = "Hugo"

description = '''
bonjour
les 
amis
'''


# boolean 

var1 = True
var2 = False 

# tableau => stocker plusieurs valeurs dans une seule variable 
# en python il en existe 4 par défauts
# liste  xxxxxxxxxx
# tuple
# set
# dictionnaire xxxxx

liste = ["a","b" , "c"]

dictionnaire = {
    "prenom"   : "Julie",
    "nom"      : "DOE" ,
    "is_admin" : True
}



```