# Exercice NoCode — CRUD Formations  

**Durée : 1 heure**  
**Outils : Tally · Airtable · Make**  

---

## Objectif pédagogique

Mettre en place un **CRUD complet (Create, Read, Update, Delete)** sur une table **Formations** sans écrire de code.

---

## Contexte

Un organisme de formation souhaite gérer son **catalogue de formations** :

- création de nouvelles formations,
- consultation de la liste,
- mise à jour des informations,
- suppression de formations obsolètes.

Le back‑office est volontairement simple et automatisé.

---

## Structure des données (Airtable)

Créer une base **`Catalogue Formations`**  

Table : **`Formations`**

### Colonnes obligatoires

- `Nom` (Single line text)
- `Prix` (Number)
- `Durée` (Single line text — ex : “3 jours”, “14h”)
- `Description` (Long text)
- `Online` (Checkbox / Boolean)
- `Date de création` (Date)
- `ID formation` (Formula ou Autonumber)

---

## Étape 1 — CREATE 

### Objectif

Créer une formation depuis un formulaire Tally.

### Actions

1. Créer un formulaire **Tally – Création formation**
   - Nom
   - Prix
   - Durée
   - Description
   - Online (Oui / Non)

2. Créer un scénario **Make**
   - Déclencheur : nouvelle réponse Tally
   - Action : **Airtable – Create Record**
     - Mapper tous les champs
     - `Date de création` = date du jour

✅ Résultat attendu :  
Une formation apparaît automatiquement dans Airtable après soumission.

---

## Étape 2 — READ 

### Objectif

Lire / visualiser les formations existantes.

### Actions

1. Dans Airtable :
   - Créer une vue **“Formations en ligne”** (`Online = true`)
   - Créer une vue **“Formations présentielles”** (`Online = false`)

2. Vérifier que les données créées via Tally sont visibles.

✅ Résultat attendu :  
Les formations sont correctement listées et filtrées.

---

## Étape 3 — UPDATE 

### Objectif

Modifier une formation existante via Tally.

### Actions

1. Créer un formulaire **Tally – Mise à jour formation**

   - ID formation
   - Nom
   - Prix
   - Durée
   - Description
   - Online

2. Créer un scénario **Make**

   - Déclencheur : nouvelle réponse Tally (formulaire update)
   - Action : **Airtable – Update Record**
     - Rechercher la formation via `ID formation`
     - Mettre à jour les champs

✅ Résultat attendu :  
Les informations de la formation sont modifiées dans Airtable.

---

## Étape 4 — DELETE

### Objectif

Supprimer une formation depuis un formulaire.

### Actions

1. Créer un formulaire **Tally – Suppression formation**
   - ID formation
   - Confirmation (checkbox : “Je confirme la suppression”)

2. Créer un scénario **Make**
   - Déclencheur : nouvelle réponse Tally
   - Condition : confirmation = true
   - Action : **Airtable – Delete Record**

✅ Résultat attendu :  
La formation est supprimée de la base Airtable.

---

## Récapitulatif CRUD

| Action | Outil déclencheur| Action Make    | Résultat |
|--------|------------------|----------------|----------|
| Create | Tally            | Create record  | Nouvelle formation |
| Read   | Airtable         | —              | Liste des formations |
| Update | Tally            | Update record  | Formation modifiée |
| Delete | Tally            | Delete record  |  Formation supprimée |

---

## Bonus (si temps restant)

- Ajouter un champ `Statut` (Active / Archivée)
- Empêcher la suppression si la formation est “Active”
- Ajouter un champ `Prix TTC` calculé