# boucle 

## Pour

1. i <- 1      // incrément qui contient la valeur de départ de la boucle 
2. i < 5       // condition de sortie de la boucle => valeur max de l'incrément
3. i <- i + 1  // augmentation de l'incrément  

```txt

Pour( i <- 1 ; i < 5 ; i <- i +1 ){
    traitement 
}
```

## TantQue (While)


```txt
algo boucle_while

variables
    i : int

debut
    // avant la boucle TantQue
    // créer l'incrément 
    i <- 1 

    TantQue ( i < 5  ){ // condition de sortie
        traitement 
        i <- i + 1     // augmentation
    }
fin
```

# cas pratique 

- créer l'algo `exo8` qui contient une boucle `TantQue`
- cette boucle va permettre d'afficher le texte suivant

```txt
10 €  i = 10    i & ' €'
20 €
30 €
40 €
50 € 
```

min 10
max 50  <= 50 ou < 51
augmentation + 10 


```txt
algo exo8

variables
    i : int

debut
    i <- 10 
    
    TantQue( i < 51 ){
        Ecrire( i & ' €' ) // 10 & ' €' => '10 €'
        i <- i + 10
    }
fin
```

# exo

créer l'algo nommé `exo9`  l'objectif est d'écrire le losange suivant

```txt
-x-
xxx
-x-
```

3 lignes et chaque ligne contient 3 caractères

```txt
-x-
123
```

ligne1 <- '-x-'


ligne1 <- '-'
ligne1 <- ligne1 & 'x'
ligne1 <- ligne1 & '-'


```txt
algo exo9

variables
    ligne : int

debut
    ligne <- ''

    Pour(i <- 1 ; i < 4 ; i <- i + 1){
        Si i != 2 alors
            ligne <- ligne & '-'
        Sinon
            ligne <- ligne & 'x'
    }
    
    ligne <- & 'xxx'
    
    
    Pour(i <- 1 ; i < 4 ; i <- i + 1){
        Si i != 2 alors
            ligne <- ligne & '-'
        Sinon
            ligne <- ligne & 'x'
    }
fin
```



total <- 10
total <- total + 2
total <- total + 5





--x--
-xxx-
xxxxx
-xxx-
--x--