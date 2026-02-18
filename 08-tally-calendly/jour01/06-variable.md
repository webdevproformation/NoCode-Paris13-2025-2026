# lorsque vous réalisez un formulaire 

-> poser des questions 
-> vous pouvez donner une note aux réponses données pour l'utilisateur
-> cette note peut vous permettre de préclasser les réponses intéressantes

=> combinaison de 3 choses
    - des champs de formulaire
    - un block / block conditionnel
    - une variable 
    - 

let score = 0 

if(document.querySelector(".marque").value === "Renault"){
    score += 3
}

if(document.querySelector(".ville").value === "Seine Denis"){
    score += 3
}

console.log(score)

# cas pratique 

vous devez créer un formulaire qui va permettre de donner une estimation du montant total d'un projet (estimation pour un devis)


- Question 1 

Ravalement de façade

superficie à traiter (menu déroulant)

10m²  => 1000€
20m²  => 2000€
30m²  => 2500€

- Question 2

option isolation (menu déroulant)

oui  => 900€
non  => 0 

afficher à la fin du formulaire un montant estimé de la prestation 

réaliser une petite mise en page sur formulaire pour le rendre attractif

