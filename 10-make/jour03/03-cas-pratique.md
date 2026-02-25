# Créer un système de préévaluation automatique de CV 

plan d'action : 

1. dans tally 

    formulaire qui permet aux candidats de soumettre leur CV
        
        prenom
        nom
        email 
        CV (document pdf)


Make 
    1 webhook pour récupérer les données saisies
    2 télécharger le CV dans mon google drive 
        HTTP 
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
    2. les CV transmis vont être stockés dans un dossier spécial dans votre Google Drive 
