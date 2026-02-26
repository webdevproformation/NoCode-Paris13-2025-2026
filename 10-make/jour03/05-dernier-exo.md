## Outils utilisés

- **Baserow** : base de données centrale
- **Notion** : interface simple de back‑office
- **Make.com** : automatisation entre les outils

---

## Contexte

Une équipe souhaite suivre des **demandes internes** (problèmes, idées, besoins).

Les demandes sont saisies dans **Notion**, mais doivent aussi être stockées dans une **base structurée** pour le suivi.

---

## Étape 1 — Créer la base Baserow 

Créer une table **`Tickets`** avec les champs suivants :

- `ID` (auto)
- `Titre` (texte)
- `Description` (texte long)
- `Priorité` (choix : Basse / Moyenne / Haute)
- `Statut` (choix : Nouveau / En cours / Terminé) => valeur défaut Nouveau
- `Source` (texte)
- `Date de création` (date)                       => pas de valeur par défaut 

---

## Étape 2 — Créer le back‑office Notion 

-  <notion.so> 
- 


Créer une base Notion **“Tickets internes”** avec les propriétés :

- `Titre` (title)
- `Description` (text)
- `Priorité` (select)
- `Statut` (select) (choix : Nouveau / En cours / Terminé)
- `Envoyé vers Baserow ?` (checkbox)


---

## Étape 3 — Automatisation Make (20 min)

Créer un scénario Make :

### Déclencheur
- **Notion** : nouvelle page dans la base “Tickets internes”

### Actions

1. **Baserow** : créer une nouvelle ligne dans la table `Tickets`
   - Titre → Titre
   - Description → Description
   - Priorité → Priorité
   - Statut → Statut
   - Source → `Notion`
   - Date de création → date du jour

2. (Optionnel)
   - Mettre à jour la page Notion
   - Cocher ✅ `Envoyé vers Baserow ?`

👉 Lancer le scénario une première fois.


curl \
-X POST \
-H "Authorization: Token 4Wp4EE2a4K7CbraN4soHdVrARU7nlpFe" \
-H "Content-Type: application/json" \
"https://api.baserow.io/api/database/rows/table/859457/?user_field_names=true" \
--data '{
    "Titre": "string",
    "Description": "string",
    "priority": 1,
    "Statut": 1,
    "Source": "string",
    "Date de création": "2020-01-01"
}'
