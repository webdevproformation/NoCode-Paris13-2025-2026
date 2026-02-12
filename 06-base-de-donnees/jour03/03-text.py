# opération sur les textes

prenom = "Victor"
nom    = "Hugo"

auteur = prenom + " " + nom 
print(auteur)

prix = 10 
unite = "euro"

prix_complet = str(prix) + " " + unite

prix_complet = f"{prix} {unite}" # f-string
print(prix_complet)



duree = "20"
duree2 = 12

total_duree = int(duree) + duree2
print(total_duree)


# exemple concrêt

# "https://api.baserow.io/api/database/rows/table/836138/?user_field_names=true",

base_url =  "https://api.baserow.io/api"
payload = "/database/rows/table/"
table_id = 836138 

api = f"{base_url}{payload}{table_id}/?user_field_names=true"


question = input("donner votre prénom : ")

reponse = f"bonjour {question}"

print(reponse)

# créer le fichier 04-exo.py
# dans ce fichier vous allez poser deux questions
# quel est votre age 
# quelle est votre nom 

# afficher dans le terminal la phrase suivante 

# Bonjour nom_saisi vous avez age_saisie
