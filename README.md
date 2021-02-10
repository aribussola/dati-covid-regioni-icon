# INDICE
### <a href=#intro>1. INTRODUZIONE</a>
### <a href=#dati>2. DATI</a>

<br/><br/><br/><br/>

<h2 id="intro"> 1. Introduzione </h2>
Il programma affronta diverse problematiche legate alla pandemia SARS CoV-2.

Il particolare, la gestione degli spostamenti tra regioni in base alle eventuali restrizioni.

Le restrizioni per gli spostamenti tra regioni sono imposte dal colore con cui sono contrassegnate, che indica il grado di emergenza.Più precisamente, in ordine crescente di criticità: white, yellow, orange, red.

Per una regione contrassegnata con il colore "red" (*) non è possibile superarne i confini.
*Il divieto è limitato alle sole zone rosse al fine di riuscire a mostrare al meglio le funzionalità dell’algoritmo di ricerca dei percorsi.

Per valutare la criticità dell'emergenza COVID si utilizza un EPI, ricavato da un dataset contenente l'andamento dei contagi giornaliero per ogni regione.<br><br>
```EPI (Epidemics Progression Index): valore che indica il tasso di contagiosità del virus dopo l’applicazione delle misure atte a contenere il diffondersi della malattia```<br>

In base agli EPI analizzati nel dataset, il programma effettua una previsione sull'andamento dell'epidemia per una settimana futura.
In seguito alla previsione, con l'ausilio di un ulteriore dataset che indica l'assegnamento delle restrizioni applicate nelle settimana precedenti, effettua una classificazione dei colori (restrizioni) per la settimana futura.

Infine, basandosi sui dati calcolati, una feature permette di ricercare il percorso (ove questo esista) per effettuare uno spostamento tra due regioni date in input con l'obiettivo di correre il minor rischio possibile.


<h2 id="dati"> 2. Dati </h2>

Il programma utilizza due differenti tipologie di data set disponibili tramite file .csv presenti su repository github:
1) **Dati sulle regioni**. In particolare un documento .csv per ogni regione in cui vengono indicati, suddivisi per giorni, i dati relativi ai casi totali per regione e numero di tamponi effettuati.<br>
Ad esempio la tabella della regione Puglia è così strutturata:<br><br>
![Help Example](/img/Immagine.png)<br><br>
Questi dati verranno utilizzati dal programma al fine del calcolo dell’EPI.<br><br>
2) Per il task della classificazione invece, viene utilizzata la tabella seguente, la quale contiene **aggiornamenti settimanali sui colori (restrizioni)** assegnati alle regioni.<br><br>
![Help Example](/img/Immagine2.png)<br>
