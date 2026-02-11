import requests 

reponse = requests.delete(
    "https://api.baserow.io/api/database/rows/table/836138/4/",
    headers={
        "Authorization": "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
)

print(reponse.content)