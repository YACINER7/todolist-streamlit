# 📝 Ma TodoList — Projet Streamlit

Application de gestion de tâches développée avec Streamlit dans le cadre d'un TP de maintenance logicielle.

## 🚀 Lancer l'application

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌿 Branches de maintenance

| Branche | Type | Description |
|---|---|---|
| `bugfix/tache-vide` | Corrective | Empêcher l'ajout de tâches vides ou en doublon |
| `feature/suppression-tache` | Évolutive | Ajouter la suppression d'une tâche |
| `adaptation/streamlit-cloud` | Adaptative | Préparer le projet pour Streamlit Cloud |
| `perfective/interface-optimisee` | Perfective | Améliorer l'interface utilisateur |

## 👥 Workflow Git

1. Chaque membre **fork** ce dépôt
2. Clone son fork en local
3. Crée une branche selon son type de tâche
4. Réalise les modifications et **commit** proprement
5. Ouvre une **Pull Request** vers `main` du leader
6. Lie la PR à une **Issue** GitHub correspondante

## 📦 Déploiement (Streamlit Cloud)

Déposer sur [share.streamlit.io](https://share.streamlit.io) avec :
- **Repository** : ce dépôt GitHub
- **Branch** : `main`
- **Main file** : `app.py`
