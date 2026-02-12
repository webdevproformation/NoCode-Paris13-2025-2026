import requests


def get_all_todo():
    reponse = requests.get(
        "https://api.baserow.io/api/database/rows/table/836138/?user_field_names=true",
        headers={
            "Authorization": "Token fjNyGrfQGwwEx5ZCQAbYRedO4x9xSry7"
        }
    )

    return reponse.json().get("results")


def add_todo(todo):
    """ fonction qui permet d'ajouter une nouvelle tache dans la table todo  """
    requests.post(
        "https://api.baserow.io/api/database/rows/table/836138/?user_field_names=true",
        headers={
            "Authorization": "Token fjNyGrfQGwwEx5ZCQAbYRedO4x9xSry7",
            "Content-Type": "application/json"
        },
        json={
            "name": todo,
            "completed": False
        }
    )