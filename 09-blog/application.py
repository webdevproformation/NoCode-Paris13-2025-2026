from flask import Flask , render_template , redirect, url_for, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, Regexp

from api.client import find_user_by_email

application = Flask(__name__)
application.config['SECRET_KEY'] = "354168746584" # créer une SESSION


@application.route("/")
def home():
    return render_template("front/index.html")


class FormulaireInscription(FlaskForm):
    pseudo = StringField('pseudo', validators=[DataRequired(), Length(min=2, max=255)])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()] )


@application.route("/register" , methods=["GET", "POST"])
def register():

    form = FormulaireInscription()

    if form.validate_on_submit():

        # récupérer les données saisies
        pseudo = request.form.get("pseudo")
        email = request.form.get("email") 
        password = request.form.get("password")

        # vérifier si il n'y a pas un profil utilisateur qui a déjà l'email saisi ??

        verif = find_user_by_email(email)

        print(verif)

        # si oui => message d'erreur

        # sinon => INSERT 

        return redirect(url_for('home'))

    return render_template("front/register.html" , form=form)

