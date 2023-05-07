# utils.py: conterrà funzioni di utilità come il salvataggio dei dati in un file Excel e il cambio IP.
import subprocess
import xlsxwriter
import os

# Funzione per salvare i dati del prodotto in un file Excel

def save_to_excel(product_data, output_folder):
    file_path = f"{output_folder}/amazon_products.xlsx"

    # Crea un nuovo file Excel se non esiste
    if not os.path.exists(file_path):
        workbook = Workbook()
        workbook.save(file_path)

    # Apri il file Excel e seleziona il foglio di lavoro
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Scrivi i dati del prodotto nel foglio di lavoro
    new_row = [product_data["asin"], product_data["title"],
               product_data["price"], product_data["rating"], 
               product_data["reviews"], product_data["sales_rank"]]

    # Aggiungi i dati di Helium 10 e Keepa se disponibili
    if "helium_data" in product_data:
        new_row.append(product_data["helium_data"])
    else:
        new_row.append("Dati Helium non disponibili")

    if "keepa_price" in product_data:
        new_row.append(product_data["keepa_price"])
    else:
        new_row.append("Prezzo Keepa non disponibile")

    sheet.append(new_row)

    # Salva il file Excel
    workbook.save(file_path)

# Funzione per cambiare IP con NordVPN ogni 3 EAN/ASIN inviati verso Amazon


def change_ip():
    # Assicurarsi che il comando 'nordvpn' sia disponibile nel sistema
    try:
        subprocess.run(["nordvpn", "--version"], check=True)
    except FileNotFoundError:
        print("Errore: NordVPN non è installato sul sistema.")
        return

    # Disconnetti da NordVPN (se connesso)
    print("Disconnessione da NordVPN...")
    subprocess.run(["nordvpn", "disconnect"], check=True)
    time.sleep(5)

    # Connetti a NordVPN con un nuovo IP
    print("Connessione a NordVPN con un nuovo IP...")
    subprocess.run(["nordvpn", "connect"], check=True)

