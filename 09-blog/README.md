# dépendances

```sh
pip install flask requests python-dotenv
```


# lancer le serveur de développement

```sh
# vous êtes dans l'environnement virtuel
# positionner dans le dossier racine du projet
flask --app application run --debug
# http://127.0.0.1:5000
```

## test e2e avec Playwright


```sh
pytest --headed --browser chromium
```

```sh
pytest --headed --browser chromium tests/test_register_negative.py::test_register_empty_submit_shows_errors
```