from gui import init_gui 
import scraper
import utils 

def main():
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