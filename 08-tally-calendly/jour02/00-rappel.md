# Tally

- application NoCode 
- de type Form Builder => créer des formulaires
- au niveau de la manière d'utiliser Tally => très inspiré d'un autre outil NoCode => Notion 
- le principe c'est de créer des formulaires comme on crée une page 
- ajouter des block l'un après l'autre 

# block 

- comme de balises html d'un formulaire => Dropdown (menu déroulant)

-  <select required hidden minlength="" maxlength="">
    - <option value="France">France</option>
    - <option value="Italie">Italie</option>
-  </select>
- 
- mais aussi des balises h1 h2 p img embed (google map)
- créer même des pages (parcours utilisateur)

# block spéciaux 

- block logique => SI le champ X contient une valeur ALORS traitement
- block variable => d'avoir une valeur qui est calculée en fonction des valeurs sélectionnées dans les champs du formulaire 
- Paiement via Stripe
- Signature 


# une fois que le formulaire est prêt

- le diffuser 
    - via un lien (dans un email)
    - via une balise iframe 
- mettre en place des automatisations 
    - soit les automatisations sont NATIVES (Airtable)
    - soit il faut utiliser Zapier pour faire communiquer votre formulaire avec BaseRow  