import tkinter as tk
from tkinter import messagebox
import threading
import uvicorn
import sys
import os

# Ajouter le répertoire parent 'unlockediptv' au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app  # Importation correcte du module app

def start_server():
    """Lancer le serveur FastAPI dans un thread séparé."""
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

def on_start():
    """Démarrer le serveur FastAPI."""
    threading.Thread(target=start_server).start()
    messagebox.showinfo("Info", "Serveur démarré sur http://localhost:8000")

def on_stop():
    """Arrêter le serveur FastAPI."""
    # Cette fonction nécessite une méthode appropriée pour arrêter le serveur.
    messagebox.showwarning("Warning", "Fonction d'arrêt non implémentée.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Secure IPTV Application")

# Ajouter des boutons pour contrôler le serveur
start_button = tk.Button(root, text="Démarrer le Serveur", command=on_start)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Arrêter le Serveur", command=on_stop)
stop_button.pack(pady=20)

# Démarrer la boucle principale de Tkinter
root.mainloop()
