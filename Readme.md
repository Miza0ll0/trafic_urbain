# Système de Simulation de Trafic Urbain
**Projet de Modélisation et Simulation - L2 RSI ANDRIATANTELY Ny Anja Misaël**

## 1. Présentation du Projet
Ce projet est une application web développée avec Django permettant de simuler et d'analyser le flux de trafic routier dans un environnement urbain simplifié. L'objectif est d'appliquer des modèles mathématiques stochastiques pour observer la gestion des congestions.

## 2. Modules Mathématiques Implémentés
Le simulateur repose sur trois piliers théoriques :
*   **Automate de Markov** : Gestion des états du réseau (FLUIDE / CONGESTION) basée sur des probabilités de transition.
*   **Méthode de Monte Carlo** : Algorithme utilisé pour le "spawn" aléatoire des véhicules selon un taux d'arrivée variable ($\lambda$).
*   **Théorie des files d'attente (Modèle M/M/1)** : Analyse de la performance du nœud routier (Loi de Little) pour calculer le temps d'attente moyen et le taux d'occupation.

## 3. Technologies Utilisées
*   **Backend** : Django pour la gestion du serveur et de la base de données.
*   **Frontend** : HTML ,CSS et JavaScript .
*   **Base de données** : SQLite (via Django ORM) pour l'archivage des statistiques de trafic.
*   **Visualisation** : Chart.js pour le rendu des graphiques en temps réel.

## 4. Fonctionnalités Clés
*   **Simulation Live** : Visualisation en temps réel du déplacement des véhicules et du cycle des feux de signalisation.

*   **Dashboard Statistique** : Page dédiée affichant les graphiques de performance (Radar, Doughnut, Barres).


## 5. Installation et Lancement
1.  **Clonage du projet** :

    git clone https://github.com/Miza0ll0/trafic_urbain
    cd urban_traffic
    
2.  **Migrations de la base de données** :
    python manage.py makemigrations
    python manage.py migrate