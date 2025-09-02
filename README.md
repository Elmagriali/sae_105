🌤️ Projet n°9 : La météo d’une journée donnée

Auteurs : TAILLY Emmanuel & EL MAGRI Ali

📝 Description

Ce projet permet d'avoir la météo de nimporte quelle ville en Bourgogne de 1950 à 2023, il faut ne pas faire d'erreur d'orthographe
dans l'écriture du nom de la ville, ex : Nevers, c'est NEVERS-MARZY.

L’application est :
-Paramétrable : vous pouvez choisir la ville et la date.
-Interactive : interface graphique intuitive avec Tkinter.
-Visuale : possibilité de générer des graphiques de températures.

⚙️ Fonctionnalités

Recherche de données météorologiques par ville et date (format AAAAMMJJ).
Affichage des informations détaillées :
-Température minimale et maximale
-Moyenne quotidienne des températures
-Précipitations et durée des précipitations
-Force et maximum du vent
-Insolation, rayonnement UV, humidité, neige fraîche
-Visualisation graphique des températures minimales et maximales.

📂 Installation & Utilisation

Prérequis
Python 3

Bibliothèques : tkinter, matplotlib, csv (incluses dans Python)
Ajouter vos fichiers CSV dans le répertoire :

fichiers_csv = [
    "Q_21_previous-1950-2023_RR-T-Vent.csv",
    "Q_58_previous-1950-2023_RR-T-Vent.csv",
    "Q_71_previous-1950-2023_RR-T-Vent.csv",
    "Q_89_previous-1950-2023_RR-T-Vent.csv",
]
Ces fichiers peuvent être retrouvé sur https://www.data.gouv.fr/datasets/donnees-climatologiques-de-base-quotidiennes/

Lancer l’application 

Conclusion

Ce projet nous a permis de :
-Traiter et visualiser des données météorologiques
-Concevoir une interface utilisateur paramétrable et intuitive
-Développer des compétences pratiques en Python et Tkinter
-Gestion des erreurs pour les champs vides ou données introuvables.
