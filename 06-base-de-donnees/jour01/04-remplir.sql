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


UPDATE exo1 SET nom = 'exo3' WHERE id = 3 ;