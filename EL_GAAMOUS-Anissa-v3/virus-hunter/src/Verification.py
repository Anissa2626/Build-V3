import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import subprocess

def choisir_fichier():
    chemin_fichier = filedialog.askopenfilename(filetypes=[("Fichiers exécutables", "*.exe")])
    if chemin_fichier:
        afficher_certificat(chemin_fichier)

def visualiser_infos_certificat(chemin):
    try:
        processus = subprocess.run(['certutil', '-v', '-dump', chemin], capture_output=True, text=True, check=True)
        details_certificat = processus.stdout
        panneau_affichage.config(state=tk.NORMAL)
        panneau_affichage.delete(1.0, tk.END)
        panneau_affichage.insert(tk.END, details_certificat)
        panneau_affichage.config(state=tk.DISABLED)
    except subprocess.CalledProcessError:
        panneau_affichage.config(state=tk.NORMAL)
        panneau_affichage.delete(1.0, tk.END)
        panneau_affichage.insert(tk.END, "Erreur : Impossible de récupérer les informations du certificat.")
        panneau_affichage.config(state=tk.DISABLED)

# Initialisation de la fenêtre principale
fenetre_principale = tk.Tk()
fenetre_principale.title("Visualisateur de Certificat")
fenetre_principale.geometry("800x600")  # Taille initiale
fenetre_principale.resizable(True, True)  # Permet le redimensionnement

# Définition de l'icône de la fenêtre
fenetre_principale.iconbitmap("icone.ico")  # Remplacer "icone.ico" par le chemin de votre fichier d'icône

style = ttk.Style(fenetre_principale)
style.theme_use('clam')  # Choix d'un thème pour une apparence cohérente

# Personnalisation de l'apparence du bouton
bouton_selection = ttk.Button(fenetre_principale, text="Sélectionner un fichier .exe", command=choisir_fichier)
bouton_selection.pack(pady=20, padx=20)

# Personnalisation du widget de texte avec barre de défilement
zone_texte = scrolledtext.ScrolledText(fenetre_principale, height=20, width=80, wrap=tk.WORD)
zone_texte.pack(padx=10, pady=10, expand=True, fill='both')
zone_texte.config(state=tk.DISABLED)

# Lancement de la boucle d'événements Tkinter
fenetre_principale.mainloop()