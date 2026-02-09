-- Maintenant que l'on sait créer des tables 

-- CRUD 

-- CREATE on va pouvoir les remplir d'informations 
-- READ   on va pouvoir rechercher des informations
-- UPDATE on va pouvoir mettre des informations existantes
-- DELETE on va pouvoir supprimer des informations existantes

-- créer un table qui contient des commentaires 

CREATE TABLE IF NOT EXISTS commentaire(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    email VARCHAR(200) NOT NULL ,
    message TEXT ,
    date_creation DATETIME ,
    is_published BOOLEAN DEFAULT FALSE 
); 

-- remplir d'enregistrements 
--     première () => préciser quelle colonnes 
--     deuxieme () => valeurs 
INSERT INTO commentaire () VALUES ()

INSERT INTO commentaire
( email , message )
VALUES 
( 'a@y.fr' , 'super article' );  


INSERT INTO commentaire 
(email , message , date_creation , is_published)
VALUES
('b@y.fr' , 'cool' , '2026-02-09 14:27:00', TRUE );

-- essayer d'exécuter une requête INSERT sans la colonne email 
-- dans ce cas vous avez une erreur qui vous dit  
-- Runtime error near line 4: NOT NULL constraint failed:

INSERT INTO commentaire 
(message,date_creation,is_published)
VALUES
( 'cool' , '2026-02-09 14:30:00', FALSE ); -- ERREUR 



INSERT INTO commentaire 
(email , date_creation )
VALUES
( 'c@y.fr', 'comment vas tu ??' );

-- opération inverse du INSERT => DELETE supprimer une ligne 

DELETE FROM commentaire WHERE id=3;


-- Exo 

-- créer une table exo1
-- cette table contient 5 colonnes
-- clé primaire
-- nom texte maximum de 255 lettres non facultatif
-- description texte long
-- date_publication date et heure et par défaut maintenant
-- date_mis_ajouter date et heure non facultatif 


-- ajouter 3 lignes dans la table 
-- 'exo1' , NULL , 'maintenant' , 'maintenant'
-- 'exo2' , 'coucou', NULL , le 1er janvier 2026 à 18h00 00
-- exo3 , salut , le 1er janvier 2026 à 18h00 00 , le 2 janvier 2026 à 18h00 00


DROP TABLE IF EXISTS exo1 ; 

CREATE TABLE IF NOT EXISTS exo1(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    nom VARCHAR(255) NOT NULL ,
    description TEXT ,
    date_publication DATETIME DEFAULT CURRENT_TIMESTAMP ,
    date_mis_jour DATE NOT NULL 
);

INSERT INTO exo1 
(
   nom ,    date_publication , date_mis_jour
)
VALUES 
(
  'exo1' ,  CURRENT_TIMESTAMP ,   CURRENT_DATE
);

INSERT INTO exo1 
(
   nom , description ,   date_mis_jour
)
VALUES 
(
  'exo2' , 'coucou' ,  '2026-01-01 18:00:00'
);

INSERT INTO exo1 
(
   nom , description ,date_publication ,   date_mis_jour 
)
VALUES 
(
  'exo3' , 'salut' ,  '2026-01-01 18:00:00' , '2026-01-02 18:00:00'
);


--- si je veux modifier la valeur dans le champ nom de la table exo1 ayant l'id 


UPDATE exo1 SET nom = 'exo3' WHERE id = 3 OR id = 2;

UPDATE exo1 SET nom = 'exo3' WHERE id > 1;

UPDATE exo1 SET nom = 'exo3' WHERE id IN (2,4,50, 1000) ;
UPDATE exo1 SET nom = 'exo3' WHERE id BETWEEN 3 AND 10  ;



---

-- Creer des tables CREATE TABLE 

-- Enregistrement
-- CREATE => INSERT INTO nom_table () VALUES () 
-- UPDATE => UPDATE nom_table SET nom_colonne = 'valeur' WHERE id = 1
-- DELETE => DELETE FROM nom_table WHERE id = 1 

-- SELECT => dernière opération de base sur une table 
-- permet de récupérer une ou plusieurs valeurs 

SELECT * FROM exo1 ; 

-- récupérer toutes les lignes et toutes les colonnes de la table exo1

SELECT nom , description , date_mis_jour 
FROM exo1 ;

-- il est possible de récupérer certaines colonnes 


SELECT nom AS `titre publication` , description , date_mis_jour AS `updated at`
FROM exo1 ;

-- AS ne modifie pas le nom de la colonne dans la table exo1 elle va juste être affichée lorsque vous avez réalisé le SELECT


