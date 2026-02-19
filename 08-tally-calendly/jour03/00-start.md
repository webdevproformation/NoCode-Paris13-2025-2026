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
- [] Update  20% il reste 80% à finir
- [] mettre en ligne sur un hébergeur => AWS 


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
    - [] remplir le formulaire 
        - => envoyer les données vers le formulaire
        - et les afficher
- l'utilisateur va réaliser des modifications dans le formulaire
    - lorsque l'on soumet 
    - UPDATE todo SET name="...." , completed = "True" WHERE id = 173 