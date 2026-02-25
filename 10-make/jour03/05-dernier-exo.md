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
- `Statut` (choix : Nouveau / En cours / Terminé)
- `Source` (texte)
- `Date de création` (date)

---

## Étape 2 — Créer le back‑office Notion (15 min)

Créer une base Notion **“Tickets internes”** avec les propriétés :

- `Titre` (title)
- `Description` (text)
- `Priorité` (select)
- `Statut` (select)
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
