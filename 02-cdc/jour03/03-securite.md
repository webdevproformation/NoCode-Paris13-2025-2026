# Sécurité 

- site internet => pirate informatique
- prendre le controle de votre site / projet 
- il va essayer de faire INJECTION de code 
- ajouter SON code DANS votre code 


# INJECTION SQL 

- je vais réussi à accéder au compte de l'administrateur (le gestionnaire) dans connaitre son login et son mot de passe 

- exemple => utiliser un site qui a spécialement conçu pour être vulnérable aux injections SQL
- OWASP (association qui s'est donné comme mission de mettre à disposition de la documentation / pour comprendre de manière claire INJECTION SQL) 

- google > altoromutual owasp 
- https://demo.testfire.net/

- https://demo.testfire.net/login.jsp
- 
- login : blabla
- password : 12345 


- login : ' OR 1=1 -- # => SQL que l'on va donner au site qui va l'ajouter au code sql  site internet  
- password : 1


```sql
SELECT * FROM users WHERE login = 'blabla' AND password = '12345'
```


```sql
SELECT * FROM users WHERE login = '&ezfoi OR 1=1 --' AND password = '1'
```

```sql
SELECT * FROM users WHERE login = :login AND password = :password 

execute([
    "login" => "' OR 1=1 --",
    "password" => '1'
])
```

## Vol de base de données

<https://informationisbeautiful.net/visualizations/worlds-biggest-data-breaches-hacks/>