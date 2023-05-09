import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading
from scraper import do_scraping
from utils import change_ip
import queue  # Non dimenticare di importare il modulo queue

class ASPTApp(tk.Tk):
    def __init__(self):
        # Implementa la creazione della dashboard qui
        super().__init__()

        self.title("ASPT - Amazon Scraping Project Tool")
        self.geometry("800x600")

        # Inizializza i widget
        self.init_widgets()
        
        # Coda messaggi
        self.log_queue = queue.Queue()

    def use_ai(self):
        return self.ai_var.get() == 1

    
    def start_scraping(self):
        params = {
            "tools": {
                "keepa": self.keepa_var.get(),
                "helium10": self.helium10_var.get(),
                "junglescout": self.junglescout_var.get(),
                "ai": self.ai_var.get(),
            },
            "csv_file": self.csv_entry.get(),
            "change_ip_enabled": self.change_ip_var.get() == 1,
            "change_ip_every": int(self.change_ip_spinbox.get() or 1)
        }

        # Avvia un nuovo thread per eseguire lo scraping in modo non bloccante
        scraping_thread = threading.Thread(target=do_scraping, args=(params, self.log_queue), daemon=True)
        scraping_thread.start()

    def update_logs(self):
        while not self.log_queue.empty():
            log_message = self.log_queue.get()
            self.log_text.insert(tk.END, log_message + "\n")
            self.log_text.see(tk.END)

        # Continua ad aggiornare i log ogni 100 millisecondi
        self.after(100, self.update_logs)

    def browse_csv_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.csv_entry.delete(0, tk.END)
            self.csv_entry.insert(0, file_path)

    def init_widgets(self):
        # ... [aggiungi qui il codice per creare i widget e posizionarli nella finestra] ...

        # Caselle di controllo per selezionare gli strumenti
        self.keepa_var = tk.IntVar()
        self.helium10_var = tk.IntVar()
        self.junglescout_var = tk.IntVar()
        self.ai_var = tk.IntVar()
        self.change_ip_var = tk.IntVar()

        self.keepa_check = ttk.Checkbutton(self, text="Keepa", variable=self.keepa_var)
        self.helium10_check = ttk.Checkbutton(self, text="Helium10", variable=self.helium10_var)
        self.junglescout_check = ttk.Checkbutton(self, text="JungleScout", variable=self.junglescout_var)
        self.ai_check = ttk.Checkbutton(self, text="AI", variable=self.ai_var)
        self.change_ip_check = ttk.Checkbutton(self, text="Enable IP Change", variable=self.change_ip_var)

        # Posiziona le caselle di controllo
        # ... [aggiungi qui il codice per posizionare le caselle di controllo nella finestra] ...
        self.keepa_check.grid(row=0, column=0)
        self.helium10_check.grid(row=0, column=1)
        self.junglescout_check.grid(row=0, column=2)
        self.ai_check.grid(row=0, column=3)
        self.change_ip_check.grid(row=1, column=0)

        # Pulsante per selezionare il file CSV
        self.csv_button = ttk.Button(self, text="Browse CSV File", command=self.browse_csv_file)
        self.csv_entry = ttk.Entry(self)

        # Posiziona il pulsante e il campo di input per il file CSV
        # ... [aggiungi qui il codice per posizionare il pulsante e il campo di input nella finestra] ...
        self.csv_button.grid(row=2, column=0)
        self.csv_entry.grid(row=2, column=1, columnspan=3, sticky=tk.W+tk.E)

        # Posiziona il pulsante "Start Scraping"
        self.start_button = ttk.Button(self, text="Start Scraping", command=self.start_scraping)

        # ... [aggiungi qui il codice per posizionare il pulsante nella finestra] ...
        self.start_button.grid(row=3, column=0)

        # Widget per i log in tempo reale
        self.log_text = tk.Text(self, wrap=tk.WORD)
        self.log_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text["yscrollcommand"] = self.log_scrollbar.set

        # Posiziona il widget per i log in tempo reale e la barra di scorrimento
        # ... [aggiungi qui il codice per posizionare il widget e la barra di scorrimento nella finestra] ...
        self.log_text.grid(row=4, column=0, columnspan=4, sticky=tk.W+tk.E+tk.N+tk.S)
        self.log_scrollbar.grid(row=4, column=4, sticky=tk.N+tk.S)
        
        # Widget per il cambio IP
        self.change_ip_label = ttk.Label(self, text="Change IP every X requests:")
        self.change_ip_spinbox_var = tk.StringVar(value="1")
        self.change_ip_spinbox = ttk.Spinbox(self, from_=1, to=100, increment=1, width=5, textvariable=self.change_ip_spinbox_var)

        # Posiziona il widget per il cambio IP
        # ... [aggiungi qui il codice per posizionare il widget nella finestra] ...
        self.change_ip_label.grid(row=5, column=0)
        self.change_ip_spinbox.grid(row=5, column=1)

        # Aggiungi un po' di spazio tra i widget e i bordi della finestra
        self.grid_columnconfigure(0, weight=1, minsize=20)
        self.grid_columnconfigure(1, weight=1, minsize=20)
        self.grid_columnconfigure(2, weight=1, minsize=20)
        self.grid_columnconfigure(3, weight=1, minsize=20)
        self.grid_rowconfigure(4, weight=1, minsize=20)

def init_gui():
    # Implementa la logica per avviare la dashboard e gestire gli eventi qui
    app = ASPTApp()
    app.update_logs()
    return app