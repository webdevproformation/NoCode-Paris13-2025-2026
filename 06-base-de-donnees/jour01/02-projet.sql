-- créer un fichier 01-base.sqlite
-- créer un fichier 02-projet.sql 

-- créer une première table qui s'appelle first 
-- dans cette table vous avez 2 colonnes 
-- prenom stocker dedans du texte
-- nom    stocker dedans du texte 

CREATE TABLE IF NOT EXISTS first(
    prenom TEXT ,
    nom TEXT 
) ;


-- cas pratique 
-- créer une nouvelle table qui s'appelle second
-- cette table contient 3 colonnes 
-- titre qui contient du texte
-- contenu qui contient du texte
-- auteur qui contient du texte 

-- créer le requête SQL 
-- exécuter 
-- visualiser la table dans SQlite Explorer 

CREATE TABLE IF NOT EXISTS second(
    titre TEXT ,
    contenu TEXT ,
    auteur TEXT  ,
    commentaire TEXT
) ;

-- je veux supprimer une table 

DROP TABLE IF EXISTS second ; 

-- il est possible de modifier la structure d'une table 
-- via le mot clé SQL ALTER TABLE 
-- ATTENTION MAIS ALTER TABLE n'existe pas dans SQlite 

-- si j'étais sur MySQL et que je veux ajouter une nouvelle colonne à la table second 

ALTER TABLE second ADD COLUMN info TEXT ; 

-- lorsque l'on crée un table il est possible de préciser la nature (type) de données que l'on veut stocker dans les colonnes 

-- il est possible de stocker 3 grandes familles de données :

-- chiffre 
    -- chiffre entier    SMALLINT  MEDIUMINT INT BIGINT 
    -- chiffre à virgule DECIMAL REEL 
    -- Boolean 0 1       BOOLEAN
-- texte
    -- texte variable VARCHAR() 0 255
    -- TEXT => 45 000 caractères
    -- BLOB => Big Large Object => stocker film 
-- date 
    -- DATE     AAAA-JJ-MM
    -- DATETIME AAAA-JJ-MM HH:MM:SS
    -- TIME     HH:MM:SS

-- minimum quelquesoit la base de données que vous allez utiliser 

-- créer une table qui s'appelle client

-- contient 6 colonnes
-- prenom texte avec un maximum de 255 lettres
-- date_naissance AAAA-MM-JJ
-- email texte avec un maximum de 255 lettres
-- is_admin 0 1
-- last_connection AAAA-MM-JJ HH:MM:SS 
-- profil texte long 


CREATE TABLE IF NOT EXISTS client(
    prenom VARCHAR(255),
    `date-naissance` DATE ,
    email VARCHAR(255),
    is_admin BOOLEAN ,
    last_connection DATETIME ,
    profil  TEXT
);

-- créer un table qui s'appelle etudiant

-- prenom texte avec maximum 255 lettres
-- age chiffre entier maximum de 255
-- cv  text long 
-- is_inscrit boolean 0 / 1 
-- date_inscription AAAA-MM-JJ HH:MM:SS 

CREATE TABLE IF NOT EXISTS etudiant(
    prenom VARCHAR(255) ,
    age SMALLINT ,
    cv TEXT ,
    is_inscrit BOOLEAN ,
    date_inscription DATETIME
);


CREATE TABLE IF NOT EXISTS etudiant(
    prenom VARCHAR(255)  DEFAULT NULL,
    age SMALLINT  DEFAULT NULL,
    cv TEXT  DEFAULT NULL,
    is_inscrit BOOLEAN  DEFAULT NULL,
    date_inscription DATETIME DEFAULT NULL
);


-- en plus du type des colonnes vous pouvez ajouter des CONTRAINTES 
-- DATETIME => ce n'est pas FACULTATIF => c'est obligatoirement une date 
-- si vous ne précisez rien après le type TEXT , DATETIME ... par défaut 
-- la colonne accepte à la fois le type ET NULL 


CREATE TABLE IF NOT EXISTS produits(
    nom VARCHAR(255) NOT NULL UNIQUE , 
    prix DECIMAL(10,2) NOT NULL , 
    is_published BOOLEAN DEFAULT TRUE , 
    -- si on lui donne une valeur NULL alors SQlite va lui donner la valeur TRUE
    description TEXT ,
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP 
    -- si je ne donne pas de date => prendre la date et heure de maintenant 
);

-- DECIMAL chiffre qui contient 10 chiffres au maximum dont 2 en dessous de la virgule 

-- 10.20
-- 99999999.99
