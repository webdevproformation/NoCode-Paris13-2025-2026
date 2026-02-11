import requests 

reponse = requests.delete(
    "https://api.baserow.io/api/database/rows/table/836138/4/",
    headers={
        "Authorization": "Token fjNyGrfQGwwEx5ZCQAbYRedO4x9xSry7"
    }
)

print(reponse.content)