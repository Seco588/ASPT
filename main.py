# main.py: conterrà il punto di ingresso principale del programma.
import tkinter as tk
from gui import open_csv_file

if __name__ == "__main__":
    # Crea l'interfaccia grafica
    root = tk.Tk()
    root.title("Amazon Scraper")

    # Crea un pulsante per aprire il file CSV
    open_button = tk.Button(root, text="Apri file CSV", command=open_csv_file)
    open_button.pack(padx=20, pady=20)

    # Aggiungi un Checkbutton per selezionare l'utilizzo di Helium 10 e Keepa
    use_helium_keepa = tk.BooleanVar()
    helium_keepa_checkbox = tk.Checkbutton(root, text="Usa Helium 10 e Keepa", variable=use_helium_keepa)
    helium_keepa_checkbox.pack(pady=10)

    # Avvia il loop principale dell'interfaccia grafica
    root.mainloop()
