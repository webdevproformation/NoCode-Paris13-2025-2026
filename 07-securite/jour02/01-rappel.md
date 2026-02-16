# dès que vous avez un site internet

avec Base de données et / ou moyen de paiement => grande chance d'être attaqué

# association OWASP 

- donné comme objectif de créer / publier du contenu pour sensibilité à la sécurité informatique 
- nous allons utiliser le projet DVWA : Damned Vulnerable Web Application pour découvrir les attaques classiques sur un site internet 


# attaque par dictionnaire / attaque par brut force 

- page de connexion (login / password)
- script / outil (burpsuite) qui va tester un tableau de 1000 password 

# injection 

les fait de pouvoir faire au site internet PLUS que ce que le développeur avait prévu 
formulaire dans lequel le développeur à prévu que vous écriviez
un chiffre 
Mais l'attaquant va saisir un chiffre + du code à injecter

- injection de commande 
    formulaire => je dois saisir une valeur  `127.0.0.1`
    et cette valeur va être utilisé dans le code pour exécuter une commande 

    `ping 127.0.0.1` 

    formulaire => je dois saisir une valeur  `127.0.0.1 | ls -al`

    `ping 127.0.0.1 | ls -al`  => la partie après la barre vertical est la commande injectée 

    vous pouvez remplacer ls par cat (lire) / rm (supprimer) / mv (changer le nom d'un fichier) ... 

- injection sql 
    - formulaire => je demande saisir un nom d'utilisateur pour le rechercher => Alain
    - 
    - `SELECT * FROM users WHERE nom = 'Alain'`

    - `Alain' #`


- injection de fichier 

- injection Javascript => XSS 