pour réaliser la partie front d'un projet web 

- webflow
- mais vous pouvez aussi utiliser Python + framework qui s'appelle Flask 

# Architecture (l'organisation des dossiers / fichiers)

```txt

.venv/     => le code source de la librairie Flask
api/       => des fichiers qui vont appeler (CRUD) la base de données Baserow
templates/ => fichier html qui vont être la vue de notre application
static/    => ici que l'on créer nos css et nos js 
app.py     => LE POINT d'entrée de votre application (controller principal)
requirements.txt 
           => fichier qui va lister les dépendances (librairies externes) obligatoire pour faire fonctionner votre projet 
            par exemple Flask 
```

# comment créer dossier .venv et le fichier requirements.txt

- ces deux éléments ne doivent pas être créés à la main MAIS en ligne de commande

```sh
# créer le fichier .venv
python -m venv .venv
# .venv est à la fois un dossier qui contient des librairies externe ET
# environnement virtuelle pour python
# pour se positionner dans l'environnement virtuel 
# Windows
.venv\Scripts\activate
# Mac
.venv/bin/activate
# dans votre terminal vous voyez :
# (.venv) chemin/du/ dossier
# en fin vous pouvez installer les dépendances de votre projet 
pip install flask requests 
# cette commande installe les librairies flask et requests dans le dossier .venv

# enfin pour créer le fichier requirements.txt
pip freeze > requirements.txt

# lancer le serveur de développement de flask
flask run --debug
```



# focus sur le fichier app.py 

```py
# 3 parties dans ce fichier 

# Partie 1 
from flask import Flask , ....
from api.client import fonction1, fonction2, ....

# charger des fonctions qui sont écrites dans d'autres fichiers python
# soit dans le dossier .venv
# soit dans un dossier api qui contient le fichier client.py

# Partie 2 
# créer notre application web 
app = Flask(__name__)

# Partie 3 => routes toutes les pages de votre site internet  
# page d'accueil
# page mention-legale
# page contact
# page connexion 

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/mention-legale")
def mention_legale():
    return render_template("mention-legale.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# dans le cas où j'ai une page qui contient un formulaire que je veux gérer moi même 
@app.route("/connexion", methods=["GET", "POST"])
def connexion():

    if request.method == "POST": # je vérifie que le formulaire est soumis
        # récupérer les valeurs saisies 
        # verifier que les données saisies sont conformes 
        # envoyer à la base de données 
        # si tout est ok => 
        # si ko 

    return render_template("connexion.html")


# dashbord => page d'accueil du backoffice 
@app.route("/dashboard")
@is_admin() # il faut disposer le navigateur dispose d'un cookie de session 
def dashboard():
    return render_template("dashboard.html")
```



