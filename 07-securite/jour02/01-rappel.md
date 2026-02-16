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

    - INJECTION SQL 

    - `Alain' #`
    - 
    - `SELECT * FROM users WHERE nom = 'Alain'  #'`
    - 
    - `Alain' OR 1 = 1 #`
    - `Alain' UNION SELECT login , passward FROM users #`


- injection de fichier 
    - formulaire qui permet de télécharger des fichiers => pdf / image 
    - vous vérifiez peu ou pas le contenu téléchargé 
    - l'attaque pas gentil va télécharger un fichier php qui contient un code que l'on peut appeler une backdoor 

---

CTF => Capture The Flag


# nouveau lien pour accéder au site DVWA 

<https://8a34-109-190-31-225.ngrok-free.app>



- injection Javascript => XSS 