import csv  
import tkinter as tk  # Pour créer l'interface graphique
from tkinter import messagebox, ttk  # Pour les boîtes de dialogue et widgets améliorés
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Pour intégrer matplotlib dans tkinter

''' Ce code permet d'avoir la météo de nimporte quelle ville en Bourgogne, il faut ne pas faire d'erreur d'orthogrphe
dns lécriture du nom de la ville, ex : Nevers, c'est NEVERS-MARZY
'''
def charger_donnees_meteo(fichiers_csv):
    data = []  # Liste pour stocker toutes les données
    for fichier_csv in fichiers_csv:
        try:
            with open(fichier_csv, mode='r', encoding='utf-8') as file:
                # Création d'un lecteur CSV qui transforme chaque ligne en dictionnaire
                lecteur_csv = csv.DictReader(file, delimiter=';')
                # Ajout des données du fichier à la liste principale
                data.extend(list(lecteur_csv))
        except FileNotFoundError:
            # Affichage d'une erreur si le fichier n'existe pas
            messagebox.showerror("Erreur", f"Le fichier {fichier_csv} est introuvable.")
    return data

# Fonction pour obtenir les données météo d'une ville à une date spécifique
def obtenir_meteo(data, ville, journee):
    # Parcours de toutes les lignes de données
    for ligne in data:
        # Vérification de la correspondance ville/date
        if ligne['NOM_USUEL'].lower() == ville.lower() and ligne['AAAAMMJJ'] == journee:
            # Extraction des données météorologiques avec valeur par défaut 'N/A'
            rr = ligne.get('RR', 'N/A')  # Quantité de précipitation
            tn = ligne.get('TN', 'N/A')  # Température minimale
            htn = ligne.get('HTN', 'N/A')  # Heure de la température minimale
            tx = ligne.get('TX', 'N/A')  # Température maximale
            htx = ligne.get('HTX', 'N/A')  # Heure de la température maximale
            tm = ligne.get('TM', 'N/A')  # Moyenne des températures
            ffm = ligne.get('FFM', 'N/A')  # Force du vent à 10m
            ff2m = ligne.get('FF2M', 'N/A')  # Force du vent à 2m
            fxy = ligne.get('FXY', 'N/A')  # Maximum de la force du vent
            drr = ligne.get('DRR', 'N/A')  # Durée des précipitations
            inst = ligne.get('INST', 'N/A')  # Durée d'insolation
            uv = ligne.get('UV', 'N/A')  # Rayonnement UV
            hux = ligne.get('HUX', 'N/A')  # Heure du maximum d'humidité
            um = ligne.get('UM', 'N/A')  # Moyenne d'humidité
            hneigef = ligne.get('HNEIGEF', 'N/A')  # Hauteur de neige fraîche

            # Retour des données reset
            return (
            f"- Quantité de précipitation : {rr} mm\n"
            f"- Température minimale : {tn} °C\n"
            f"- Heure de la température minimale : {htn}\n"
            f"- Température maximale : {tx} °C\n"
            f"- Heure de la température maximale : {htx}\n"
            f"- Moyenne quotidienne des températures : {tm} °C\n"
            f"- Moyenne quotidienne de la force du vent à 10 m : {ffm} m/s\n"
            f"- Moyenne quotidienne de la force du vent à 2 m : {ff2m} m/s\n"
            f"- Maximum quotidien de la force du vent à 10 m : {fxy} m/s\n"
            f"- Durée des précipitations : {drr} minutes\n"
            f"- Durée d'insolation : {inst} minutes\n"
            f"- Rayonnement UV : {uv} J/cm²\n"
            f"- Heure du maximum d'humidité : {hux}\n"
            f"- Moyenne d'humidité relative : {um} %\n"
            f"- Hauteur de neige fraîche : {hneigef} cm\n"

            )
    
    return "Aucune donnée trouvée pour cette ville ou cette date."

