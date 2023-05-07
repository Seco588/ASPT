# scraper.py: conterrà il codice per lo scraping dei dati da Amazon.
import requests
from bs4 import BeautifulSoup
import csv
import time
from utils import save_to_excel, change_ip


# Definisco una funzione per estrarre i dati del prodotto da Amazon


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
        rating = rating_element.get_text().strip(
        ) if rating_element else "Valutazione non trovata"

        # Estrai il numero di recensioni
        reviews_element = soup.find("span", {"id": "acrCustomerReviewText"})
        reviews = reviews_element.get_text().strip(
        ) if reviews_element else "Recensioni non trovate"

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


# Inserisci qui la tua chiave API di Helium 10
#HELIUM_10_API_KEY = "your_api_key_here"

#def scrape_amazon(asin):
#   url = f"https://api.helium10.com/v1/product/{asin}"
#   headers = {
#       "x-api-key": HELIUM_10_API_KEY,
#   }
#
#   response = requests.get(url, headers=headers)
#
#   if response.status_code == 200:
#       data = response.json()
#
#       # Estrai i dati del prodotto dall'API di Helium 10
#       title = data["title"]
#       price = data["price"]
#       rating = data["rating"]
#       reviews = data["reviews_count"]
#       sales_rank = data["sales_rank"]
#
#       return {"asin": asin, "title": title, "price": price, "rating": rating, "reviews": reviews, "sales_rank": sales_rank}
#   else:
#       print(f"Errore nella richiesta: {response.status_code}")
#       return None




# Funzione per leggere il file CSV e avviare lo scraping


def read_csv_and_scrape(file_path, output_folder):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        request_count = 0

        for row in reader:
            for asin_or_ean in row:  # Itera su tutti gli elementi in ogni riga
                print(f"Scraping {asin_or_ean}...")
                product_data = scrape_amazon(asin_or_ean)
                if product_data:
                    print(product_data)
                    # Salva i dati del prodotto in un file Excel
                    save_to_excel(product_data, output_folder)

                request_count += 1

                if request_count % 3 == 0:  # Cambia IP ogni 3 richieste
                    change_ip()

                # Attendi 60 secondi (1 minuto) tra le richieste
                time.sleep(60)
