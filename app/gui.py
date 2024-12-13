import tkinter as tk
from tkinter import messagebox
import threading
import subprocess
import sys
import os

# Add the parent directory 'unlockediptv' to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ensure the path to fastapi.exe is correct
FASTAPI_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mon_env', 'Scripts', 'fastapi.exe'))
API_SCRIPT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main.py'))

def start_server():
    """Launch the FastAPI server in a separate thread."""
    subprocess.Popen([FASTAPI_PATH, "run", "--host", "0.0.0.0", "--port", "8000", API_SCRIPT])

def on_start():
    """Start the FastAPI server."""
    threading.Thread(target=start_server).start()
    messagebox.showinfo("Info", "Server started at http://localhost:8000")

def on_stop():
    """Stop the FastAPI server."""
    # This function requires an appropriate method to stop the server.
    messagebox.showwarning("Warning", "Stop function not implemented.")

# Create the main window
root = tk.Tk()
root.title("Secure IPTV Application")

# Add buttons to control the server
start_button = tk.Button(root, text="Start Server", command=on_start)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Server", command=on_stop)
stop_button.pack(pady=20)

# Start the main Tkinter loop
root.mainloop()
