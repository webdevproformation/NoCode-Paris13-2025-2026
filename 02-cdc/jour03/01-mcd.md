# Le coeur de tout programme / logiciel

- Base données 

- ça ressemble beaucoup à un fichier Excel 

- fichier => Base de données
- chaque feuille du fichier excel => Table (qui stocke un concept)
        - table client 
        - table commande
        - produit 
- tableau  qui est composé de colonnes 

- chaque colonne contenir des données informations 


---

je veux créer un logiciel qui permet de suivre l'ensemble de mes travaux 


table Todo (tâche)

- nom : texte qui contient au maximum 255 lettres
- date de debut : JJ/MM/AAAA
- date de fin  : JJ/MM/AAAA
- status : à faire / en cours / fait 

table Projet 

- nom 
- description 
- RELATION avec la table TODO
- RELATION avec la table client 

table client 

- nom 


# cas pratique

je souhaite ajouter la possibilité de gérer mes factures 

créer une table facture

contient les colonnes 

numéro de facture
montant 
dt emission
statut  : en attente de paiement / payée


Le relation (bi directionnelle) avec la table client 