import requests


def get_all_todo():
    reponse = requests.get(
        "https://api.baserow.io/api/database/rows/table/836138/?user_field_names=true",
        headers={
            "Authorization": "Token jozQdkmfa0YIvJrhQqADDAgrkR9q0vFm"
        }
    )

    return reponse.json().get("results")


def add_todo(todo):
    """ fonction qui permet d'ajouter une nouvelle tache dans la table todo  """
    requests.post(
        "https://api.baserow.io/api/database/rows/table/836138/?user_field_names=true",
        headers={
            "Authorization": "Token jozQdkmfa0YIvJrhQqADDAgrkR9q0vFm",
            "Content-Type": "application/json"
        },
        json={
            "name": todo,
            "completed": False
        }
    )

def delete_todo(todo_id):
    """ fonction qui permet de supprimer une todo via son id (clé primaire) """
    requests.delete(
        f"https://api.baserow.io/api/database/rows/table/836138/{todo_id}/",
        headers={
            "Authorization": "Token jozQdkmfa0YIvJrhQqADDAgrkR9q0vFm"
        }
    )