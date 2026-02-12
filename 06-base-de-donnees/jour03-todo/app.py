from flask import Flask , render_template , request, redirect , url_for
# import depuis la librairie flask que l'on a téléchargé 
# la class Flask 

from api.client import get_all_todo , add_todo

app = Flask( __name__ )
# créer mon site internet qui va être stocké dans une variable qui s'appelle app 

# dans mon site internet je vais avoir une première page qui sera accessible depuis l'adresse / l'adresse de la page d'accueil
# si un utilisateur appele l'adresse / => Flask va exécuter la fonction home qui va retourner le texte "page d'accueil"

@app.route("/")
def home():

    fleurs = ["jasmin", "tulipe", 'lilas']
    etudiants = ["Alain" , "Céline" , "Zorro"]
    todos = get_all_todo()

    # print(todos)

    return render_template("index.html" , fleurs=fleurs , etudiants=etudiants , todos=todos)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new" , methods=["GET", "POST"])
def new():
    if request.method == "POST" :
        todo = request.form.get("name") # récupérer la valeur saisie dans le formulaire

        add_todo( todo ) # appeler l'API de baserow
        
        return redirect(url_for('home'))  # redirigé vers la page d'accueil

    return render_template("formulaire.html")
    

# flask run --debug # démarrer votre serveur de développement
# http://127.0.0.1:5000
# http://127.0.0.1:5000/contact