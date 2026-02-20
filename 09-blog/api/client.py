import requests 


def find_user_by_email( email ):
    # SELECT * FROM users WHERE email = email
    reponse = requests.get(
        f"https://api.baserow.io/api/database/rows/table/849395/?user_field_names=true&search=email={email}",
        headers={
            "Authorization": "Token xxxxxxxxxxxxxxxxxx"
        }
    )
    return reponse.json().get("results")