# Fonction pour afficher les données météo dans l'interface
def afficher_meteo():
    # Récupération des valeurs entrées par l'utilisateur
    ville = entree_ville.get()
    journee = entree_date.get()

    # Vérification que les champs ne sont pas vides
    if not ville or not journee:
        messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")
        return

    # Obtention et affichage des données météo
    meteo = obtenir_meteo(data, ville, journee)
    texte_resultat.delete(1.0, tk.END)  # Efface le contenu précédent
    texte_resultat.insert(tk.END, meteo)  # Insère les nouvelles données

# Fonction pour créer et afficher le graphique
def afficher_graphique():
    # Récupération des valeurs entrées
    ville = entree_ville.get()
    journee = entree_date.get()

    # Vérification des champs
    if not ville or not journee:
        messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")
        return

    # Obtention des données météo
    meteo = obtenir_meteo(data, ville, journee)
    if "Aucune donnée trouvée" in meteo:
        messagebox.showwarning("Données non trouvées", "Aucune donnée trouvée pour cette ville ou cette date.")
        return

    # Création du graphique
    fig, ax = plt.subplots()
    # Extraction et affichage des températures min et max
    ax.bar(["Température minimale", "Température maximale"], 
           [float(meteo.split('\n')[1].split(': ')[1].split(' ')[0]), 
            float(meteo.split('\n')[3].split(': ')[1].split(' ')[0])])
    ax.set_ylabel('Température (°C)')
    ax.set_title(f'Températures pour {ville} le {journee}')

    # Intégration du graphique dans l'interface
    canvas = FigureCanvasTkAgg(fig, master=onglet_graphique)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Liste des fichiers CSV à charger
fichiers_csv = [
    "Q_21_previous-1950-2023_RR-T-Vent.csv",
    "Q_58_previous-1950-2023_RR-T-Vent.csv",
    "Q_71_previous-1950-2023_RR-T-Vent.csv",
    "Q_89_previous-1950-2023_RR-T-Vent.csv",
]
# Chargement initial des données
data = charger_donnees_meteo(fichiers_csv)

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Données Météorologiques")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Création du système d'onglets
tab_control = ttk.Notebook(root)
onglet_recherche = ttk.Frame(tab_control)
onglet_graphique = ttk.Frame(tab_control)
tab_control.add(onglet_recherche, text='Recherche')
tab_control.add(onglet_graphique, text='Graphique')
tab_control.pack(expand=1, fill='both')

# Configuration des widgets de l'onglet de recherche
label_ville = tk.Label(onglet_recherche, text="Nom de la ville :", bg="#f0f0f0", font=("Arial", 12))
label_ville.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entree_ville = tk.Entry(onglet_recherche, width=30, font=("Arial", 12))
entree_ville.grid(row=0, column=1, padx=5, pady=5)

label_date = tk.Label(onglet_recherche, text="Date (AAAAMMJJ) :", bg="#f0f0f0", font=("Arial", 12))
label_date.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entree_date = tk.Entry(onglet_recherche, width=30, font=("Arial", 12))
entree_date.grid(row=1, column=1, padx=5, pady=5)

# Bouton de recherche
bouton_rechercher = tk.Button(onglet_recherche, text="Rechercher", command=afficher_meteo, bg="#4CAF50", fg="white", font=("Arial", 12))
bouton_rechercher.grid(row=2, column=0, columnspan=2, pady=10)

# Zone de texte pour les résultats
texte_resultat = tk.Text(onglet_recherche, height=15, width=60, wrap="word", font=("Arial", 12))
texte_resultat.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Configuration de l'onglet graphique
bouton_graphique = tk.Button(onglet_graphique, text="Afficher Graphique", command=afficher_graphique, bg="#4CAF50", fg="white", font=("Arial", 12))
bouton_graphique.pack(pady=10)

# Configuration de la barre de menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Ajout du menu Quitter
fichier_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Quitter", menu=fichier_menu)
fichier_menu.add_command(label="Quitter", command=root.quit)

# Lancement de l'application
root.mainloop()