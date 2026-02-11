
# requête HTTP 
# requête ajax 
# demande à la base de données de lui retourner une ligne
# SELECT * FROM todo WHERE id = 1
# pour pouvoir exécuter cette requête http 
# il faut installer une librairie python qui s'appelle requests 
# on va utiliser un outil en ligne de commande qui s'appelle pip 
# Package Installer for Python
# pip install requests

import requests

reponse = requests.get(
    "https://api.baserow.io/api/database/rows/table/836138/?user_field_names=true",
    headers={
        "Authorization": "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
)

print(reponse.content)

## exécuter mon code il faut se positionner dans le dossier qui contient le fichier que vous êtes entrain de regarder