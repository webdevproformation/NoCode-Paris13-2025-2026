# en 2 étapes 

## etape 1 

- register (inscription)
- formulaire dans lequel l'utilisateur va se créer un profil 
- CREATE dans la table users

- formulaire
    - email
    - pseudo
    - password

dans la base de données 
    - id 
    - email      => il faut que l'email soit UNIQUE 
    - pseudo
    - password   => hashé dans la base de données 
    - role 
    - dt-creation

# connexion (authentification)

formulaire 
    - email
    - password 

    - 1 requete select => vérifier est ce que l'email existe ??
    - si oui 
    - est ce que le password hashé correspond au mot de passe non hashé
    
    - si tout est OK alors python va nous retourner un cookie de session 

# autorisation 

dans les pages du back office nous allons ajouter un décorateur 
il va vérifier que le navigateur dispose bien d'un cookie de session valide 