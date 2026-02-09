-- 03-suite.sql 

-- rappel 
-- tout projet informatique nécessite des valeurs 
-- si vous avez beaucoup de valeurs à manipuler dans votre projet
    -- variable 
    -- tableau 
    -- utiliser une base de données 


-- pour découvrir les bases
    -- SQlite => théorie
    -- Airtable => retrouver les concepts présentés dans SQLite
    -- Rowbase (SupaBase ???) <==> API (Application Program Interface)

-- 3 concepts
    -- base de données
    -- table (qui sont un essemble de colonnes)
    -- Enregistrements 

-- découvrir le vocabulaire de base du langage SQL 

-- BASE DE DONNEE => créer un fichier / renommer / supprimer 
-- sur MySQl 

CREATE DATABASE nom_base ;
DROP DATABASE nom_base ;


-- TABLE 

CREATE TABLE IF NOT EXISTS nom_table(
    nom_colonne VARCHAR(255) NOT NULL UNIQUE , 
    nom_colonne2 DATETIME DEFAULT CURRENT_TIMESTAMP ,
    nom_colonne3 VARCHAR(200) DEFAULT 'un texte' 
);

-- attention dans les nom de colonnes, ne pas mettre d'espace ou symbole mathématiques ( - + / ...) ou un mot clé de SQL 
-- sinon il faudra mettre des backtick `nom-colonne` 

-- En plus de ces colonnes, en général on va en plus ajouté une colonne TECHNIQUE
-- clé colonne en général elle va être appelée `id`
-- c'est une colonne qui est une clé primaire (primary key / PK)
-- cette colonne a plusieurs roles 
    -- permettre de pouvoir sélectionner une ligne dans une tableau SANS AMBIGUITE
    -- permettre de mettre en relation la table avec une table (SGBDR )


CREATE TABLE IF NOT EXISTS formation (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    nom VARCHAR(200) NOT NULL ,
    description TEXT ,
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP ,
    is_ready BOOLEAN DEFAULT FALSE 
);

-- créer une table catalogue 
-- elle contient 
-- colonne id clé primaire
-- nom texte maximum de 100 lettres n'accepte pas NULL 
-- categorie texte long 
-- description texte long
-- online Boolean par défaut à VRAI
-- nb_produit chiffre entier très grand (4 milliards maximum)
-- date_mise_a_jour AAAA-MM-JJ n'accepte pas la valeur NULL 


CREATE TABLE IF NOT EXISTS catalogue(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(100) NOT NULL ,
    categorie TEXT ,
    description TEXT ,
    online BOOLEAN DEFAULT TRUE ,
    nb_produit INT ,
    date_mise_a_jour DATE NOT NULL 
); 

-- google Mariadb column types 
-- https://www.ionos.fr/digitalguide/hebergement/aspects-techniques/mariadb-data-types/
-- https://mariadb.com/docs/server/reference/data-types/data-type-storage-requirements