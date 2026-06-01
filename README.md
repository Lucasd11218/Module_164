# Projet Promenade de chiens - DaRosa Lucas DEVA1A

## Logiciels nécessaires
- Python 3.14.2
- Laragon (MySQL + phpMyAdmin)

## Installation

### 1. Installer les dépendances
pip install -r requirements.txt

### 2. Créer la base de données
- Ouvrir phpMyAdmin
- Créer une base de données : darosa_lucas_deva1a_chiens_164_2026
- Importer le fichier : database/DaRosa_Lucas_DEVA1A_DUMP_164.sql

### 3. Configurer le .env
Vérifier que le fichier .env à la racine contient les bonnes informations de connexion MySQL

### 4. Lancer le projet
python run_mon_app.py

### 5. Ouvrir le navigateur
http://127.0.0.1:5560