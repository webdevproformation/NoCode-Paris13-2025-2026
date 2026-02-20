from flask import Flask , render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, Regexp

application = Flask(__name__)


@application.route("/")
def home():
    return render_template("front/index.html")


class FormulaireInscription(FlaskForm):
    pseudo = StringField('pseudo', validators=[DataRequired(), Length(min=2, max=255)])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Regexp(regex='(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')])


@application.route("/register" , methods=["GET", "POST"])
def register():
    return render_template("front/register.html")

