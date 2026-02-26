# rappel de la journée



## processus complexe 

- tri de candidature 

- chaine de modules 
    - formulaire (Tally)
    - webhook 
    - créer des variables (facilité leur utilisation)
    - HTTP + Google Drive + Pdf.co 
    - ChatGPT
    - fichier excel (google sheet) - base de données

# Google Sheet (connexion)

- créer un compte utilisateur

# Baserow 

- token 

# Google Drive 

- OAuth + 2 clés : clé publique / clé privée + autorisé des adresses internet

--- 

# dernier gros outil dans le monde de l'automatisation

- Zapier
- make 
- n8n => si tu arrives à l'installer => autant que tu veux 

## installation n8n en local

- télécharger un logiciel qui s'appelle nodejs

```sh
# installation
npm i -g n8n

# lancer le logiciel
n8n
```

# make / zapier / n8n

zap / scénario / workflow (automatisation)
module         / noeud 

--- 

# make => Appel API     

- Make et j'ai besoin de faire une action (ajouter une ligne / supprimer / récupérer des infos ..) dans l'outil B 
- outil B  : google sheet / gmail / baserow / airtable ... met à disposition une API 

- adresse internet : https://.....
- méthode : GET / POST / PUT / DELETE 
- token   :  


HTTP 

Ajouter un nouveau profil étudiant

```sh
curl \
-X POST \
-H "Authorization: Token YOUR_DATABASE_TOKEN" \
-H "Content-Type: application/json" \
"https://api.baserow.io/api/database/rows/table/855610/?user_field_names=true" \
--data '{
    "prenom": "string",
    "nom": "string",
    "date naissance": "2020-01-01"
}'
```

récupérer un profil étudiant

```sh
curl \
-X GET \
-H "Authorization: Token YOUR_DATABASE_TOKEN" \
"https://api.baserow.io/api/database/rows/table/855610/{row_id}/?user_field_names=true"
```