# fonction 


en informatique : variable qui permet de stocker un ou plusieurs valeurs 

```txt

variables
    phrase : string
    prix : float
    jours : array : string 

debut
    phrase <- "bonjour les amis"
    prix <- 22.5
    jours <- [ 'Lundi' , 'Mardi' , 'Mercredi' ]
fin
``` 

**une fonction : c'est comme une variable MAIS on va stocker un algo**


```
algo facture

variables 
    prix1 , prix2 , tva , prix1_ttc , prix2_ttc : float 

debut

    prix1 <- 10.5
    tva <- 1.2
    prix1_ttc <- tva * prix1


    prix2 <- 40.5
    tva <- 1.2
    prix2_ttc <- tva * prix2
    

fin 
```




```
algo facture


fonction calcul_ttc(prix)
    tva <- 1.2
    prix_ttc <- tva * prix

variables 

debut

    calcul_ttc(10.5)

    calcul_ttc(40.5)
    
fin 
```
