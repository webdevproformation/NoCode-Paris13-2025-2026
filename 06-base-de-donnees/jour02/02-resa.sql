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
);

-- ajouter deux profils utilisateurs dans la table user

INSERT INTO user 
( prenom , email  )
VALUES 
('Alain', 'a@y.fr') ,
('Céline', 'c@y.fr');

-- récupérer les id des utilisateurs insérés dans la table user 

SELECT * FROM user 

-- ajouter 2 réservations pour Alain 

INSERT INTO salle_reunion 
( nom , capacite , user_id )
VALUES 
( 'Bleu' , 10 , 1 ) ,
( 'Rouge' , 20 , 1 ) ; 

-- ajouter 3 réservations pour céline

INSERT INTO salle_reunion 
( nom , capacite , user_id )
VALUES 
( 'Bleu' , 10 , 2 ) ,
( 'Verte' , 30 , 2 ) ,
( 'Mauve' , 5 , 2) ; 


-- afficher pour l'ensemble des réservations pour chaque utilisateur 
-- j'ai besoin de récupérer des informations qui sont DANS PLUSIEURS tables 
-- SELECT en utilisant des JOINTURES 

SELECT salle_reunion.nom , user.prenom 
FROM salle_reunion
JOIN user
ON salle_reunion.user_id  =  user.id

-- je veux récuperer la colonne nom qui est dans la table salle_reunion
-- je veux récuperer la colonne prenom qui est dans la table user 

-- FROM salle_reunion ET 
-- Ajouter (JOIN) la table user 

-- ATTENTION entre la table user et la table salle_reunion on a définit une relation
-- utilise cette relation pour assembler les deux tables
-- FOREIGN KEY (user_id) REFERENCES user(id) 
-- user.id = salle_reunion.user_id 



-- Cas pratique 
-- vous devez créer une application pour gérer des etudiants 
-- vous devez créer un base de données qui contient 2 tables
-- etudiants :
    prenom
    nom 
    dt_naissance
    email 

- cours :
    nom 
    prix

chaque étudiant peut suivre plusieurs cours 
par contre un cours ne peut être suivi que par un et un seul etudiant 

créer les requêtes sql qui permettent de créer ces tables 


créer 3 etudiants

Alain nait en 01/01/1980 a@y.fr
Céline nait en 02/02/1990 c@y.fr 
Denis  nait en 03/03/2000 d@y.fr 

cours 
PHP 400 est suivi par Alain 
JS 200  est suivi par Alain 


CREATE TABLE IF NOT EXISTS etudiant(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    prenom VARCHAR(200) NOT NULL ,
    nom VARCHAR(200) NOT NULL ,
    dt_naissance DATE NOT NULL ,
    email VARCHAR(200) NOT NULL 
);

CREATE TABLE IF NOT EXISTS cours(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    nom VARCHAR(200) NOT NULL ,
    prix INT NOT NULL ,
    etudiant_id INTEGER NOT NULL ,
    FOREIGN KEY (etudiant_id) REFERENCES etudiant(id)
);

INSERT INTO etudiant 
( prenom , nom , dt_naissance , email )
VALUES 
( 'Alain', 'A' , '1980-01-01', 'a@y.fr' ),
( 'Céline', 'C' , '1990-02-02', 'c@y.fr' ),
( 'Denis', 'D' , '2000-03-03', 'd@y.fr' ) ;

INSERT INTO cours 
(nom , prix , etudiant_id)
VALUES
('PHP', 400 , 1) ,
('JS' , 200 , 1) ; 


SELECT cours.nom , etudiant.prenom , etudiant.nom 
FROM etudiant 
JOIN cours
ON etudiant.id = cours.etudiant_id ;



