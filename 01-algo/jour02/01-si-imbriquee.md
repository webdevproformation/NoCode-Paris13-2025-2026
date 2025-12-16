# le SI imbriqué

// on a plusieurs rôles dans notre projet

// admin
// rédacteur
// traducteur
// commentateur 

et pour chaque catégorie d'utilisateur => page dédiée 

// SI ALORS SINON

```txt
algo page_dediee

variables
    role : string

debut
    role <- 'admin'
    
    SI role == 'admin'
        Ecrire("page admin")
    SINON
        SI role == 'rédacteur'
            Ecrire("page rédacteur")
        SINON
            SI role == 'traducteur'
                Ecrire("page traducteur")
            SINON
                SI role == 'commentateur'
                    Ecrire("page commentateur")
                SINON
                    Ecrire("Role inconnu ????")
fin 
```

# autre syntaxe disponible => SELON variable FAIRE 

```txt
algo page_dediee

variables
    role : string

debut
    role <- 'admin'

    SELON role FAIRE
        'admin'        : Ecrire("page admin")
        'rédacteur'    : Ecrire("page rédacteur")
        'traducteur'   : Ecrire("page traducteur")
        'commentateur' : Ecrire("page commentateur")
    SINON
        Ecrire("Role inconnu ????")

fin 
```

```php

$role = 'admin' ;

switch($role) {
    case 'admin' : echo 'page admin' ; break ;
    case 'rédacteur' : echo 'page rédacteur' ; break ;
    case 'traducteur' : echo 'page traducteur' ; break ;
    case 'commentateur' : echo 'page commentateur' ; break ;
    default echo 'Role inconnu ????' ;
} 

if($role == 'admin'){
    echo 'page admin' ;
}else if($role == 'rédacteur'){
    echo 'page rédacteur' ;
}else if($role == 'traducteur'){
    echo 'page traducteur' ;
}else if($role == 'commentateur'){
    echo 'page commentateur' ;
}else {
    echo 'page Role inconnu ????' ;
}    
```

# exo créer le script exo3

dans cet algo vous créez une variable qui s'appelle ville et qui contient le texte Paris

dans l'algo, vous allez écrire les traitements suivants 
si ville contenait la valeur Paris Ecrire "votre code postal est 75000"
si ville contenait la valeur Marseille Ecrire "votre code postal est 13000"
si ville contenait la valeur Lyon Ecrire "votre code postal est 69000"
si ville contenait la valeur Bourg en Bresse Ecrire "votre code postal est 01000"
sinon afficher Ecrire code postal inconnu


```txt
algo exo3

variables
    ville : string 

debut
    ville <- 'Paris'
    
    SELON ville FAIRE 
        'Paris'            :  Ecrire("votre code postal est 75000")
        'Marseille'        :  Ecrire("votre code postal est 13000")
        'Lyon'             :  Ecrire("votre code postal est 69000")
        'Bourg en Bresse'  :  Ecrire("votre code postal est 01000")
    SINON
        Ecrire("code postal inconnu")
    
fin
```