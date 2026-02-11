# Base de données 

- support de cours 
- https://formation.webdevpro.net/sgbd/
- login : sgbd
- password : sgbd



- support de cours 
- https://formation.webdevpro.net/python-initiation/
- login : python
- password : python


## intro 

- tout projet informatique (site internet) doit disposer d'une base de données
- Quand est ce que les bdd ont été crées ?? 
- à partir des années 70 => fichiers spéciaux 
- les fusées Apollo 
- => le père fondateur => Codd (ingénieur chez IBM)
- => base de données 
    1. Base de données (l'endroit où vous allez stocker l'information)
        - (le développeur ne doit pas la manipuler)
    2. SGBD => Système de Gestion de Base de Données 
        - l'outil qui va être en charge de discuter avec le développeur ET les données 
    3. pour parler avec un SGBD => utiliser un langage spécial SQL  


# Exemple : outil de gestion d'étudiants

```js
// début de l'informatique
const prenom1 = "Alain" ;
const nom1    = "DOE"   ;
const age1    = 22

const prenom2 = "Céline" ;
const nom2    = "DUPONT" ;
const age2    = 33       ; 
```

```js
const etudiants = [
    { prenom : "Alain" , nom : "DOE" , age : 22  },
    { prenom : "Céline" , nom : "DUPONT" , age : 33}
]

// CRUD tableau de JAVASCRIPT
// Create  => ajouter un nouvel étudiant         etudiants.push()
// Read    => rechercher un étudiant             etudiants[0]
// Update  => change l'age de Céline             etudiants[1].age = 34
// Delete  => Supprimer le profil d'Alain        etudiants.shift()
```

super exemple MAIS les tableaux en javascript sont idéals pour peu d'informations
Qu'est ce que je dois faire si je dois gérer 1000 étudiants et que chaque étudiant a 20 propriétés


=> SORTIR ce genre de valeur DANS UNE BASE DE DONNEES 


```js 
fetch("/adresse/internet")
    .then(function(reponse){ return reponse.json() })
    .then(function(  etudiants  ){ ....  })
```

DONC les valeurs ont été sorties hors de votre code => BASE DE DONNEES 

=> PLEIN DE BASE DE DONNEES SGBDR (Base de données Relationnelles)  => dès les années 80 

- Système payant (avec LICENCE) => ORACLE / ACCESS  / AirTable (NoCode)
- Système Gratuit (juste télécharger) => PostGRE / MariaDB / Sqlite  / BaseRow  (NoCode)

=> culture générale => Base de Données NOSQL => Redis // MongoDB    => dès les années 2000 

=> ce que je vous propose => SQlite pour découvrir les bases des bases de données 

---

# SQLite 

1. installer l'extension

=> il faut installer sur votre Visual Studio Code extension 
=> extensions > SQlite > installer l'extension Sqlite de alexcvzz

2. créer un fichier `.sqlite`
    - c'est ce fichier QUI va contenir nos DONNEES 
    - ce n'est pas au développeur d'écrire DEDANS 
    - créer et le fermer 

3. Lancer le SGBD (sqlite)
    1. clique droit sur le fichier `01-base.sqlite`
    1. choisir `open database`
    1. nouvelle zone est apparue => `sqlite explorer`


Pour discuter avec Sqlite (MySQL / Airtable ) => on utilise un langage qui s'appelle SQL 

---

# SQL Structured Query Langage 

=> langage qui contient des miliers de mots clés 
=> avec 50 mots clés vous pouvez faire de grandes choses 

pour insérer des données dans une base de données Relationnelle comme Sqlite
il faut au préalable créer "TABLE"


```sql 
-- commentaire
-- écrire en majuscule => SQL 
-- écrire en minuscule => nom de table / colonne / valeur ... 
CREATE TABLE first (
    prenom TEXT ,
    nom    TEXT 
)
```

