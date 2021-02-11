# INDICE
### <a href=#intro>1. INTRODUZIONE</a>
### <a href=#dati>2. DATI</a>
### <a href=#regioni>3. REGIONI</a>
### <a href=#previsione>4. PREVISIONE</a>
### <a href=#classificazione>5. CLASSIFICAZIONE</a>
### <a href=#percorso>6. RICERCA PERCORSO</a>

<h2 id="intro"> 1. Introduzione </h2>
Il programma affronta diverse problematiche legate alla pandemia SARS-CoV-2.

Il particolare, la gestione degli spostamenti tra regioni in base alle eventuali restrizioni.

Le restrizioni per gli spostamenti tra regioni sono imposte dal colore con cui sono contrassegnate, che indica il grado di emergenza. Più precisamente, in ordine crescente di criticità: white, yellow, orange, red.

Per una regione contrassegnata con il colore "red" (*) non è possibile superarne i confini.
>*Il divieto è limitato alle sole zone rosse al fine di riuscire a mostrare al meglio le funzionalità dell’algoritmo di ricerca dei percorsi.

Per valutare la criticità dell'emergenza SARS-CoV-2 si utilizza un EPI, ricavato da un dataset contenente l'andamento dei contagi giornaliero per ogni regione.<br><br>
```EPI (Epidemics Progression Index): https://www.cdc.gov/foodsafety/outbreaks/investigating-outbreaks/epi-curves.html```<br>

In base agli EPI analizzati nel dataset, il programma effettua una previsione sull'andamento dell'epidemia per una settimana futura.
In seguito alla previsione, con l'ausilio di un ulteriore dataset che indica l'assegnamento delle restrizioni applicate nelle settimana precedenti, effettua una classificazione dei colori (restrizioni) per la settimana futura.

Infine, basandosi sui dati calcolati, una feature permette di ricercare il percorso (ove questo esista) per effettuare uno spostamento tra due regioni date in input con l'obiettivo di correre il minor rischio possibile.


<h2 id="dati"> 2. Dati </h2>

Il programma utilizza tre differenti tipologie di data set disponibili tramite file .csv presenti su repository github:<br><br>
2.1) **Dati sulle regioni**. In particolare un documento .csv per ogni regione in cui vengono indicati, suddivisi per giorni, i dati relativi ai casi totali per regione e numero di tamponi effettuati.<br>
Ad esempio la tabella della regione Puglia è così strutturata:<br><br>
![Help Example](/img/Immagine.PNG)<br><br>
Questi dati verranno utilizzati dal programma al fine del calcolo dell’EPI.<br><br>
2.2) Per il task della classificazione invece, viene utilizzata la tabella seguente, la quale contiene **aggiornamenti settimanali sui colori (restrizioni)** assegnati alle regioni.<br><br>
![Help Example](/img/TabellaColori.PNG)<br><br>
2.3) Dati inerenti la popolazione di ogni regione per effettuare con una maggiore precisione il task di classificazione<br><br>
![Help Example](/img/TabellaPopolazione.PNG)<br>

<h2 id="regioni"> 3. Regioni</h2>
Nel programma ogni regione è stata rappresentata mediante un'apposita classe (Regione.py), così definita:<br><br>
<table>
<tr><td>Attributi</td></tr>
<tr><td>name</td><td>Nome della regione</td></tr>
<tr><td>epi</td><td>EPI medio calcolato per la settimana futura rispetto agli utimi dati registati nel dataset</td></tr>
<tr><td>color</td><td>Colore ("white","yellow","orange","red") che indica il grado di criticità dei contagi</td></tr>
</table>
<table>
<tr><td>Metodi</td></tr>
<tr><td>avgEPIByDate (self, dataCalcolo)</td><td>Metodo per il calcolo dell'EPI medio, a partire da una settimana prima fino ad una data passata in input</td></tr>
<tr><td>avgEPI (self)</td><td>Metodo per il calcolo dell'EPI medio calcolato per la settimana futura rispetto agli utimi dati registati nel dataset</td></tr>
<tr><td>printGraphics(self)</td><td>Metodo per la visualizzazione dei grafici inenerenti l'andamento dei contagi registrati nelle ultime due settimane (prima della previsione) e la curva epidemiologica della previsione (con relativi margini di errore)</td></tr>
</table>


