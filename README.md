# 🚀 Projet : Consommation d'API Publiques de la NASA

Ce projet Python a pour but d'explorer et manipuler des données provenant des **API publiques de la NASA**, notamment :

- 🌌 L'image astronomique du jour (APOD)
- ☄️ Les astéroïdes proches de la Terre (NEO - Near Earth Object)

## 📁 Contenu du projet

- `image_du_jour.py` : Récupère l’image astronomique du jour depuis l’API APOD et l’enregistre localement.
- `asteroids.py` : Récupère les données des astéroïdes en approche de la Terre à une date donnée et extrait certaines informations.
- `asteroides_nasa.csv` : Fichier généré par `asteroids.py` contenant les données traitées des astéroïdes (ID, nom, diamètre, vitesse...).

## 🛠️ Prérequis

- Python 3
- Bibliothèques nécessaires :
  ```bash
  pip install requests pandas
  ```

## 🚦 Utilisation

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/chniang/checkpoint_API.git
   cd checkpoint_API
   ```

2. **Exécuter le script de l’image du jour** :
   ```bash
   python image_du_jour.py
   ```

3. **Exécuter le script des astéroïdes** :
   ```bash
   python asteroids.py
   ```

> ℹ️ N'oublie pas de remplacer `"DEMO_KEY"` dans les scripts par **ta propre clé API** obtenue sur [api.nasa.gov](https://api.nasa.gov/)

## 📌 Objectifs pédagogiques

- Comprendre le fonctionnement des API REST
- Envoyer des requêtes `GET` avec des paramètres
- Manipuler des réponses JSON
- Nettoyer et structurer des données avec Pandas
- Exporter vers CSV

## 🛰️ Ressources

- [NASA API Portal](https://api.nasa.gov/)
- [Documentation APOD](https://github.com/nasa/apod-api)
- [Documentation NeoWs (Asteroids)](https://github.com/nasa/neo-api)

---

_Fait avec passion pour explorer l'univers en données_ 🌌✨
