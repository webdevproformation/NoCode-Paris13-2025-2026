# variables

manipuler des VALEURS => gestion de rendez vous
    - date et heure de début
    - date et heure de fin
    - description
    - lieu
    - personnes invitées
    - etc 

Pour qu'un programme puisse accéder / manipuler / utiliser ces valeurs => STOCKER ces valeurs dans des VARIABLES 

# variables et les constantes 

- variable => stocker une valeur ET pouvoir la modifier
            - `mutable`
- constante => stocker une valeur ET plus possible de la modifier 
            - une constante est une variable dont la valeur ne peut pas changer 
            - `readonly`, `immutable` 


# variable / constante est un espace mémoire

- en fonction du langage utilisé vous avez la possible de dire où et quelle taille à l'espace mémoire
- en C => langage bas niveau => possibilité de préciser quelle taille et où
- en PHP, JS, Python => langage haut niveau => le compilateur (traducteur de votre code en bit) qui va faire le travail à votre place 

# en algorithmie

une variable peut contenir :

- string  => texte
- int     => chiffre entier 1 22 33 -10
- float   => chiffre à virgule 1.5 -2.3
- boolean => boolean 0 1   False  True


```txt
algo nom_programme

variables
a, b : int
c    : float 

début
    traitement 1
    traitement 2
fin
```

# cas pratique 

- créer un algo qui s'appelle exo1
- cette algo créer 4 variables 
    - a qui est un chiffre entier
    - b qui est un texte
    - c qui est un texte
    - d qui est soit 0 soit 1 

```txt
algo exo1

variables
a    : int
b, c : string
d    : bool

debut
fin
```

## dernier point => NOMMER les variables

- commencer par une Majuscule / Minuscule / _ / $
- puis  Majuscule / Minuscule / _ / chiffres 
- mais il existe aussi des normes 

les normes de nommage à connaitre : 

- premierEtudiant => camelCase ( casse Chameau)
- PremierEtudiant => PascalCase ( casse Pascal )
- premier-etudiant => kebab-case
- premier_etudiant => snake_case 
 