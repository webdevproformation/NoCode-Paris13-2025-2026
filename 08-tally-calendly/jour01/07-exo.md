## 🧩 Contexte

Vous travaillez pour le service **Ressources Humaines** d’une entreprise qui recrute régulièrement sur plusieurs postes.

Aujourd’hui, les candidatures arrivent par email et sont difficiles à suivre.  
Votre mission est de **concevoir un système automatisé**, simple et fiable, sans écrire de code.

---

## 🛠️ Outils à utiliser

- **Tally** : création du formulaire de candidature
- **Zapier** : automatisation et orchestration du workflow
- **Google Sheets** : base centralisée des candidatures (ATS simplifié)
- **Gmail** : notification automatique de l’équipe RH

---

## 🏗️ Workflow attendu (vue d’ensemble)

1. Le candidat remplit un **formulaire Tally**
2. Les réponses sont analysées selon le **poste sélectionné**
3. La candidature est enregistrée dans **Google Sheets**
4. Un **email automatique** est envoyé à l’équipe RH
5. Le candidat est **redirigé vers une page de confirmation**

---

## ✅ Travail demandé

### 1️⃣ Créer le formulaire de candidature (Tally)

Le formulaire doit contenir **plusieurs pages** et collecter au minimum :

#### Informations candidat
- Prénom
- Nom
- Email
- Poste visé (choix unique) :
  - Développeur
  - Designer
  - Chef de projet

#### Candidature
- CV (fichier)
- Message de motivation (texte long)

💡 Le formulaire doit être clair, progressif et rassurant pour le candidat.

---

### 2️⃣ Mettre en place la logique conditionnelle (Tally)

Selon le **poste sélectionné** :
- certaines informations peuvent être adaptées (ex. message explicatif),
- les données devront permettre un **tri ultérieur automatique**.

---

### 3️⃣ Centraliser les candidatures dans Google Sheets

À l’aide de **Zapier**, chaque nouvelle candidature doit :
- créer une **nouvelle ligne** dans un Google Sheets, 
- inclure :
  - identité du candidat,
  - poste visé,
  - lien vers le CV,
  - date de candidature.

Le tableau Google Sheets joue le rôle d’un **ATS simple** (Applicant Tracking System).

---

### 4️⃣ Envoyer une notification RH (Gmail)

À chaque nouvelle candidature :
- un email automatique est envoyé via Gmail à l’équipe RH,
- l’email doit contenir :
  - le nom du candidat,
  - le poste visé,
  - un lien vers la ligne Google Sheets ou le CV.

---

### 5️⃣ Rediriger le candidat après soumission (Tally)

Une fois le formulaire envoyé :
- le candidat est redirigé vers une **page de confirmation**,
- la page doit contenir un message du type :
  > *Merci pour votre candidature. Notre équipe RH reviendra vers vous prochainement.*

---

## 🎯 Résultat attendu

À la fin de l’exercice :
- les candidatures sont **centralisées automatiquement**,
- le tri par poste est immédiat,
- l’équipe RH est informée sans action manuelle,
- le candidat bénéficie d’une expérience fluide et professionnelle.

---

## 🚀 Bonus (optionnel)

- Ajouter une colonne “Statut” dans Google Sheets (Nouveau / En cours / Refusé)
- Envoyer un **email automatique de confirmation au candidat**
- Ajouter un **reCAPTCHA** au formulaire
- Filtrer les notifications RH selon le poste
