# schéma

- MCD => Modèle Conceptuel des données 

[x] Entité (table)
[x] Relation 
[x] Cardinalité 

- MLD => Modèle Logique des Données 

Transformer le MCD en MLD 

Transformer les Entités en Tables
Ajouter des colonnes en + dans les tables 
    clé primaire / Primary Key
    clé secondaire / clé étrangère / Foreign Key 

- Appliquer l'une des règles suivantes 
    - si on est sur une relation OneToMany ManyToOne => ajouter une clé étrangère côté du 1
    - si on est sur une relation ManyToMany          => créer une table intermédiaire 
    - si on est sur une relation OneToOne            => fusionner les tables 
- 

- MPD => Modèle Physique des Données 
- 
    - traduire le MLD et véritable requêtes SQL 
    - CREATE TABLE  

```sql
CREATE TABLE IF NOT EXISTS user(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    prenom VARCHAR(200) NOT NULL ,
    email VARCHAR(200) NOT NULL ,
    dt_naissance DATE 
);

CREATE TABLE IF NOT EXISTS salle_reunion(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    nom VARCHAR(200) NOT NULL , 
    capacite SMALLINT DEFAULT 0 , 
    user_id INTEGER NOT  NULL ,
    FOREIGN KEY (user_id) REFERENCES user(id) 
)

```