<h2 id="previsione"> 4. Previsione</h2>
L’applicazione, mediante l’accesso ad un data set, permette di effettuare delle predizioni sull’andamento del tasso di contagiosità (EPI) nella settimana seguente rispetto a quella dei dati di training.

In particolare, la previsione viene effettuata per ogni singola regione, mediante l’apposito metodo avgEPI della classe Regione. Per effettuare la previsione, il programma si basa sull’utilizzo di un **regressore linare** che opera con le informazioni relative agli ultimi 14 giorni presenti nel dataset mostrato precedentemente nella sezione Dati.
> La **regressione lineare** è una tecnica di modellazione statistica utilizzata per descrivere una varabile di risposta continua in funzione di una o più variabili (predittori). Può contribuire a comprendere e a prevedere il comportamento di sistemi complessi, nonché ad analizzare dati.
Le regressioni lineari hanno delle proprietà che le rendono particolarmente utili per effetuare **predizioni o previsioni** (utilizzo di un modello di regressione per creare un modello di previsione per un set di dati specifico; dal modello, è possibile usare la regressione per prevedere i valori di risposta quando sono noti solo i predittori).

![Help Example](/img/EPI-all.png)

Il programma quindi, con l’ausilio del regressore lineare, calcola un ipotetico andamento della curva epidemiologica, che viene mostrato e visualizzato all’interno di grafici generati dal programma, affinchè si possa fornire una rappresentazione più intuitiva ai tassi di contagiosità calcolati per la settimana successiva.

Inoltre, il programma calcola anche l’**errore massimo e minimo** commesso dal modello nella predizione, e anch’esso viene mostrato nel grafico insieme all’andamento della curva previsto.

![Help Example](/img/EPI-prediction.png)

I **grafici** con tutte queste informazioni vengono mostrate richiamando sull’oggetto Regione d’interesse, il metodo printGraphics.

<h2 id="classificazione"> 5. Classificazione</h2>
Il programma, raccogliendo dati sulle restrizioni associate ad ogni regione nelle ultime settimane, utilizza un **albero di decisione** per classificare le regioni nella settimana oggetto della predizione.<br>

>Un albero di decisione è un albero di classificatori (Decision Stump) dove ogni nodo interno è associato ad una particolare “domanda” su una caratteristica (feature). Da questo nodo dipartono tanti archi quanti sono i possibili valori che la caratteristica può assumere, fino a raggiungere le foglie che indicano la categoria associata alla decisione.

In particolare utilizza come **training set** l'elenco delle regioni a cui sono associati:
1. Come feature di **input**, di ogni regione, il **numero di abitanti** e l'**EPI medio** calcolato nella settimana d'interesse;<br>
2. Come **target** il **colore** assegnato alla regione nella settimana d'interesse.<br>
Il numero di abitanti di ogni regione viene rilevato dalla tabella "TrainingSet(Popolazione).csv", il colore per la settimana presa in considerazione viene rilevato dalla tabella "TrainingSet(Colori).csv", mentre l'EPI medio della settimana viene calcolato appositamente dalla funzione avgEPIByDate(self,dataCalcolo) descritta nella sezione 'Regione' che permette di calcolare il valore richiesto passando in input l'ultimo giorno della settimana.

Allenandosi su questi dati, l'albero di decisione sarà in grado di assegnare alle regioni il colore corretto per la settimana oggetto della  previsione, basandosi sulle stesse feature di input "popolazione" ed "EPI" (predetto dalla funzione di previsione).

Il classificatore potrà essere mandato in esecuzione dall'utente mediante la funzione "printColors()", la quale stamperà a video i colori assegnati ad ogni regione nel seguente modo: 

<h2 id="percorso"> 6. Ricerca Percorso</h2>
 
