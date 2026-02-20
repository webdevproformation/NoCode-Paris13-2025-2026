# question 

- AWS
- google > aws console 
- <https://aws.amazon.com/fr/console/>
- sign in > 
    - prendre l'utilisateur Root
    - login : votre email
    - password : saisir votre password 
    - MFA : Multi Factor Authentification 
        - 2FA double authentification 
            - SMS
            - email 
            - logiciel (application mobile) xxxx

# rappel

- finit le projet Todo
- découvert comment ajouter nos css / nos javascript dans un projet Python Flask
    - créer un dossier `static` à la racine de votre projet
    - dans le fichier `base.html` ajouter 
    - `<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">`
    - `<script src="{{ url_for('static', filename='js/script.js') }}"></script>`
- nous avons préparé notre projet pour le déployer sur AWS
    - modifié le nom de app.py => application.py
    - dans le fichier modifié la variable `app = Flask(__name__)` par `application = Flask(__name__)`
    - modifié les routes `@app.route()` => `@application.route()`
    - créer un dossier qui s'appelle `.ebextensions` qui un fichier `app.config`
    
```yml
option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath: application:application
```

# lancement le serveur HTTP pour Python 

```sh
flask run --debug 
flask --app app run --debug 
flask --app application run --debug 
```

- zipper notre projet 
    - .ebextensions/
    - api/
    - templates/
    - static/
    - application.py
    - requirements.txt

- créer un serveur Elastic Beanstalk et migration du fichier zip 