SELECT nom AS `titre publication` , description , date_mis_jour AS `updated at`
FROM exo1 ;


-- vous pouvez effectuer des calculs 
-- dans un select  => concatenation 

SELECT nom || ' publié sur l id ' || id AS `description article`
FROM exo1 ;


SELECT nom , strftime("%d/%m/%Y" , date_mis_jour )
FROM exo1 ;

-- il est possible de filtrer des résultats (ne pas avoir toutes les lignes)

SELECT * 
FROM exo1 
WHERE id = 1 ;

-- récupére moi toutes les colonnes dont l'id a pour valeur le chiffre 1


SELECT * 
FROM exo1 
WHERE id = 1 OR id = 2 ;


SELECT * 
FROM exo1 
WHERE id IN ( 1, 2 ) ; 


----

CREATE TABLE IF NOT EXISTS exo3 (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    email VARCHAR(150) NOT NULL,
    age INT,
    is_admin BOOLEAN
);


INSERT INTO exo3 

(name, email, age, is_admin) 
VALUES
('Alice Martin', 'alice.martin@example.com', 25, 0),
('Bob Dupont', 'bob.dupont@example.com', 32, 0),
('Charlie Leroy', 'charlie.leroy@example.com', 41, 1),
('Diana Petit', 'diana.petit@example.com', 29, 0),
('Ethan Moreau', 'ethan.moreau@example.com', 35, 0),
('Fatima Benali', 'fatima.benali@example.com', 28, 0),
('George Smith', 'george.smith@example.com', 45, 1),
('Hannah Brown', 'hannah.brown@example.com', 22, 0),
('Ivan Ivanov', 'ivan.ivanov@example.com', 38, 0),
('Julia Rossi', 'julia.rossi@example.com', 31, 0),
('Kevin Nguyen', 'kevin.nguyen@example.com', 27, 0),
('Laura Garcia', 'laura.garcia@example.com', 34, 1),
('Mohamed Ali', 'mohamed.ali@example.com', 40, 0),
('Nina Schmidt', 'nina.schmidt@example.com', 26, 0),
('Oscar Lopez', 'oscar.lopez@example.com', 36, 0),
('Paula Silva', 'paula.silva@example.com', 24, 0),
('Quentin Dubois', 'quentin.dubois@example.com', 33, 0),
('Rania Haddad', 'rania.haddad@example.com', 29, 0),
('Samuel Cohen', 'samuel.cohen@example.com', 42, 1),
('Yasmine Noor', 'yasmine.noor@example.com', 21, 0);


Pouvez vous me donner donner le nom de tous les étudiants qui ont le rôle admin ?

SELECT name FROM exo3 WHERE is_admin = TRUE ;


pouvez vous me donner le  nom et l'email de tous les étudiants qui ont plus de 30 ans

SELECT name , email FROM exo3 WHERE age >=30  ;

pouvez vous me donner le  nom et l'email de tous les étudiants qui ontentre 20 et 40 ans

SELECT name , email FROM exo3 WHERE age >= 20 AND age <= 40
SELECT name , email FROM exo3 WHERE age BETWEEN 20 AND 40

- pouvez vous me donner le  nom et l'email de tous les étudiants qui ont entre 20 et 40 ans ET qui sont admin ? 


SELECT name , email FROM exo3 WHERE age >= 20 AND age <= 40 AND is_admin = TRUE


- je veux récupérer tous les étudiants dont le name commence par lettre a 


SELECT * FROM exo3 WHERE name LIKE 'A%'

SELECT * FROM exo3 WHERE name LIKE '%s'

-- tous les étudiants dont le name contient le texte ma 

SELECT * FROM exo3 WHERE name LIKE '%ma%' 

-- tous les étudiants dont le name ne contient pas les lettres ma 

SELECT * FROM exo3 WHERE name NOT LIKE '%ma%'

-- afficher tous les étudiants / toutes les colonnes mais je veux que les valeurs soient triées par age croissant (jeune => ancien)

SELECT * FROM exo3 ORDER BY age ASC

-- afficher tous les étudiants / toutes les colonnes mais je veux que les valeurs soient triées par age décroissant (ancien => jeune)

SELECT * FROM exo3 ORDER BY age DESC


SELECT * FROM exo3 
WHERE age > 30 
ORDER BY age DESC


tout l'intérêt de bases de données au delà créer un méthode commune pour gérer les données 
en + c'est le fait de pouvoir créer des relations entre les tables 


=> demandé à la base de données 

table article 
- id PK
- titre 
- description 

table commentaire 
- id PK
- email
- message 
- article_id => clé étrangère (liaison entre la table commentaire ET la table article) 
