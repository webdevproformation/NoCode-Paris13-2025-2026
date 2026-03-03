# Groupe 1 - sujet 1

- pas de question

---

# Groupe 2 - sujet 2

- pas de question


# pour la pause : installation n8n en local

- [x] installation docker
- installation n8n


# Docker 

- pour que n8n fonctionne => il a besoin (dépendance) de nodejs 
- un outil qui permet de créer un environnement de travail pour que n8n fonctionne 

# dans le dossier en cours

1. créer un fichier docker-compose.yml
2. remplir avec le texte suivant 


```yml
services: # créer 2 machines
    postgres: # postgres => base de données
        image: ..... # docker va télécharger l'image postgres:17 depuis le site internet qui s'appelle dockerhub 

    n8n: # notre logiciel 
        image: ..... # docker va télécharger l'image docker.n8n.io/n8nio/n8n depuis le site internet qui s'appelle dockerhub 
        ports:
            - 5678:5678 # => est accessible en saissant l'adresse 
            - # http://localhost:5678
``` 

dans le fichier docker-compose.yml vous pouvez voir des variables ${POSTGRES_DB}
et pour les définir il suffit de créer un fichier `.env`

# enfin pouvoir installer et utiliser n8n

```sh
# créer l'ensemble des conteneurs décrits dans le fichier docker-compose.yml
docker compose up -d --build

# supprimer l'ensemble des conteneurs décrits dans le fichier docker-compose.yml
docker compose down
```