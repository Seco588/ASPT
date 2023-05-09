import gui 
import scraper
import utils 

def main():
    # Inizializza l'interfaccia grafica
    app = gui.init_gui()

    # Inizializza l'intelligenza artificiale (se necessario)
    if gui.use_ai():
        import ai
        ai.init_ai(api_key='your_api_key')

    # Avvia l'applicazione
    app.mainloop()

if __name__ == '__main__':
    main()
