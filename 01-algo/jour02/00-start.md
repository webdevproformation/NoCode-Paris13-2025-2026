# support 

- <https://formation.webdevpro.net/algo>
- login : algo
- password : algo

# rappels 

- programme => suite d'instructions 
- variable moyen de manipuler des valeurs 
- la nature de la valeur stockée est importante
    - texte (string)
    - chiffre entier / chiffre à virgule
    - boolean true / false 0 / 1

- opérateurs
    - calcul + - / * % div ^
    - comparaison < > <= >= == !=
    - attribution <- 
    - logique && || ! 

- Input Output 
    - capacité du langage informatique avec interagir avec son utilisateur
    - Demander une info  input() confirm()
    - Ecrire un message  print() alert() console.log()

- chaine de caractère ça ressemble beaucoup à des variables

```txt

debut
        'C' => texte est entouré d'apostrophe 
        C   => variable 
fin 
```

- addition de deux textes , c'est possible en informatique CONCATENATION avec l'opérateur &

```txt
algo concat

variables 
a, b , c : string

debut
    a <- 'Victor'
    b <- 'Hugo'
    c <- a & ' ' & b // 'Victor Hugo'
fin 
```

- en informatique, le code s'exécute de haut en bas par défaut 
- il existe 3 syntaxes, 3 structures de contrôles qui vont changer l'ordre exécution du programme 
    - condition => SI (if)
    - boucle    => for / while 
    - fonction   

- le SI 


```txt
algo gestion_droit

variables
    role : string

debut
    role <- 'redacteur'

    SI role == 'admin' Alors
        // si la condition est vrai alors exécution de la première partie ET la deuxième est ignorée
        // si la condition est fausse alors exécution de la deuxieme partie ET la première est ignorée
        Ecrire('Afficher le tableau de bord')
    Sinon
        Ecrire('Afficher la page de profil de base')

fin
```