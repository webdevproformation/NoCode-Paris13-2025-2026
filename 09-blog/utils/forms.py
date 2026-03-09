from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, Regexp , EqualTo , ValidationError



def strict_email(form, field):
    forbidden = ["'", "&", "--", "<", ">", '"']
    if any(c in field.data for c in forbidden):
        raise ValidationError("Adresse email invalide")



class FormulaireInscription(FlaskForm):
    pseudo = StringField('pseudo', validators=[
        DataRequired(), 
        Length(min=2, max=255) ,
        Regexp(r"^[A-Za-z0-9_.]{2,255}$")
    ])
    email = EmailField('email', validators=[
        DataRequired(),
        Length(max=255),
        Email(),
        strict_email
    ])
    password = PasswordField('password', validators=[
        DataRequired(),
        Length(min=8, max=255 , message="Mot de passe invalide (doit contenir au moins 8 caractères avec lettres minuscule et majuscule, chiffres et caractères spéciaux)"),
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
            Email(),
            strict_email
    ])
    password = PasswordField('password', validators=[DataRequired()] )