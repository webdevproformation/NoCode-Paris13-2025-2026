# tableau 

je veux gérer un catalogue de produits :

- PS4
- PS5
- Nintendo DS

```txt
algo gestion_catalogue

variables 
    p1 , p2 , p3 : string

debut
    p1 <- 'PS4'
    p2 <- 'PS5'
    p3 <- 'Nintendo DS'
fin
```

# tableau : une variable qui contient PLUSIEURS VALEURS 

// je veux pouvoir stocker ces 3 produits dans 1 seule variable 
// tableau (array)


```txt
algo gestion_catalogue

variables
    catalogue : array : string 

debut 
    catalogue <- [ "PS4" , "PS5" , "NintendoDS" ]
    //               0       1          2         // FAIT AUTOMATIQUEMENT 
    // catalogue est une variable qui contient 3 textes 

    // chaque valeur stockée dans le tableau  a une position => INDEX 

    catalogue [ 2 ] // récupérer la valeur qui est à l'index 2 dans la variable catalogue => "NintendoDS"

    catalogue[ 1 ]
    
    Ecrire( catalogue [ 1 ] ) // PS5

fin
```

# exemple d'utilisation d'un tableau 

```txt
algo gestion_formation

variable 
    formation : array : mixed 

debut
    // 5 valeurs 
    formation <- [ 'diw No Code' , 4 , 5000 , 'Paris 13' , 'mois'  ]
    // écrire la phrase suivante 
    // je suis une formation de 4 mois à Paris 13
    // 'je suis une formation de ' &  formation[ 1 ]  & ' ' &  formation[ 4 ] &  ' à ' &  formation[ 3 ]
    // la formation diw No Code coûte 5000 euros / par mois 
    // 'la formation ' &  formation[0]  &  ' coûte ' &  formation[3] &  'euros / par ' &  formation[ 4 ] 
fin     
```
# exo 

créer l'algo exo10  
dans cet algo, vous devez créer un tableau qui s'appelle `fleur` qui contient les  5 valeurs suivantes (bien respecter l'ordre des valeurs):

- rose
- 30
- euros
- 10
- Monceau Fleurs

A partir de ce tableau , écrire les phrases suivantes à partir de la variable `fleurs` :
- J'ai acheté un bouquet de roses pour 30 euros
- La boutique Monceau Fleurs est située au 10 rue de Paris
- Monceau Fleurs fait une promotion sur les 10 premiers clients : -30% 


```txt
algo exo10

variable 
    fleur : array : mixed

debut
    fleur <- [ 'rose' , 30 , 'euros'  , 10 , 'Monceau Fleurs' ]

    // - J'ai acheté un bouquet de roses pour 30 euros
    
    'J\'ai acheté un bouquet de ' & fleur[0] & 's pour ' & fleur[1] & ' ' & fleur[2]

    // - La boutique Monceau Fleurs est située au 10 rue de Paris

    'La boutique ' & fleur[4] & ' est située au ' & fleur[3] & ' rue de Paris' 

    // - Monceau Fleurs fait une promotion sur les 10 premiers clients : -30% 

    fleur[4] & ' fait une promotion sur les ' & fleur[3] & ' premiers clients : -' & fleur[1] & '%'
fin
```

# Enoncé :

Tu as un tableau d'entiers. Le but de l'exercice est de trouver le plus grand nombre dans ce tableau. 
Ton algorithme s'appelle `max`
il contiennent 3 variables 
    tableau ....
    resultat int
    i 
    
créer le tableau <- [ 22 , 10 , 15 , 99 , 1 ]
    
parcourir chaque element du tableau est ne garde QUE celui qui est le plus grand

```txt
algo max

variables 
    t : array : int 
    resultat : int
    i : int 

debut
    t <- [ 22 , 10 , 15 , 99 , 1 ]
    resultat <- t[0] 

    // 1 position du 2ème élément du tableau t
    // 4 la position du dernier élément du tableau t
    Pour( i <- 1 ; i <= 4 ; i <- i + 1){
        Si resultat < t[i]   
            resultat <- t[i]
    }
    
    Ecrire( resultat )

fin 
```


```txt
algo max

variables 
    t : array : int 
    resultat : int
    i : int 

debut
    t <- [ 22 , 10 , 15 , 99 , 1 ]
    resultat <- t[0] 
    i <- 1

    TantQue(  i <= 4 ){
        Si resultat < t[i]   
            resultat <- t[i]

        i <- i + 1
    }
    
    Ecrire( resultat )

fin 
```