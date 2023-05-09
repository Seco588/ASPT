from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def scrape_amazon_page(url, headers):
    processed_scrape_amazon_page_data = {}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Esegui lo scraping delle informazioni dalla pagina Amazon qui
        # ad esempio: titolo, prezzo, descrizione, recensioni, ecc.
    
    except Exception as e:
        log_queue.put(f"Errore durante l'estrazione con Scrape Amazon Page: {str(e)}")
    return processed_scrape_amazon_page_data
    
def scrape_helium10(asin_or_ean, log_queue):
    extracted_data = {}
    try:
        # Codice per effettuare lo scraping con Helium10 (usando Selenium)
        # Configura Selenium per utilizzare l'estensione Helium10
        chrome_options = Options()
        chrome_options.add_extension("path/to/helium10_chrome_extension.crx")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        # Apri la pagina Amazon corrispondente all'ASIN o EAN
        url = f"https://www.amazon.com/dp/{asin_or_ean}"
        driver.get(url)

        # Aspetta che l'estensione Helium10 aggiunga le informazioni alla pagina
        time.sleep(10)  # Aumenta il tempo di attesa se necessario

        # Esegui lo scraping delle informazioni aggiunte da Helium10
        # ad esempio: grafici, valutazioni, ecc.

        # Chiudi il browser e restituisci i dati estratti
        driver.quit()
    except Exception as e:
        log_queue.put(f"Errore durante l'estrazione con Helium10: {str(e)}")
    return extracted_data
    
def scrape_keepa(asin_or_ean, api_key):
    processed_keepa_data = {}
    try:
        # Codice per effettuare lo scraping con Keepa
        # Costruisci la richiesta all'API di Keepa e ottieni i dati
        # Consulta la documentazione di Keepa per ulteriori dettagli
        url = f"https://api.keepa.com/product?key={api_key}&domain=1&asin={asin_or_ean}"
        response = requests.get(url)
        keepa_data = response.json()

        # Elabora i dati di Keepa come necessario
        # ad esempio: prezzo, classifica, ecc.
    except Exception as e:
        log_queue.put(f"Errore durante l'estrazione con Keepa: {str(e)}")
    return processed_keepa_data
    

def scrape_junglescout(asin_or_ean, api_key):
    processed_junglescout_data = {}
    try:
        # Codice per effettuare lo scraping con JungleScout
        # Costruisci la richiesta all'API di JungleScout e ottieni i dati
        # Consulta la documentazione di JungleScout per ulteriori dettagli
        headers = {"Authorization": f"Bearer {api_key}"}
        url = f"https://api.junglescout.com/asin/{asin_or_ean}"
        response = requests.get(url, headers=headers)
        junglescout_data = response.json()

        # Elabora i dati di JungleScout come necessario
        # ad esempio: vendite mensili, fatturato mensile, ecc.
    except Exception as e:
        log_queue.put(f"Errore durante l'estrazione con JungleScout: {str(e)}")
    return processed_junglescout_data
    
def scrape_ai(asin_or_ean):
    processed_ai_data = {}
    try:
        # Inserisci qui il codice esistente per l'estrazione con l'IA
        # Codice per utilizzare AI per migliorare lo scraping
        openai.api_key = api_key

        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Elabora i dati ottenuti dall'IA e aggiungi le informazioni rilevanti a processed_ai_data
        # Ad esempio, si potrebbe estrarre informazioni sul prodotto o suggerimenti sulla sua popolarità
    except Exception as e:
        log_queue.put(f"Errore durante l'estrazione con l'IA: {str(e)}")
    return processed_ai_data

def do_scraping(params, log_queue):
    asin_or_ean_list = []
    try:
        # Leggi gli ASIN o EAN dal file CSV
        with open(params["csv_file"], 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                asin_or_ean_list.extend(row)  # Aggiungi tutti gli elementi separati da "," alla lista

    except Exception as e:
        log_queue.put(f"Errore durante la lettura del file CSV: {str(e)}")
        return

    # Crea un oggetto ExcelWriter per salvare i risultati in un file Excel
    writer = pd.ExcelWriter("output.xlsx", engine='xlsxwriter')

    for index, asin_or_ean in enumerate(asin_or_ean_list):
        extracted_data = []

        if params["change_ip_enabled"] and index % params["change_ip_every"] == 0:
            change_ip()

        if params["tools"]["helium10"]:
            extracted_data = scrape_with_helium10(asin_or_ean, log_queue)

        if params["tools"]["keepa"]:
            keepa_data = get_keepa_data(asin_or_ean, params["api_keys"]["keepa"])
            extracted_data.update(keepa_data)

        if params["tools"]["junglescout"]:
            junglescout_data = get_junglescout_data(asin_or_ean, params["api_keys"]["junglescout"])
            extracted_data.update(junglescout_data)

        if params["tools"]["ai"]:
            prompt = f"[AI] -> Informazioni sul prodotto ASIN/EAN {asin_ean} su Amazon"
            ai_data = get_ai_data(asin_ean, params["api_keys"]["openai"], prompt)
            extracted_data.update(ai_data)

        # Esegui lo scraping delle pagine Amazon e salva i risultati in un DataFrame
        url = f"https://www.amazon.com/dp/{asin_or_ean}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }

        # Aggiungi le informazioni estratte con scraping
        extracted_data = scrape_amazon_page(url, headers)

        # Invia messaggi di log alla coda per aggiornare la GUI
        log_queue.put(f"Scraped data for {asin_or_ean}")

        # Salva i risultati in un DataFrame e aggiungi il DataFrame come foglio nel file Excel
        df = pd.DataFrame(extracted_data)
        df.to_excel(writer, sheet_name=f"{asin_or_ean}", index=False)

    # Salva il file Excel con tutti i fogli
    writer.save()
