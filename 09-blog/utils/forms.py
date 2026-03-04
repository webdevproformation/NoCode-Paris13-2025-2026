from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, Regexp , EqualTo


class FormulaireInscription(FlaskForm):
    pseudo = StringField('pseudo', validators=[
        DataRequired(), 
        Length(min=2, max=255)
    ])
    email = EmailField('email', validators=[
        DataRequired(),
        Length(max=255),
        Email()
    ])
    password = PasswordField('password', validators=[
        DataRequired(),
        Length(min=8 , message="Le mot de passe doit contenir au moins 8 caractères."),
        Regexp(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!?*\.,;:~]).{8,}$", message="Mot de passe invalide (doit contenir au moins 8 caractères avec lettres minuscule et majuscule, chiffres et caractères spéciaux)")
    ] )
    
    confirm_password = PasswordField(
        "confirm password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Les mots de passe ne correspondent pas."
            )
        ]
    )


    


class FormulaireConnexion(FlaskForm):
    email = EmailField('email', validators=[
            DataRequired(),
            Length(max=255),
            Email()
    ])
    password = PasswordField('password', validators=[DataRequired()] )