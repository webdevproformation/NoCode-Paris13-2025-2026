# boucle 

- loop en anglais
- c'est la capacité de pour un programme de répéter plusieurs fois un même code 

// je dois écrire le texte suivant 
//  0 x 2  = 0
//  1 x 2  = 2
//  2 x 2  = 4
//  3 x 2  = 6
//  4 x 2  = 8

```txt
algo table_multiplication

variables
    cas0 , cas1, cas2, cas3, cas4 : string

debut
    cas0 <- '0 x 2  = 0'
    Ecrire( cas0 )

    cas1 <- '1 x 2  = 2'
    Ecrire( cas1 )  

    cas2 <- '2 x 2  = 4'
    Ecrire( cas2 ) 

    cas3 <- '3 x 2  = 6'
    Ecrire( cas3 )  

    cas4 <- '4 x 2  = 8'
    Ecrire( cas4 ) 
fin
```

- le code précédent est fonctionnel MAIS il y a beaucoup de répétitions
- en utilisant les boucles nous allons pouvoir écrire une seule fois une des répétitions ET laisser au code la capacité de réexécuter le code autant de fois que nécessaire
 

```txt
algo table_multiplication

variables
    cas : string
    i   : int // compteur variable qui va s'incrémenter (augmenter de +1)
              // cette variable est obligatoire pour utiliser les boucles 

debut
    Pour i <- 0 jusqu' 4 augmente + 1
         // i <- 0 // dans la variable i stocker la valeur 0         
         // jusqu' 4 // est ce que i est inférieur à 4 ??? 0 < 4 true 
         // exécuter les traitements dans la boucle Pour
         // concaténation 
         // i & ' x 2  = ' & i * 2
         // 0 & ' x 2  = ' & 0 * 2
         // cas <- '0 x 2  = 0' 

        cas <- i & ' x 2  = ' & i * 2
        Ecrire( cas )  
fin
```

programme qui écrit 

1
2
3
4

```txt
algo chiffres

debut
    Ecrire(1)
    Ecrire(2)
    Ecrire(3)
    Ecrire(4)
fin 
```


```txt
algo chiffres

variable 
    i : int 

debut
    chiffre qui commence à 1 
    ET qui augmente de + 1 entre chaque exécuter // incrément 
    qui finit à 4
    
    Pour(i <- 1 ; i < 5 ; i <- i + 1){
        Ecrire(i)
    }
fin 
```

créer l'algo exo5
ce script va afficher à l'écran la suite de chiffre suivante 

4  
5  
6
7 
8
9 
10
11

utiliser les boucles pour éviter d'avoir un code répétitif

min 4
maximum 11     <= 11 || < 12
pas (augmentation)  + 1 à chaque exécution de la  boucle / chaque itération


```
algo exo5

variable
    i : int 

debut
    Pour( i <- 4 ; i <= 11 ; i <- i + 1 ){
        Ecrire( i )
    }
fin
```

# changer la valeur de l'augmentation + 1 à + 3

```txt
4  
7 
10
13
```


```
algo exo5

variable
    i : int 

debut
    Pour( i <- 4 ; i <= 13 ; i <- i + 3 ){
        Ecrire( i )
    }
fin
```

# décrémenter

```txt
10
8
6
4
2
```


```txt
algo exo5

variable
    i : int 

debut
    Pour( i <- 10 ; i >= 2 ; i <- i - 2 ){ // réduit i => décrémente 
        Ecrire( i )
    }
fin
```

# exo

créer un nouvel algo qui s'appelle `exo6` et qui écrit la suite de chiffres suivants :

```txt
1    => 1 * 1 
4    => 2 * 2
9    => 3 * 3
16   => 4 * 4
25
36
49   => 7 * 7
```
min 1
maximum 7    <=7 ou < 8
augmentation de + 1

```txt
algo exo6

variable
    i : int

debut
    Pour( i <- 1 ; i < 8 ; i <- i + 1 ) {
        Ecrire( i * i )
    }
fin
```

# exo

créer un nouvel algo qui s'appelle `exo7` et qui écrit la suite de chiffres suivants :


```txt
1 x 4 = 4  si i = 1     i & 'x 4 = ' & i * 4
2 x 4 = 8  si i = 2     i & 'x 4 = ' & i * 4
3 x 4 = 12
4 x 4 = 16
```

- min 1
- maximum 4  <=4 ou < 5
- pas  + 1

```txt
algo exo7

variable 
    i : int 

debut
    Pour(i <- 1 ; i <= 4 ; i <- i + 1){
        Ecrire(i & 'x 4 = ' & i * 4)
    }
fin
```