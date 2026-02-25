# processus

etape1

INPUT  => texte
OUTPUT => tableau / rien

etape2

INPUT tableau
OUTPUT bundle 


```js
const a = [];

for(let i in a)
{
    // ....
}

//
```

```js
try{
    const a = [];

    for(let i in a)
    {
        // ....
    }
}catch( erreur ){
    # envoi un email
    # écrire dans les logs 
    return new Error({ status: 404 , data : { message : .... }  })
}

// ...
```

# 5 modules qui permettent de gérer les cas d'erreurs

- commit / rollback 
- module spécial pour les modules qui communique avec la base de données ou ACID (Atomicity, Consistency, Isolation et Durability)
    - si au cours du process il y a plusieurs insert / update / delete
    - ET que un des traitements n'est pas exécuté correctement 
    - ROLLBACK => aucun n'est exécuté 

- Ignore => si erreur stop ignore le module 

- Break => permet de relancer le module si erreur 
        => vous pouvez définir le nombre de tentative et la durée entre chaque tentative

- Resume 
    - module qui va donner des valeurs par défaut si son exécution est compromise
    - 
OAuth