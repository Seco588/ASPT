<h1>ASPT - Amazon Scraping Project Tool</h1>
<p>ASPT (Amazon Scraping Project Tool) è un'applicazione Python basata su tkinter per estrarre informazioni sui prodotti da Amazon, utilizzando vari strumenti come Helium10, Keepa, JungleScout e intelligenza artificiale.</p>
<h2>Requisiti</h2>
<p>Per eseguire questo progetto, è necessario installare i seguenti pacchetti Python. Puoi trovare questi pacchetti nel file <code>requirements.txt</code>
:</p>
<ul><li>openai</li>
<li>pandas</li>
<li>beautifulsoup4</li>
<li>selenium</li>
<li>requests</li>
<li>tkinter</li>
</ul>
<h2>Struttura del progetto</h2>
<p>Il progetto è composto dai seguenti file:</p>
<ul><li><code>ai.py</code>: modulo per l'inizializzazione dell'intelligenza artificiale e per ottenere risposte dall'IA.</li>
<li><code>gui.py</code>: modulo che contiene la logica dell'interfaccia grafica e la classe principale dell'applicazione ASPT.</li>
<li><code>main.py</code>: punto di ingresso dell'applicazione, avvia l'interfaccia grafica e inizializza l'intelligenza artificiale (se necessario).</li>
<li><code>scraper.py</code>: modulo che contiene le funzioni per effettuare lo scraping delle pagine Amazon e utilizzare gli strumenti di terze parti (Helium10, Keepa e JungleScout).</li>
<li><code>utils.py</code>: modulo contenente funzioni di utilità per leggere e scrivere log e cambiare l'indirizzo IP (utilizzando NordVPN).</li>
</ul>
<h2>Utilizzo</h2>
<p>Per avviare l'applicazione, esegui il seguente comando nella directory del progetto:</p>
<pre class=""><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">
</div>
<div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-css">python main.py</code>
</div>
</div>
</pre>
<p>Nella finestra dell'applicazione, puoi selezionare gli strumenti che desideri utilizzare per lo scraping, specificare il percorso del file CSV contenente gli ASIN o EAN dei prodotti e decidere se abilitare il cambio IP. Dopo aver configurato le impostazioni, fai clic sul pulsante "Start Scraping" per avviare il processo di scraping.</p>
<p>I risultati dello scraping verranno salvati in un file <code>output.xlsx</code>
, con un foglio separato per ogni ASIN o EAN.</p>
<h2>Personalizzazione</h2>
<p>Per utilizzare l'intelligenza artificiale nel tuo progetto, sostituisci <code>'your_api_key'</code>
 nel file <code>main.py</code>
 con la tua chiave API di OpenAI.</p>
<p>Se vuoi utilizzare l'estensione Helium10 per Chrome, aggiungi il percorso del file <code>.crx</code>
 dell'estensione nella riga appropriata nel file <code>scraper.py</code>
.</p>
</div>
