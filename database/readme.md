#  Promenade de Chiens - Guide d'Installation

Bienvenue sur le projet Promenade de Chiens, une application web permettant de gérer une base de données relationnelle autour de la gestion de promenades de chiens (Clients, Chiens, Promeneurs, Services, Réservations).

Ce guide s'adresse au client / correcteur pour lui permettre de déployer le projet localement sur sa machine en quelques minutes.

---

##  1. Prérequis (Logiciels nécessaires)

Pour faire fonctionner ce projet, votre poste de travail doit être équipé des logiciels suivants :

- **Python 3.14** : Pour exécuter l'application Flask.
- **Laragon** : Pour héberger le serveur de base de données MySQL en local.
- **Un IDE (PyCharm recommandé)** : Pour ouvrir le projet et gérer l'environnement virtuel.

---

##  2. Installation de la Base de Données

L'application repose sur une base de données MySQL qui doit être initialisée avant de lancer le code.

1. Lancez **Laragon** et démarrez les services **MySQL**.
2. Ouvrez votre navigateur et rendez-vous sur : `http://localhost/phpmyadmin/`
3. Dans phpMyAdmin, cliquez sur l'onglet **Importer**.
4. Sélectionnez le fichier de sauvegarde SQL fourni dans le dossier `database` (`DaRosa_Lucas_DEVA1A_DUMP_164.sql`).
5. Cliquez sur **Exécuter** en bas de la page.

> Note : Le script SQL contient les instructions `DROP DATABASE IF EXISTS` et `CREATE DATABASE`. Il génèrera automatiquement la structure des tables et insérera les données d'exemple.

---

##  3. Configuration de l'Application Python

1. Récupérez le dossier du projet (via le ZIP ou clonez GitHub).
2. Ouvrez ce dossier complet dans **PyCharm**.
3. **Environnement virtuel** : PyCharm devrait vous proposer de créer un environnement virtuel (`.venv`). Acceptez.
4. **Dépendances** : Ouvrez le terminal de votre IDE et installez les modules nécessaires en tapant :
pip install -r requirements.txt

---

##  4. Variables d'Environnement (.env)

Pour que Python puisse communiquer avec la base de données locale, l'application utilise un fichier de configuration `.env`.

Vérifiez la présence du fichier `.env` à la racine du projet. S'il n'existe pas, créez-le et insérez les paramètres suivants :

HOST_MYSQL=localhost
USER_MYSQL=root
PASS_MYSQL=
PORT_MYSQL=3306
NAME_BD_MYSQL=darosa_lucas_deva1a_chiens_164_2026
NAME_FILE_DUMP_SQL_BD=DaRosa_Lucas_DEVA1A_DUMP_164.sql
ADRESSE_SRV_FLASK=localhost
DEBUG_FLASK=True
PORT_FLASK=5560
SECRET_KEY_FLASK=secret


---

##  5. Lancement de l'Application

1. Dans PyCharm, repérez le fichier principal de lancement : `run_mon_app.py`.
2. Faites un clic droit sur ce fichier et sélectionnez **Run 'run_mon_app'** (ou utilisez le bouton Play vert en haut à droite).
3. Le terminal va afficher une adresse locale : `http://127.0.0.1:5560`
4. Cliquez sur ce lien pour ouvrir l'application dans votre navigateur web.

L'application est maintenant 100% fonctionnelle ! Vous pouvez gérer les clients, chiens, promeneurs, services et réservations.
