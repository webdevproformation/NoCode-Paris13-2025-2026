import requests 

reponse = requests.post(
    "https://api.baserow.io/api/database/rows/table/836138/?user_field_names=true",
    headers={
        "Authorization": "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "Content-Type": "application/json"
    },
    json={
        "name": "Utiliser Python pour créer une application",
        "completed": True
    }
)

print(reponse.content)