# Créer un système de préévaluation automatique de CV 

plan d'action : 

1. dans tally 

    formulaire qui permet aux candidats de soumettre leur CV
        
        prenom
        nom
        email 
        menu deroulant 
            Developpeur
            Chef de Projet
            Designeur
        CV (document pdf)


Make 
    1 webhook pour récupérer les données saisies
    2 télécharger le CV dans mon google drive 
        HTTP file download
        le positionner dans google Drive (clé OAuth)
    3 Pdf.co
        -> prendre le texte du CV et le transformer en string 
    4 ChatGPT  (clé API chez OpenAI)
        - alimenter avec 2 prompts 
            - règle de l'évaluation
            - le contenu du CV
        - retourne un fichier json  contenant la note 
 
1. A la fin 
    1. Google Sheet
    
        tableau qui contient 
        prénom / nom / email / dt de soumission / note 

    1.  note entre 0 et 100 
    
    1. les CV transmis vont être stockés dans un dossier spécial dans votre Google Drive 


switch(  first(data.fields[4].value) ; 232fd874-4ced-4db9-8329-d050d8bfbf51 ; developpeur ; 9f6858cc-844f-4420-bbaa-185748af7942 ; Designeur ; Chef de projet  )


--

pour pouvoir télécharger (upload) des fichiers dans votre Google Drive
il faut générer 2 clé OAuth 

ID client :
Code secret du client :

- d'abord s'être connecté avec votre compte gmail 
- google cloud > console  <https://cloud.google.com/>
- créer une application => make 


--

aller sur le site :

https://pdf.co/
