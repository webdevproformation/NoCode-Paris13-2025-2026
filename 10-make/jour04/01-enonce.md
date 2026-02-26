## Outils utilisés

- **Webflow** : page web simple (front)
- **Tally.so** : formulaire de contact
- **Airtable** : base de données
- **Make.com** : automatisation

---

## Contexte

Une petite structure souhaite collecter des **demandes de contact** depuis son site web
et les centraliser automatiquement dans une base pour les traiter plus tard.

---


✅ Un visiteur remplit un formulaire sur le site  
✅ Les données arrivent automatiquement dans Airtable  
✅ Aucune saisie manuelle côté admin  

---

## Étape 1 — Créer la base Airtable 

Créer une base **`Leads`** avec une table **`Contacts`** contenant :

- `Nom` (Single line text)
- `Email` (Email)
- `Message` (Long text)
- `Source` (Single select : Webflow)
- `Date de création` (Date)

👉 Ajouter **1 contact de test** manuellement pour vérifier la structure.

---

## Étape 2 — Créer le formulaire Tally

Créer un formulaire **“Contact”** avec les champs :

- Nom
- Email
- Message

Paramètres :

- Activer la page de confirmation
- Texte : *“Merci, votre message a bien été envoyé.”*

👉 Copier le lien ou le code d’intégration du formulaire.

---

## Étape 3 — Créer la page Webflow

Créer une page simple :

- Titre : *Contactez‑nous*
- Texte court explicatif
- Intégrer le formulaire **Tally** (embed <iframe> ou lien)

👉 Publier la page Webflow.

---

## Étape 4 — Automatisation Make

Créer un scénario Make :

### Déclencheur
- **Tally** : nouvelle réponse au formulaire

<https://airtable.com/create/tokens>

### Action
- **Airtable** : créer un enregistrement dans `Contacts`
  - Nom → Nom
  - Email → Email
  - Message → Message
  - Source → `Webflow`
  - Date de création → date du jour

👉 Lancer le scénario une première fois.

---

## Étape 5 — Test final 

- Remplir le formulaire depuis la page Webflow
- Vérifier :
  - ✅ le contact apparaît dans Airtable
  - ✅ les champs sont correctement remplis

---


## Bonus (si temps restant)
- Ajouter un champ `Statut` dans Airtable (Nouveau / Contacté)
- Ajouter une condition Make : email obligatoire
- Créer une vue Airtable “Nouveaux leads”
