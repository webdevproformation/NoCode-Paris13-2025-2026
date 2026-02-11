import requests 

reponse = requests.post(
    "https://api.baserow.io/api/database/rows/table/836373/?user_field_names=true",
    headers={
        "Authorization": "Token 49MtB67hvPpMypGZuymP27iYwvs8JyWE",
        "Content-Type": "application/json"
    },
    json={
        "prenom": "Alain",
        "nom": "DOE",
        "age": 34
    }
)

print(reponse.content)