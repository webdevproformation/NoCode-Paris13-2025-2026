support 

- https://formation.webdevpro.net/securite/
- login : secu
- password : rite


# ngrok 

```sh
ngrok http http://localhost:8080/
```


<https://38d5-2a01-cb04-5f0-fb00-64be-2ed3-4a57-746e.ngrok-free.app/login.php>


# demande auprès de site internet 

requete http adresse internet : https://monsupersite.fr/ressource

méthode => 4 méthodes de base

GET         => récupérer de l'information / 
POST        => Formulaire et je veux ajouter l'informations du formulaire dans ma base de 
            données
PUT / PATCH => je veux mettre à jour un enregistrement dans ma base de données
DELETE      => supprimer un enregistrement dans mon serveur ()

CRUD dans une base de données au niveau SQL 
    Create => INSERT
    Read   => SELECT
    UPdate => update
    Delete => Delete

pour le procole HTTP il existe aussi 4 méthodes qui permettent de donner des intructions au serveur
    Create => POST 
    Read   => GET 
    Update => PUT / Patch
    Delete => Delete


Code statut des serveurs
Code 200 => tout s'est bien passé
code 302 => redirection
Erreur 400 => erreur dans le requête 
Erreur 401 => pas autorisé il faut au préalable être connecté
Erreur 404  => get  article 10 => erreur 404 
Erreur 500 => bug 