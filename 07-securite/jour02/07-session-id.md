# SESSION ID

lorsque vous vous connectez à un site internet le serveur va réponse 

- html 
- header de la requête => cookie de session => texte qui contient clé / valeur / durée de vie 
- SESSION ID => l'identifiant de se session 

-  PHPSESSID : l3r1ijlj6cesmulv2mk1gi6267
- 
- TRES TRES IMPORTANT => valeur ne doit pas être anticipable / prévisible 
- 
- Mettre le niveau de difficulté à Medium 
- retourner sur la page weaksession id 
- trouvé la fonction qui permet de déterminer la valeur de la session 
- 
- 
- set-cookie
	dvwaSession=1771250842

dvwaSession=1771250866


document.cookie = Date.now();