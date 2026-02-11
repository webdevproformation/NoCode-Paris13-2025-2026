# Rappel 

## CRUD 

- Create 
- Read 
- Update 
- Delete

## 3 concepts clé des Bases de données 

1. Base de données 
2. Table (ensemble de colonnes)
3. Enregistrements


## CRUD pour les Base de données 

Create
pour sqlite => créer un fichier .sqlite 
pour MySQL  => `CREATE DATABASE nom_base` ;

Read 
pour sqlite => utiliser outil (extension)
pour mySQL  => `USE nom_base ; SHOW TABLES ;`

Update
pour sqlite => changer le nom du fichier
pour MySQL => ???? 

Delete
pour sqlite => supprimer le fichier
pour MySQL  => `DROP DATABASE nom_base`

## CRUD Table 

Create 
pour SQlite  => 
```sql 
CREATE TABLE IF NOT EXISTS nom_table(
    id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT ,
    nom VARCHAR(255) NOT NULL UNIQUE ,
    is_admin BOOLEAN ,
    prix DECIMAL(10,2) ,
    age SMALLINT ,  
    dt_arrivee DATETIME ,
    dt_fin DATE 
) STRICT 
```

pour MySQl  => 
```sql 
CREATE TABLE IF NOT EXISTS nom_table(
    id INT  NOT NULL PRIMARY KEY AUTO_INCREMENT ,
    nom VARCHAR(255) NOT NULL UNIQUE ,
    is_admin BOOLEAN ,
    prix DECIMAL(10,2) ,
    age SMALLINT ,  
    dt_arrivee DATETIME ,
    dt_fin DATE 
) 
```

READ  (structure / pas le contenu)
pour sqlite => `.schema table_name`
pour mySQL => `EXPLAIN TABLE nom_table`

Update 
pour sqlite => `créer une table intermédiaire / stocker les valeurs dedans / créer le nouvelle table et supprimer l'ancienne`
pour MySQL => `ALTER TABLE .... `

DELETE 

pour sqlite => DROP TABLE table_name
pour mySQL  => DROP TABLE table_name


## Enregistrement  (les données)

CREATE 
pour sqlite / MySQL 

```sql
INSERT INTO nom_table ( nom_col , nom_col) VALUES ( '' , ''  )
```

READ 
pour sqlite / mySQL 

```sql
-- renommer des colonnes 
-- faire des calculs sur des colonnes 
SELECT  nom_col AS `nouveau nom` , *  , nom_col + 1
FROM nom_table 
-- filtrer avec
WHERE nom_col = '' AND nom_col LIKE '%s%'
-- trier
ORDER BY nom_col ASC / DESC
```

## UPDATE
 
pour sqlite / mySQL 

```sql
UPDATE nom_table SET nom_col = 'nouvelle valeur' WHERE id = 1
```


## DELETE

pour sqlite / mySQL 

```sql
DELETE FROM nom_table WHERE id = 1 
```

