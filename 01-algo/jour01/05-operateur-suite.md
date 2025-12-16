# opérateurs 

## de calcul

```txt
+
- 
* 
/ 

%  modulo
^ puissance
div  partie entière de la division
```

## affectation

```txt
algo toto

variables
prix : float
unite : string 


debut
    prix = 12.5
    prix <-  12.5
    unite <- 'euro' // stocker du texte (string) dans la variable unite
                    // ATTENTION ATTENTION
                    // mot entouré de ' '  apostrophe quote string du texte
                    // mot entouré de " "  guillemet double quote string du texte
                    // mot entouré de ` `  backtick du texte
                    // mot entouré de <<<SQL  SQL  Heredoc du texte
                    // mot pas entouré mot clé du langage SOIT une variable
fin

```


## opérateurs de comparaison

```txt

> strictement supérieur
< strictement inférieur
>= > = supérieur ou égal 
<= < = inférieur ou égal
<> != ! = différent
== égal 
```


```txt
algo verif_password

variables
    password , formulaire : string
    verif  : bool

debut
    password <- 'azerty'
    formulaire <- 'bonjour'

    verif <- password == formulaire
fin
```


créer une nouvel algo qui s'appelle exo2
cet algo contient 4 variables 

prix_ht   chiffre à virgule
tva       chiffre à virgule
total_ttc chiffre à virgule 

dans la partie traitement
stocker dans la variable prix_ht la valeur 33.5
stocker dans la variable tva la valeur 1.2
stocker dans la variable total_ttc la multiplication de tva x prix_ht
 

```txt
algo exo2

variables
prix_ht , tva , total_ttc : float

debut
    prix_ht <- 33.5
    tva <- 1.2
    total_ttc <- prix_ht * tva
fin 
```



```txt
algo exemple

variables
total : int

debut
    total <- 10
    total <- total + 15 
fin 
```


## opérateurs boolean


```txt
&&  ET esperluet
||  OU  pipe 
!   NOT
```

sont utilisés pour effectuer des calculs sur des booléans (true / false)

=> lorsque vous vous connectez à un site internet (gmail)
=> on vous demande de saisir correctement un email ET un mot de passe
=> SI le email correspond ET le password correspond aux ceux en base de données ALORS c'est ok vous pouvez accéder à votre espace email
=> dans tous les autres cas 
    email ok mais password ko => NON
    email ko mais password ok => NON 
    email ko et password ko   => NON 


```
algo connexion_gmail

variables
    email_bdd, password_bdd , email_saisi , password_saisi : string 
    connexion_verif : bool 

debut
    email_bdd <- 'toto@yahoo.fr'
    password_bdd <- 'azerty'

    email_saisi <- Demander("saisir votre email")
    password_saisi <- Demander("saisir votre mot de passe")

    connexion_verif <- email_bdd        == email_saisi        && password_bdd == password_saisi
                       'toto@yahoo.fr'  ==  'toto@yahoo.fr'   &&  'azerty'    ==  'azerty'
                                    true                      &&         true 
                                                  true      
    
fin 
```