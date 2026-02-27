# rappel 

- 2 gros exos / cas pratiques (préparation Hackaton)

- formulaire (Notion / tally)
- make 
- Base de données Baserow / Airtable

# Notion 

- faire communiquer Notion avec Make 
- créer une clé API dans Notion
    - ... > Connexion > créer une connexion interne > clé
    - associer la clé à la base dans Notion 

# Make

- module interne Airtable / Baserow => ROUGE erreur 
- 1er reflexe lire le message d'erreur 
    - 400 / 401 / 403 => lié à une erreur dans la clé API
    - parsing 
        - récupérer une info en format 01/01/2026 mais dans la base elle est attendue 2026-01-01
        - `Basse` dans Notion et `basse` de Baserow 
- module HTTP de Make  
        - refaire une requête API à la main 


```sh
curl \
-X GET \
-H "Authorization: Token YOUR_DATABASE_TOKEN" \
"https://api.baserow.io/api/database/rows/table/829570/{row_id}/?user_field_names=true"
```

```sh
curl \
-X PATCH \
-H "Authorization: Token YOUR_DATABASE_TOKEN" \
-H "Content-Type: application/json" \
"https://api.baserow.io/api/database/rows/table/829570/{row_id}/?user_field_names=true" \
--data '{
    "Nom": "string",
    "Nom de famille": "string",
    "Notes": "string",
    "Actif": true
}'
```

# Airtable 

- <https://airtable.com/create/tokens>
- Attention lors de la création de la clé bien sélectionner les valeurs suivantes dans la `portée`
    - data.records:read
    - data.records:write
    - schema.base:read
    - schema.base:write

- token => make  


# exemple du MCD (Modèle Conceptuel des Données) d'un site e commerce (comme prestahop)

- <https://i.pinimg.com/originals/9a/55/cf/9a55cf03e68bdfe6ba7504bac1f4b87d.png>