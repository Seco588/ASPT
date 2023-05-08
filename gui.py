# gui.py: conterrà il codice per l'interfaccia grafica.
import tkinter as tk
from scraper import read_csv_and_scrape
from tkinter import Checkbutton, BooleanVar, filedialog



# Funzione per aprire il file CSV tramite l'interfaccia grafica
def open_csv_file(use_helium_keepa):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        output_folder = filedialog.askdirectory(title="Seleziona la cartella di output")
        if output_folder:
            read_csv_and_scrape(file_path, output_folder, use_helium_keepa.get())