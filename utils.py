import requests
import json

def write_log(log_data, log_file='logs.json'):
    with open(log_file, 'a') as file:
        json.dump(log_data, file)

def read_log(log_file='logs.json'):
    with open(log_file, 'r') as file:
        log_data = json.load(file)
    return log_data

def change_ip():
    # Codice per connettersi a NordVPN e cambiare l'IP
    # Assicurati di avere NordVPN e la sua CLI (Command Line Interface) installata sul tuo computer e di essere connesso con il tuo account NordVPN. 
    # Per ulteriori dettagli su come utilizzare la CLI di NordVPN, consulta la documentazione ufficiale: https://support.nordvpn.com/Connectivity/Linux/1325531132/Installing-and-using-NordVPN-on-Linux.htm
    
    # Disconnetti da NordVPN, se connesso
    try:
        subprocess.run(["nordvpn", "disconnect"], check=True, timeout=10)
    except subprocess.CalledProcessError:
        print("Errore durante la disconnessione da NordVPN.")
    except subprocess.TimeoutExpired:
        print("Timeout scaduto durante la disconnessione da NordVPN.")
    
    # Connettiti a NordVPN con il protocollo di connessione rapida
    try:
        result = subprocess.run(["nordvpn", "connect"], check=True, timeout=30)
        if result.returncode == 0:
            print("Connesso a NordVPN.")
        else:
            print("Errore durante la connessione a NordVPN.")
    except subprocess.CalledProcessError:
        print("Errore durante la connessione a NordVPN.")
    except subprocess.TimeoutExpired:
        print("Timeout scaduto durante la connessione a NordVPN.")
