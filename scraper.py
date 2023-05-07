# scraper.py: conterrà il codice per lo scraping dei dati da Amazon.
import requests
from bs4 import BeautifulSoup
from utils import save_to_excel, change_ip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk
from tkinter import filedialog
import csv
import subprocess


# Definisco una funzione per estrarre i dati del prodotto da Amazon
# Configura qui le tue chiavi API per Keepa
KEEPA_ACCESS_KEY = "your_keepa_access_key"

def scrape_amazon_helium_keepa(asin):
    # Aggiungi qui la chiamata a change_ip() se necessario
    # change_ip()

    # 1. Utilizza Selenium per interagire con Helium 10
    # ...
    # 1. Utilizza Selenium per interagire con Helium 10
    chrome_options = Options()
    chrome_options.add_extension("/home/user/helium_10_extension.crx")
    chrome_options.add_argument("user-data-dir=/home/user/chrome/profile")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = f"https://www.amazon.it/dp/{asin}"
    driver.get(url)

    # Fai il login su Helium 10, se necessario

    # Utilizza i metodi di Selenium per interagire con la pagina e recuperare i dati desiderati
    # Nota: dovrai identificare gli elementi HTML e i selettori CSS appropriati per estrarre i dati da Helium 10

    # Esempio:
    # helium_data_element = driver.find_element_by_css_selector("your_css_selector_here")
    # helium_data = helium_data_element.text

    helium_data_element = driver.find_element_by_css_selector("your_css_selector_here")
    helium_data = helium_data_element.text


    driver.quit()

    # 2. Recupera i dati tramite l'API di Keepa
    keepa_url = f"https://api.keepa.com/product?key={KEEPA_ACCESS_KEY}&domain=8&asin={asin}"
    keepa_response = requests.get(keepa_url)
    keepa_data = keepa_response.json()

    # Estrai i dati di interesse dall'API di Keepa
    # Nota: dovrai analizzare la struttura dei dati JSON restituiti dall'API per estrarre le informazioni desiderate

    # Esempio:
    # keepa_price = keepa_data["your_key_here"]

    # 3. Effettua lo scraping su Amazon per ottenere ulteriori informazioni
    amazon_data = scrape_amazon(asin)

    # Combina i dati raccolti da Helium 10, Keepa e Amazon
    combined_data = {
        "asin": asin,
        # "helium_data": helium_data,
        # "keepa_price": keepa_price,
        **amazon_data
    }

    return combined_data

def scrape_amazon(asin):
    url = f"https://www.amazon.it/dp/{asin}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Estrai il titolo del prodotto
        title_element = soup.find("span", {"id": "productTitle"})
        title = title_element.get_text().strip() if title_element else "Titolo non trovato"

        # Estrai il prezzo del prodotto
        price_element = soup.find("span", {"id": "priceblock_ourprice"})
        price = price_element.get_text().strip() if price_element else "Prezzo non trovato"

        # Estrai la valutazione media
        rating_element = soup.find("span", {"class": "a-icon-alt"})
        rating = rating_element.get_text().strip() if rating_element else "Valutazione non trovata"

        # Estrai il numero di recensioni
        reviews_element = soup.find("span", {"id": "acrCustomerReviewText"})
        reviews = reviews_element.get_text().strip() if reviews_element else "Recensioni non trovate"

        # Estrai il Sales Rank
        sales_rank_element = soup.find("span", {"id": "SalesRank"})
        if sales_rank_element:
            sales_rank = sales_rank_element.get_text().strip()
            # Rimuovi eventuali caratteri non numerici nel Sales Rank
            sales_rank = ''.join(filter(str.isdigit, sales_rank))
        else:
            sales_rank = "Sales Rank non trovato"

        return {"asin": asin, "title": title, "price": price, "rating": rating, "reviews": reviews, "sales_rank": sales_rank}
    else:
        print(f"Errore nella richiesta: {response.status_code}")
        return None

# Funzione per leggere il file CSV e avviare lo scraping
# La funzione read_csv_and_scrape accetta ora un parametro aggiuntivo output_folder, che è impostato su None come valore predefinito.
#  Se output_folder viene passato alla funzione, i dati vengono salvati in un file Excel e viene aggiunto un intervallo di tempo di 60 secondi tra le richieste.
def read_csv_and_scrape(file_path, output_folder=None):
    asin_counter = 0
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for asin_or_ean in row:  # Itera su tutti gli elementi in ogni riga
                print(f"Scraping {asin_or_ean}...")
                asin_counter += 1

                if asin_counter % 3 == 0:
                    change_ip()

                if use_helium_keepa.get():
                    product_data = scrape_amazon_helium_keepa(asin_or_ean)
                else:
                    product_data = scrape_amazon(asin_or_ean)

                if product_data:
                    print(product_data)
                    
                    if output_folder:
                        save_to_excel(product_data, output_folder)  # Salva i dati del prodotto in un file Excel
                        time.sleep(60)  # Attendi 60 secondi (1 minuto) tra le richieste

