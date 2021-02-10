# -*- coding: utf-8 -*-
import pandas as pd #Manipolazione e analisi dei dati
import matplotlib.pyplot as plt #Creazione grafici
from sklearn import linear_model #Creazione regressore per apprendimento e previsione
from sklearn.metrics import max_error #Metrica di errore
from datetime import datetime #Conversione date
from datetime import timedelta #Conversione date

class Regione:
    # Initialize the class
    def __init__(self, name:str):
        self.name = name
        self.rt = self.avgRT()
        self.color = ""
              
    def avgRtByDate(self, dataCalcolo):
        #ADDESTRAMENTO
        linkDataset = "https://raw.githubusercontent.com/aribussola/dati-covid-regioni-icon/main/Italia-dataSet-COVID/" + self.name +".csv"
        data = pd.read_csv(linkDataset)
        datePresenti = data['data']
        tc = data['totale_casi']
        tt = data['tamponi']
        
        contatore=0
        for i in range (len(datePresenti)):
            if (dataCalcolo == datePresenti[i]):
                contatore=i+1
                break
        contatore2 = contatore - 6
        y = [] # EPI
        tt_increase = []
        avgEPI = 0
        for i in range(contatore2, contatore):
            current_epi = (tc[i] - tc[i-1])/(tt[i]-tt[i-1])*100
            tt_increase.append(tt[i]-tt[i-1])
            y.append(current_epi)
            avgEPI = avgEPI + current_epi
            
        avgEPI = avgEPI / len(y)
        return avgEPI
    
    def avgRT(self):
        #ADDESTRAMENTO
        linkDataset = "https://raw.githubusercontent.com/aribussola/dati-covid-regioni-icon/main/Italia-dataSet-COVID/" + self.name +".csv"
        data = pd.read_csv(linkDataset) 
        tc = data['totale_casi']
        tt = data['tamponi']
        y = [] # EPI
        tt_increase = []
        
        for i in range(1, len(tt)):
            current_epi = (tc[i] - tc[i-1])/(tt[i]-tt[i-1])*100
            tt_increase.append(tt[i]-tt[i-1])
            y.append(current_epi)
            data['data']

        X = []  # Conversione date (stringhe) in numeri 
        for i in range(1, len(y)+1):
            X.append([i])
           
        #CALCOLO RT E CREAZIONE REGRESSORE
        start = len(tt)-14 #giorno inizio previsioni
    
        # Costruzione del modello di apprendimento
        X = X[start:]
        y = y[start:]
    
        # Costruire un regressore lineare che rappresenti l'EPI, adatti il regressore e calcoli il punteggio
        linear_regr = linear_model.LinearRegression()

        # Addestrare il modello utilizzando i set di addestramento 
        linear_regr.fit(X, y)
        linear_regr.score(X,y)

        # Prevedere l'andamento futuro
        y_pred = linear_regr.predict(X)
        error = max_error(y, y_pred)
        error
        
        X_test = [] # Contiene sia i vecchi giorni (cioè i giorni per i quali i dati sono già disponibili) sia i giorni futuri
        gp = 21 # Numero di giorni di previsione
        for i in range(start, start + gp):
            X_test.append([i])
            y_pred_linear = linear_regr.predict(X_test) # Previsione dell'EPI per i giorni futuri
            
        
        # Calcolo dell'errore commesso dal modello
        avgEPI = 0
        
        for i in range(0, len(y_pred_linear)):
            if(i>13):
                avgEPI = avgEPI + y_pred_linear[i]    
            
        avgEPI = avgEPI / 7
    
        print(avgEPI)
        return avgEPI     

    #Fare NomeRegione.printGraphics
    def printGraphics(self):
        linkDataset = "https://raw.githubusercontent.com/aribussola/dati-covid-regioni-icon/main/Italia-dataSet-COVID/" + self.name +".csv"
        data = pd.read_csv(linkDataset) 
        tc = data['totale_casi']
        tt = data['tamponi']
        y = [] # EPI
        tt_increase = []
        #Primo Grafico
        for i in range(1, len(tt)):
            current_epi = (tc[i] - tc[i-1])/(tt[i]-tt[i-1])*100
            tt_increase.append(tt[i]-tt[i-1])
            y.append(current_epi)
            data['data']

        X = []  # Conversione date (stringhe) in numeri 
        for i in range(1, len(y)+1):
            X.append([i])


        # Grafico andamento epidemia    
        plt.scatter(X, y, color='black')
        plt.grid()
        plt.xlabel('Days')
        plt.xlim(0,14)
        plt.ylim(0,25)
        elencoDate = data['data']
        elencoDateGrafico = []
        for i in range (14):
            elencoDateGrafico.append(elencoDate[i][6:10])
            
        plt.xticks([0,1,2,3,4,5,6,7, 8, 9, 10, 11, 12, 13],
               elencoDateGrafico)
        plt.ylabel('Epidemics Progression Index (EPI)')
        plt.savefig("EPI-all.png")
        plt.show()

        #Secondo Grafico
        #CALCOLO RT E CREAZIONE REGRESSORE
        start = len(tt)-14 #giorno inizio previsioni
    
        # Costruzione del modello di apprendimento
        X = X[start:]
        y = y[start:]
    
        # Costruire un regressore lineare che rappresenti l'EPI, adatti il regressore e calcoli il punteggio
        linear_regr = linear_model.LinearRegression()

        # Addestrare il modello utilizzando i set di addestramento 
        linear_regr.fit(X, y)
        linear_regr.score(X,y)

        # Prevedere l'andamento futuro
        y_pred = linear_regr.predict(X)
        error = max_error(y, y_pred)
        error
        
        X_test = [] # Contiene sia i vecchi giorni (cioè i giorni per i quali i dati sono già disponibili) sia i giorni futuri
        gp = 21 # Numero di giorni di previsione
        for i in range(start, start + gp):
            X_test.append([i])
            y_pred_linear = linear_regr.predict(X_test) # Previsione dell'EPI per i giorni futuri
            
        
        # Calcolo dell'errore commesso dal modello
        y_pred_max = []
        y_pred_min = []
        
        for i in range(0, len(y_pred_linear)):
            y_pred_max.append(y_pred_linear[i] + error)
            y_pred_min.append(y_pred_linear[i] - error)
            
        
        #Parte di grafica
        # Tracciare tre linee (output della previsione, errore massimo ed l'errore minimo)
        data_eff = datetime.strptime(data['data'][start], '%Y-%m-%dT%H:%M:%S')
    
        date_prev = [] # Date previsione
        x_ticks = []
        step = 1
        data_curr = data_eff
        x_current = start
        n = int(gp/step)
        for i in range(0, n):
            date_prev.append(str(data_curr.day) + "/" + str(data_curr.month))
            x_ticks.append(x_current)
            data_curr = data_curr + timedelta(days=step)
            x_current = x_current + step
        
        # Grafico finale
        plt.grid()
        plt.scatter(X, y, color='black')
        plt.plot(X_test, y_pred_linear, color='green', linewidth=2)
        plt.plot(X_test, y_pred_max, color='red', linewidth=1, linestyle='dashed')
        plt.plot(X_test, y_pred_min, color='red', linewidth=1, linestyle='dashed')
        plt.xlabel('Days')
        plt.xlim(start,start+gp)
        plt.xticks(x_ticks, date_prev)
        plt.ylabel('Epidemics Progression Index (EPI)')
        plt.yscale("log")
        plt.savefig("EPI-prediction.png")
        plt.show()