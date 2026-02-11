-- méthode 1

DROP TABLE IF EXISTS exo2 ;

CREATE TABLE IF NOT EXISTS exo2 (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    age INTEGER,
    is_admin INTEGER,
    date_creation DATE
) STRICT;

INSERT INTO exo2 (email, age , date_creation) VALUES ('a@b.com', 2 , 'hello');


-- méthode 2 

DROP TABLE IF EXISTS exo2 ;

CREATE TABLE IF NOT EXISTS exo2 (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    age INTEGER CHECK (typeof(age) = 'integer'),
    is_admin INTEGER CHECK (is_admin IN (0, 1))
);

INSERT INTO exo2 (email, age) VALUES ('a@b.com', 'faux');