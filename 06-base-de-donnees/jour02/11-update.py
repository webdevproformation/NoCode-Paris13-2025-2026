import requests

reponse = requests.patch(
    "https://api.baserow.io/api/database/rows/table/836373/3/?user_field_names=true",
    headers={
        "Authorization": "Token 49MtB67hvPpMypGZuymP27iYwvs8JyWE",
        "Content-Type": "application/json"
    },
    json={
        "nom": "DUPONT",
        "age": 49
    }
)

print(reponse.content)