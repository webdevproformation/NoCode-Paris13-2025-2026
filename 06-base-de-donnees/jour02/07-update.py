import requests 

reponse = requests.patch(
    "https://api.baserow.io/api/database/rows/table/836138/4/?user_field_names=true",
    headers={
        "Authorization": "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "Content-Type": "application/json"
    },
    json={
        "name": "Finaliser le projet coucou les amis",
        "completed": False
    }
)

print(reponse.content)