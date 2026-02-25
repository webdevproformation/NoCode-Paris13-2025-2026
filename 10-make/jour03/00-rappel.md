# rappel 

Par rapport à Zapier, Make dispose de nombreux modules `Build IN` qui permettent d'effectuer des traitements 

- Tools Variable / Agregation
- Parser : csv / json / xml / excel / text
- Control Flow 
    - Array Agregator
    - Iterator 
    - Router

```js
const a = [10, 20 ,30]

let total = 0

for(let i in a)
{
    total += i
}
```

# HTTP 

- créer des demandes à une autre machine : requête HTTP
- utiliser l'adresse d'une API : Application Program Interface 
- <https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita>
    - GET 
    - pas d'identification 
- appeler une base de données : `SELECT * FROM cocktails WHERE strDrink LIKE '%margarita%'`
- retourne un tableau au format JSON


Votre Application appelle -----> application tiers (base de données externe)


# Webhook 

créer une adresse interne

que l'on va mettre dans l'application tiers 
ET c'est lorsque l'on utilise l'application tiers => exécuter notre application

# JSON

- dans les valeurs pas de saut de ligne 
- clé et les valeurs OBLIGATOIREMENT entre guillemet " "
- pas de virgule sur la dernière valeur du json
- si on a besoin de mettre un saut de ligne dans une valeur, il faut utiliser `\n`

```text
coucou  les amis
 comment allez vous ??
```

```text
coucou  les amis \n comment allez vous ??
```

nl2br new line to br 

```html
coucou  les amis<br> comment allez vous ??
```

replace("<br>"; "\n")



```text
coucou  les amis                 comment allez vous ??
```

```html
coucou  les amis comment allez vous ??
```

```text
coucou  les amis&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment allez vous ??
```

```html
coucou  les amis          comment allez vous ??
```

```json

```



# INSERT 

combinaison d'outils nocode 

formulaire Tally

Make 
    - webhook
    - HTTP            - gestion erreur
    - Tools Variable  - gestion erreur
    - Mapping vers Google Sheet

Base de données Google Sheet
