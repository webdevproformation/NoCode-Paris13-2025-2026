## Objectif 

- créer un projet hybride 
- 60% NoCode
- 40% Code  => max 300 lignes de code 


## aujourd'hui

- la dernière action du CRUD 
- Lire des Todos => page d'accueil
- Supprimer des Todos => page d'accueil
- Créer des Todos => formulaire 


- [x] ajouter du css et js
- [x] Update  20% il reste 80% à finir
- [] mettre en ligne sur un hébergeur => AWS et Elastic Beanstalk


# ajouter du css dans un projet Python Flask

1. créer un nouveau dossier dans `jour03-todo` => `static` (respecter le nom)
1. Dans ce dossier, vous pouvez créer autant de dossier que vous voulez avec le nom de vous voulez, 
1. je vais créer 3 sous dossiers
    1. img
    1. js
    1. css 
1. dans le dossier css, je vais créer un fichier `style.css` 
1. dans le fichier vous allez écrire

```css
body{
    background: grey;
}
```

1. dans le fichier `base.html` dans le dossier templates, il faut ajouter avant la balise `</head>` => 
1.  `<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">`


Maintenant je peux tester 

1. http://127.0.0.1:5000 

---

#  Update  20% il reste 80% à finir

- lorsque je clique sur le bouton modifier => formulaire 
- remplir le formulaire avec des données stockées dans la table Todo 
    - [x] SELECT * FROM todo WHERE id = 173 
        - je suis allé sur documentation de Baserow => récupérer la requête API "lire une ligne"
        - je suis allé dans le fichier client.py et j'ai une fonction qui utilise le code de l'api
        - je suis allé dans le fichier app.py et j'ai importé la fonction
    - [] remplir le formulaire 
        - dans la route update 
        - j'ai exécuter la fonction importée
        - et j'envoie les infos à la vue (j'ajoute un nouveau paramètre à la fonction render_template( , todo=todo))
        - => envoyer les données vers le formulaire
        - et les afficher
        - ajouté dans le formulaire un attribut value={{ todo.name if todo else '' }}
        - ajouté dans le formulaire un attribut {% if todo and todo.completed %}checked{% endif %}
        - 
        - `<input type="checkbox"  >` carré non coché
        - `<input type="checkbox" checked >` carré coché
        - je ne vérifique QUE si completed est True 
        - 
- l'utilisateur va réaliser des modifications dans le formulaire
    - lorsque l'on soumet 
    - on fait un POST => il faut l'ajouter dans la route methods=["GET", "POST"]
    - UPDATE todo SET name="...." , completed = "True" WHERE id = 173 


# Objectif atteint MAIS

- très très gros problème de sécurité 
- token => diffusé sur github 
- plein de formulaire MAIS aucune vérification avant de lancer le traitement en base de données
- il reste plein de code à ajouter en + pour le projet soit fonctionnel ET sécure 


# Déploiement

lorsque votre projet est prêt en local (dans votre ordinateur)
le mettre sur internet 
copier votre code => coller sur un ordinateur qui a pour rôle de 
    - fonctionner 24h sur 24h / 7jours /7
    - répondre lorsque on l'appelle via une adresse internet 
    - ordinateur => SERVEUR 

société qui vont louer des serveurs => hébergeurs 

    - OVH (société leader en france qui propose des serveurs)
    - <https://www.ovhcloud.com/fr/>
    - 
    - <https://www.nuxit.com/pack-etudiant/>

    - AWS (Amazon Web Service) => hébergement et en plus système qui permet 
        - de créer autant de serveur que vous avez besoin 
        - préinstaller des logiciels dans ces machines 
        - xxxx 
        - 

# Elastic Beanstalk
 
<https://aws.amazon.com/fr/elasticbeanstalk>

# avant de lancer la migration 

il faut préparer notre code 

1. renommer le fichier `app.py` en `application.py`
