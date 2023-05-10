from gui import init_gui 
import scraper
import utils 
import subprocess
import sys
import tkinter.messagebox as messagebox
import os

def check_and_install_requirements():
    with open("requirements.txt", "r") as file:
        requirements = file.read().splitlines()

    missing_requirements = []
    for requirement in requirements:
        try:
            subprocess.check_output([sys.executable, "-m", "pip", "show", requirement], stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"Errore per la dipendenza {requirement}: {e}")
            missing_requirements.append(requirement)

    if missing_requirements:
        message = "Le seguenti dipendenze sono mancanti:\n\n" + "\n".join(missing_requirements) + "\n\nVuoi installarle?"
        answer = messagebox.askyesno("Dipendenze mancanti", message)

        if answer:
            if os.name == 'nt':  # Windows
                for requirement in missing_requirements:
                    subprocess.check_call(["powershell", "Start-Process", "pip", "-ArgumentList", "'install', '{}', '--user'".format(requirement), "-Verb", "RunAs"])
            else:  # Linux/macOS
                for requirement in missing_requirements:
                    subprocess.check_call(["sudo", sys.executable, "-m", "pip", "install", requirement])
        else:
            sys.exit(0)

def main():
    # Controlla e installa dipendenze
    #check_and_install_requirements()
    # Inizializza l'interfaccia grafica
    app = init_gui()

    # Inizializza l'intelligenza artificiale (se necessario)
    if app.use_ai():  # Usa 'app' al posto di 'gui'
        import ai
        ai.init_ai(api_key='your_api_key')

    # Avvia l'applicazione
    app.mainloop()

if __name__ == '__main__':
    main()




