from flask import Flask , render_template , request, redirect , url_for
# import depuis la librairie flask que l'on a téléchargé 
# la class Flask 

from api.client import get_all_todo , add_todo , delete_todo , get_todo_by_id

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
        todo = request.form.get("name") # récupérer la valeur saisie 
        # token = request.form.get("token")


        # dans le formulaire

        add_todo( todo ) # appeler l'API de baserow
        
        return redirect(url_for('home'))  # redirigé vers la page d'accueil
    
    token = "eofiheoruhze"

    return render_template("formulaire.html" , title="Ajouter un Todo")
    

@app.route("/delete/<todo_id>")
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for('home'))


@app.route("/update/<todo_id>")
def update(todo_id):

    todo = get_todo_by_id(todo_id)
    
    return render_template("formulaire.html" , title="Modifier un Todo", todo=todo)


# flask run --debug # démarrer votre serveur de développement
# http://127.0.0.1:5000
# http://127.0.0.1:5000/contact