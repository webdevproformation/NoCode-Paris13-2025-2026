import functools

from flask import Flask , render_template , redirect, url_for, request , session , flash , g
from dotenv import dotenv_values
from werkzeug.security import check_password_hash , generate_password_hash

from api.client import find_user_by , add_user
from utils.forms import FormulaireInscription , FormulaireConnexion

config = dotenv_values(".env")


application = Flask(__name__)
application.config['SECRET_KEY'] = config.get("FLASK_SECRET") # créer une SESSION


# Bonnes pratiques sécurité cookies session (adapte selon ton contexte HTTPS)
application.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    # SESSION_COOKIE_SECURE=True,  # Active-le si ton site est servi en HTTPS
)


# -------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------


# création d'une fonction décoratrice
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("Veuillez vous connecter pour accéder à cette page.")
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


def admin_required(view):
    @functools.wraps(view)
    def wrapped(**kwargs):
        if g.user is None:
            flash("Veuillez vous connecter pour accéder à cette page.")
            return redirect(url_for("login"))
        if g.user.get("role") != "admin":
            flash("Accès refusé.")
            return redirect(url_for("login"))
        return view(**kwargs)
    return wrapped


# -------------------------------------------------------------------
# Routes
# -------------------------------------------------------------------

@application.before_request
def load_logged_in_user():
    email = session.get('email')
    g.user = find_user_by("email",email) if email else None



@application.route("/")
def home():
    return render_template("front/index.html")


@application.route("/register" , methods=["GET", "POST"])
def register():

    form = FormulaireInscription()

    if form.validate_on_submit():

        # récupérer les données saisies
        pseudo = form.pseudo.data.strip()
        email = form.email.data.strip().lower()
        password = form.password.data

        # vérifier si il n'y a pas un profil utilisateur qui a déjà l'email saisi ??
        user = find_user_by("email" , email)

        if user is not None :
            flash("Cet email est déjà utilisé.", "warning")
            return render_template("front/register.html", form=form)

        password_hashed = generate_password_hash(password)

        new_user = {
            'pseudo': pseudo,
            'email': email,
            'password': password_hashed,
            'role': 'admin'
        } 

        add_user(new_user)
        application.logger.info('Nouveau profil créé: %s', pseudo)
        flash("Compte créé avec succès. Vous pouvez vous connecter.", "success")
        return redirect(url_for('login'))

    return render_template("front/register.html" , form=form)


@application.route("/login" , methods=["GET", "POST"])
def login():

    form = FormulaireConnexion()

    if form.validate_on_submit():

        email = form.email.data.strip().lower()
        password = form.password.data

        user = find_user_by("email",email)

        # Message unique pour éviter l'énumération d'utilisateurs
        invalid_msg = "Identifiants incorrects."

        if user is None:
            flash(invalid_msg , "warning")
            return render_template("front/login.html", form=form)

        stored_hash = user.get("password")
        if not stored_hash or not check_password_hash(stored_hash, password):
            flash(invalid_msg, "warning")
            return render_template("front/login.html", form=form)

        session.clear()
        session['email'] = user.get("email")
        application.logger.info('User %s vient de se connecter', session['email'])
        flash("Connexion réussie.", "success")
        return redirect(url_for('admin'))

    return render_template("front/login.html" , form=form )


@application.route("/dashboard")
@login_required
def admin():
    return render_template("back/dashboard.html")


@application.route('/logout')
def logout():
    session.clear()
    flash("Vous avez été déconnecté.", "info")
    return redirect(url_for('login'))
