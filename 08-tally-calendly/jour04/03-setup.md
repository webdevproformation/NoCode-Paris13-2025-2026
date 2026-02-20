# set up python

- création de l'environnement virtuel 
- créer le dossier
    - .ebextensions
        - app.config
    - api
    - static
    - templates
    - application.py
    - requirements.txt
    - .env => fichier qui contient les informations SECRET de notre code 
    - .env.example 

Installation des dépendances de notre projet 

```sh
pip install flask requests python-dotenv 
# ...
```

pour le fichier requirements.txt  (à réaliser avant le déploiement)

```sh
pip freeze > requirements.txt
```

# création de l'environnement virtuel



```sh
python -m venv .venv
.venv\Scripts\activate
pip install flask requests python-dotenv
```

