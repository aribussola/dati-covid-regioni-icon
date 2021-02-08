# The main entry point for this module
from Grafo import Graph, realCost, heuristicsVector, astar_search
from Regione import Regione
from sklearn import tree
import pandas as pd #Manipolazione e analisi dei dati
 
lista = []
#Creazione regioni
ValleAosta = Regione("ValleAosta")
lista.append(ValleAosta)
Piemonte = Regione("Piemonte")
lista.append(Piemonte)
Lombardia = Regione("Lombardia")
lista.append(Lombardia)
Liguria =  Regione("Liguria")
lista.append(Liguria)
EmiliaRomagna = Regione("EmiliaRomagna")
lista.append(EmiliaRomagna)
Veneto = Regione ("Veneto")
lista.append(Veneto)
TrentinoAltoAdige = Regione ("TrentinoAltoAdige")
lista.append(TrentinoAltoAdige)
FriuliVeneziaGiulia = Regione("FriuliVeneziaGiulia")
lista.append(FriuliVeneziaGiulia)
Toscana =  Regione("Toscana")
lista.append(Toscana)
Marche = Regione("Marche")
lista.append(Marche)
Umbria = Regione("Umbria")
lista.append(Umbria)
Lazio = Regione("Lazio")
lista.append(Lazio)
Abruzzo = Regione("Abruzzo")
lista.append(Abruzzo)
Campania = Regione("Campania")
lista.append(Campania)
Molise = Regione ("Molise")
lista.append(Molise)
Puglia = Regione("Puglia")
lista.append(Puglia)
Basilicata = Regione("Basilicata")
lista.append(Basilicata)
Calabria = Regione("Calabria")
lista.append(Calabria)

def generateGraph () :
    # Create a graph
    graph = Graph()
    
    # Create graph connections (Actual distance)
    graph.connect(ValleAosta.name,Piemonte.name, realCost(ValleAosta.rt,Piemonte.rt))
    graph.connect(Piemonte.name,Lombardia.name, realCost(Piemonte.rt,Lombardia.rt))
    graph.connect(Liguria.name, EmiliaRomagna.name, realCost(Liguria.rt,EmiliaRomagna.rt))
    graph.connect(Liguria.name, Toscana.name, realCost(Liguria.rt,Toscana.rt))
    graph.connect(Piemonte.name, Liguria.name, realCost(Piemonte.rt,Liguria.rt))
    graph.connect(Piemonte.name, EmiliaRomagna.name, realCost(Piemonte.rt,EmiliaRomagna.rt))
    graph.connect(Lombardia.name, EmiliaRomagna.name, realCost(Lombardia.rt,EmiliaRomagna.rt))
    graph.connect(Lombardia.name, Veneto.name, realCost(Lombardia.rt,Veneto.rt))
    graph.connect(Lombardia.name, TrentinoAltoAdige.name, realCost(Lombardia.rt,TrentinoAltoAdige.rt))
    graph.connect(TrentinoAltoAdige.name, Veneto.name, realCost(TrentinoAltoAdige.rt,Veneto.rt))
    graph.connect(Veneto.name, FriuliVeneziaGiulia.name, realCost(Veneto.rt,FriuliVeneziaGiulia.rt))
    graph.connect(Veneto.name, EmiliaRomagna.name, realCost(Veneto.rt,EmiliaRomagna.rt))
    graph.connect(EmiliaRomagna.name, Toscana.name, realCost(EmiliaRomagna.rt,Toscana.rt))
    graph.connect(EmiliaRomagna.name, Marche.name, realCost(EmiliaRomagna.rt,Marche.rt))
    graph.connect(Toscana.name, Marche.name, realCost(Toscana.rt,Marche.rt))
    graph.connect(Toscana.name, Umbria.name, realCost(Toscana.rt,Umbria.rt))
    graph.connect(Toscana.name, Lazio.name, realCost(Toscana.rt,Lazio.rt))
    graph.connect(Marche.name, Umbria.name,realCost(Marche.rt,Umbria.rt))
    graph.connect(Marche.name, Lazio.name, realCost(Marche.rt,Lazio.rt))
    graph.connect(Marche.name, Abruzzo.name,realCost(Marche.rt,Abruzzo.rt))
    graph.connect(Umbria.name, Lazio.name,realCost(Umbria.rt,Lazio.rt))
    graph.connect(Lazio.name, Abruzzo.name, realCost(Lazio.rt,Abruzzo.rt))
    graph.connect(Lazio.name, Molise.name, realCost(Lazio.rt,Molise.rt))
    graph.connect(Lazio.name, Campania.name,realCost(Lazio.rt,Campania.rt))
    graph.connect(Abruzzo.name, Molise.name, realCost(Abruzzo.rt,Molise.rt))
    graph.connect(Molise.name, Campania.name, realCost(Molise.rt,Campania.rt))
    graph.connect(Molise.name, Puglia.name, realCost(Molise.rt,Puglia.rt))
    graph.connect(Campania.name, Puglia.name, realCost(Campania.rt,Puglia.rt))
    graph.connect(Campania.name, Basilicata.name, realCost(Campania.rt,Basilicata.rt))
    graph.connect(Puglia.name, Basilicata.name, realCost(Puglia.rt,Basilicata.rt))
    graph.connect(Basilicata.name, Calabria.name, realCost(Basilicata.rt,Calabria.rt))
    
    # Make graph undirected, create symmetric connections
    graph.make_undirected()
    return graph
    
def findPath (start, end):
    for i in range (len(lista)):
        if (lista[i].name==start):
            regioneStart = lista[i]
        if (lista[i].name==end):
            regioneEnd = lista[i]
    
    graph = generateGraph ()
    
    # Create heuristics (straight-line distance, air-travel distance)
    #Euristiche per la regione 
    heuristics = heuristicsVector (regioneEnd, lista)

    #path = astar_search(graph, heuristics, 'Emilia Romagna', 'Puglia')
    path = astar_search(graph, heuristics, regioneStart, regioneEnd)
    print(path)
  
def colorAssignment():
    linkDataset = "https://raw.githubusercontent.com/aribussola/dati-covid-regioni-icon/main/Italia-dataSet-COVID/TrainingSet(Colori).csv"
    data = pd.read_csv(linkDataset)
    regione = data['regione']
    popolazione = data['popolazione']
    colore = data['colore']
    X = []
    Y = []

    for i in range (len(popolazione)):
        for j in range (len(lista)):
            if (lista[j].name==regione[i]):
                   rt=lista[j].avgRtByDate()
                   break
        print(regione[i])
        print(colore[i])
        X.append([popolazione[i],rt])
        Y.append([colore[i]])

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    
    for i in range (len(popolazione)):
        for j in range (len(lista)):
            if (lista[j].name==regione[i]):
                   rt=lista[j].rt
                   break
        print(regione[i])
        print(clf.predict([[popolazione[i],rt]]))
        