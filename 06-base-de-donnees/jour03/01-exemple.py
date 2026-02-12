import requests

# SELECT * FROM todo 

reponse = requests.get(
    "https://api.baserow.io/api/database/rows/table/836138/?user_field_names=true",
    headers={
        "Authorization": "Token fjNyGrfQGwwEx5ZCQAbYRedO4x9xSry7"
    }
)

print(reponse.json())

## pour réaliser le CRUD sur les tables 
## nous allons utiliser des API 