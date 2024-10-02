
# Gestion des Clients - CarPart API

**Université de Bretagne Sud (UBS) - I.U.T de Vannes**  
**Département Informatique - BUT 3e année**  
**Encadré par :** Matthieu Le Lain, Xavier Roirand  
**TP 2 - R5.A.09**

---

## Objectif du TP

Suite au succès de l'application de gestion de stocks, l'entreprise CarPart souhaite désormais une API similaire pour la **gestion des clients**. Ce TP vous demandera de créer une nouvelle application en reprenant les bases de la précédente, mais cette fois-ci avec des fonctionnalités centrées sur les clients.

### Spécifications

1. **Création d’une API web de gestion des clients.**

L'API devra offrir les fonctionnalités suivantes pour la gestion des clients :

- **Ajouter un client** (nom, prénom, adresse mail, nombre de commandes)
- **Modifier une fiche client** (informations personnelles, nombre de commandes)
- **Supprimer un client**
- **Accéder à la fiche d'un client**

#### Contraintes techniques :

- **Technologie** : L'API doit être développée avec **FastAPI** (version Python > 3.9)
- **Base de données** : Cette fois-ci, une base de données **MySQL** sera utilisée pour stocker les informations des clients.
- **Format de réponse** : Les retours devront être effectués en **JSON**

Les commandes des clients sont traitées par email, et les employés de CarPart sont responsables de la mise à jour du nombre de commandes via cette API.

2. **Génération des applications en conteneurs.**

L'entreprise souhaite que cette nouvelle application, ainsi que la base de données associée, soient contenues et déployées facilement via Docker. À cet effet, vous devrez fournir un fichier **Docker Compose** pour lancer les services.

Le fichier **docker-compose.yml** devra permettre de :

- Instancier les conteneurs de l'API et de la base de données
- Configurer les services, ports, et réseaux nécessaires
- Utiliser des variables d'environnement pour stocker les informations sensibles telles que les identifiants de connexion à la base de données MySQL

---

### Structure du projet

- `main.py` : Contient l'implémentation de l'API FastAPI pour la gestion des clients
- `crud.py` : Fonctions pour ajouter, modifier, supprimer et lire les fiches clients
- `Dockerfile` : Pour construire l'image de l'API
- `docker-compose.yml` : Permet de lancer l'application API et MySQL ensemble
- `requirements.txt` : Dépendances Python pour l'API
- `.dockerignore` : Fichiers à exclure lors de la construction Docker
- `.github/workflows/docker-publish.yml` : Workflow GitHub Actions pour déployer les conteneurs sur Docker Hub

---

### Instructions pour lancer l'application

1. **Construire et lancer la base de données MySQL :**

   Utilisez Docker Compose pour lancer la base de données MySQL et l'API en même temps :

   ```bash
   docker-compose up -d
   ```

   Cela lancera à la fois la base de données MySQL et l'API FastAPI, en configurant les services et les ports définis dans le fichier `docker-compose.yml`.

2. **Accéder à la documentation interactive :**

   Vous pouvez accéder à la documentation interactive de l'API via Swagger une fois que les conteneurs sont démarrés, à l'adresse suivante :  
   [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Ressources supplémentaires

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation Docker](https://docs.docker.com/)
- [Documentation MySQL](https://dev.mysql.com/doc/)

---

**Auteur :** Mathieu Stephan  
**Date :** 2024
```
