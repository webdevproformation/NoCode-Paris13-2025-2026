# créer un scénario 

- Module trigger (horloge)
- connecté / réalisé les paramètrages
- cliquer sur Run Once (remplir de données le module)
- le petit chiffre en haut à droite (1)
    - Bundle => la manière dont les données vont être 
    - transmises dans les modules du scénario

- 2ème module Tool (module interne à Make) 
    - Set Multiple Variables
    - créer des variables 
        - nom à la variable
        - la valeur (donnée de l'étape précédente)
        - en + de la récupération de la valeur précédent 
        - vous pouvez appliquer une ou plusieurs fonctions 

500 * 1.2 
600,00 € TTC

champ_montant {{*}} 1.2 {{space}} €


function formatNumber ( variable ,      ){
}

formatNumber( variable ; 2 ; , ; {{space}} )

600 => 600,00
1200.5  => 1 200,50
1200.88888  => 1 200,88


si le montant de la facture > 1000 alors "bon client" else "client"


switch( $statut ; payé ; verifier le compte en banque ; en cours ; relance ; attendre )


```js
switch($statut){
    case "payé":
        return "verifier le compte en banque";
        break ;
    case "en cours":
        return "relance";
        break;
    default :
        return "attendre";
}
```

fonction qui permet de récupérer une valeur dans un tableau (array)

bundle client 2
{
    "client" : "Alain",
    "telephone" : [ '01010101' , '06060606'  ]
}



get(2client.telephone ; 1) permettre de récupérer le 1er téléphone du client 



phrase = [
    'bonjour',
    'comment',
    'vas tu?'
]

get(phrase , 1)

$user = {
    email : "toto@yahoo.fr",
    password : "123456",
    age : 24
}

pick($user , password)

omit($user, password)


# fonction mathématique

parseNumber()  => 20,5 attention étant donné qu'il y a une virgule dans le chiffre, c'est considéré pour du texte  => 20.5

formatNumber() transformer un chiffre en un chiffre formaté (c'est du texte)
               cette fonction permet d'intégré les règles d'écrire des chiffres dans une langue

                20510.8999   => 20 510,90
    

round() ceil() floor()

5000.30   round() => 5000
5000.50   round() => 5001

5000.30   ceil() => 5001
5000.50   ceil() => 5001 // toujours arrondi au dessus 

5000.30   floor() => 5000
5000.50   floor() => 5000 // toujours arrondi en dessous 


# Fonction de texte 

uuid => identifiant unique Unique User ID

trim()  '      prénom        ' => permet d'enlever les espaces en début et fin d'un texte
contains()  chercher si un texte est dans une phrase 
        $phrase =  "bonjour les amis"

        contains(bonjour ; $phrase) true
        contains(hello ; $phrase) false
        
split() "Alain DOE"  => [ "Alain" , "DOE" ]
length() le nombre de lettre dans un texte length(bonjour) 7


# Fonction de date

now => maintenant

formatDate( now ; MM/YYYY )

je veux récupérer les données du mois précédent 

formatDate(addMonths( now ; -1 ) ; MM/YYYY )

# fonction sur les tableaux 


join() // prendre chaque valeur d'un tableau => transformer en texte

["jasmin" , "rose" , "tulipe" ] join(["jasmin" , "rose" , "tulipe" ] ; ,) =>
                                jasmin,rose,tulipe

slice() => permet de prendre une partie d'un tableau
["jasmin" , "rose" , "tulipe" ] slice(["jasmin" , "rose" , "tulipe" ] , 1, 2)
                                ["rose" , "tulipe"]

first() => premier élement d'un tableau 
["jasmin" , "rose" , "tulipe" ] first(["jasmin" , "rose" , "tulipe" ]) => 
                                ["jasmin"]

["jasmin" , "rose" , "tulipe" , "jasmin" , "tulipe" ]
distinct() => enlève les doublons d'un tableau 
["jasmin" , "rose" , "tulipe" ]


Dans Google Sheet

créer une nouvelle feuille dans le fichier make qui s'appelle exo
dans cette feuille vous allez créer un tableau qui contient les valeurs suivantes

nom            |   email    |    adresse       |  age

Alain  Doe        a@y.fr      75 rue de Paris    30
Céline Pierre     c@y.fr      22 rue du Louvre   44
Zorro  DUPONT     a@y.fr      42 rue de Lyon     12

dans Make récupérer ces valeurs via le module Search Google Sheet

effectuer les traitements suivants 


nom            |   email    |  num  |   adresse       |  annee de naissance

Alain  DOE        a@y.fr      75    | rue de Paris       maintenant - 30 ans
Céline PIERRE     c@y.fr      22    | rue du Louvre      maintenant - 44 ans
Zorro  DUPONT     a@y.fr      42    | rue de Lyon        maintenant - 12 ans
 

get(split( nom ; {{space}} ) ; 1) {{space}} upper(get(split( nom ; {{space}} ) ; 2))

get(split( adresse , {{space}} ) ; 1 )

replace ( adresse ; first(split( adresse , {{space}} ) ) ; {{space}} )

formatDate( addYears( {{now}} ; - age ) , YYYY )

