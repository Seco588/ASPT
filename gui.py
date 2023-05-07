# gui.py: conterrà il codice per l'interfaccia grafica.
import tkinter as tk
from tkinter import filedialog
from scraper import read_csv_and_scrape


def open_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        output_folder = filedialog.askdirectory(
            title="Seleziona la cartella di output")
        if output_folder:
            read_csv_and_scrape(file_path, output_folder)
