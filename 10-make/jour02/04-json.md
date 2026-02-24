# rappel sur le format JSON


```json
{
    "prenom" : "nom"
}
```

```json
{
    "prenom" : 'erreur'
}
```

Attention aux sauts de lignes


```json
{
    "prenom" : "bonjour
comment cv ??"
}
```


```json
{
    "prenom" : "bonjour \n comment cv ??"
}
```

le dernier élément d'un JSON ne doit pas avoir de , à la fin 

```json
{
    "prenom" : "bonjour \n comment cv ??",
    "nom" : "DUFOUR"
}
```

chiffre / boolean / objet / tableau 

```json
{
    "prenom" : "Alain",
    "age" : 10,
    "prix" : 10.3,
    "is_admin" : true,
    "is_connected" : false 
}
```
si dans un texte vous avez des guillemets, il faut les échapper 


```json
{
    "prenom" : "toto \" dieoizj \" ",
}
```