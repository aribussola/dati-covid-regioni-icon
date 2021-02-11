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
Sardegna = Regione("Sardegna")
lista.append(Sardegna)
Sicilia = Regione("Sicilia")
lista.append(Sicilia)

def generateGraph () :
    # Create a graph
    graph = Graph()
    colorAssignment()
    # Create graph connections
   
    graph.connect(ValleAosta.name,Piemonte.name, realCost(ValleAosta.epi,Piemonte.epi))
    graph.connect(Piemonte.name,Lombardia.name, realCost(Piemonte.epi,Lombardia.epi))
    graph.connect(Liguria.name, EmiliaRomagna.name, realCost(Liguria.epi,EmiliaRomagna.epi))
    graph.connect(Liguria.name, Toscana.name, realCost(Liguria.epi,Toscana.epi))
    graph.connect(Piemonte.name, Liguria.name, realCost(Piemonte.epi,Liguria.epi))
    graph.connect(Piemonte.name, EmiliaRomagna.name, realCost(Piemonte.epi,EmiliaRomagna.epi))
    graph.connect(Lombardia.name, EmiliaRomagna.name, realCost(Lombardia.epi,EmiliaRomagna.epi))
    graph.connect(Lombardia.name, Veneto.name, realCost(Lombardia.epi,Veneto.epi))
    graph.connect(Lombardia.name, TrentinoAltoAdige.name, realCost(Lombardia.epi,TrentinoAltoAdige.epi))
    graph.connect(TrentinoAltoAdige.name, Veneto.name, realCost(TrentinoAltoAdige.epi,Veneto.epi))
    graph.connect(Veneto.name, FriuliVeneziaGiulia.name, realCost(Veneto.epi,FriuliVeneziaGiulia.epi))
    graph.connect(Veneto.name, EmiliaRomagna.name, realCost(Veneto.epi,EmiliaRomagna.epi))
    graph.connect(EmiliaRomagna.name, Toscana.name, realCost(EmiliaRomagna.epi,Toscana.epi))
    graph.connect(EmiliaRomagna.name, Marche.name, realCost(EmiliaRomagna.epi,Marche.epi))
    graph.connect(Toscana.name, Marche.name, realCost(Toscana.epi,Marche.epi))
    graph.connect(Toscana.name, Umbria.name, realCost(Toscana.epi,Umbria.epi))
    graph.connect(Toscana.name, Lazio.name, realCost(Toscana.epi,Lazio.epi))
    graph.connect(Marche.name, Umbria.name,realCost(Marche.epi,Umbria.epi))
    graph.connect(Marche.name, Lazio.name, realCost(Marche.epi,Lazio.epi))
    graph.connect(Marche.name, Abruzzo.name,realCost(Marche.epi,Abruzzo.epi))
    graph.connect(Umbria.name, Lazio.name,realCost(Umbria.epi,Lazio.epi))
    graph.connect(Lazio.name, Abruzzo.name, realCost(Lazio.epi,Abruzzo.epi))
    graph.connect(Lazio.name, Molise.name, realCost(Lazio.epi,Molise.epi))
    graph.connect(Lazio.name, Campania.name,realCost(Lazio.epi,Campania.epi))
    graph.connect(Abruzzo.name, Molise.name, realCost(Abruzzo.epi,Molise.epi))
    graph.connect(Molise.name, Campania.name, realCost(Molise.epi,Campania.epi))
    graph.connect(Molise.name, Puglia.name, realCost(Molise.epi,Puglia.epi))
    graph.connect(Campania.name, Puglia.name, realCost(Campania.epi,Puglia.epi))
    graph.connect(Campania.name, Basilicata.name, realCost(Campania.epi,Basilicata.epi))
    graph.connect(Puglia.name, Basilicata.name, realCost(Puglia.epi,Basilicata.epi))
    graph.connect(Basilicata.name, Calabria.name, realCost(Basilicata.epi,Calabria.epi))
    graph.connect(Calabria.name, Sicilia.name, realCost(Calabria.epi,Sicilia.epi))
    graph.connect(Sicilia.name, Sardegna.name, realCost(Sicilia.epi,Sardegna.epi))
    
    
    # Make graph undirected, create symmetric connections
    graph.make_undirected()
    regioni = lista.copy()
    i = 0
    while(i < (len(regioni))):
        if(regioni[i].color == "red"):
             graph.remove(regioni, regioni[i].name)        
             regioni.pop(i)
             i = i-1
        i = i+1
        
    return graph

def getRegione (nameRegione):
    for i in range (len(lista)):
        if (nameRegione==lista[i].name):
            return lista[i]
    return None

def findPath (start, end):

    regioneStart = None
    regioneEnd = None
    for i in range (len(lista)):
        if lista[i].name.lower()==start.lower():
            regioneStart = lista[i]
        if lista[i].name.lower()==end.lower():
            regioneEnd = lista[i]
            
    if(regioneStart == None or regioneEnd == None):
        print("Inserimento errato!")
        return
    graph = generateGraph ()
    
    #Euristiche per la regione 
    heuristics = heuristicsVector (regioneEnd, lista)

    path = astar_search(graph, heuristics, regioneStart, regioneEnd)
    print(path)
  
def colorAssignment():
    linkDataset = "https://raw.githubusercontent.com/aribussola/dati-covid-regioni-icon/main/Italia-dataSet-COVID/TrainingSet(Colori).csv"
    data = pd.read_csv(linkDataset)
    regione = data['regione']
    dateInfo = data['data']
    popolazione = getPopolazioni()
    colore = data['colore']
    X = []
    Y = []

    for i in range (len(regione)):
        for j in range (len(lista)):
            if (lista[j].name==regione[i]):
                   epi=lista[j].avgEPIByDate(dateInfo[j])
                   break
        X.append([popolazione.get(regione[i]),epi])
        Y.append([colore[i]])

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    
    for i in range (len(popolazione)):
        for j in range (len(lista)):
            if (lista[j].name==regione[i]):
                   epi=lista[j].epi
                   break
        color=clf.predict([[popolazione.get(regione[i]),epi]])
        for k in range (len(lista)):
            if (regione[i]==lista[k].name):
                lista[k].color=color
                
    return tree,clf
                
def getPopolazioni():
    linkDatasetPopolazione = "https://raw.githubusercontent.com/aribussola/dati-covid-regioni-icon/main/Italia-dataSet-COVID/TrainingSet(Popolazione).csv"
    dataPopolazione = pd.read_csv(linkDatasetPopolazione)
    popolazioni = dataPopolazione['popolazione']
    regioni = dataPopolazione['regione']
    elencoPop = {}
    for i in range(len(regioni)):
        elencoPop.update({regioni[i]:popolazioni[i]})
    return elencoPop

def printColors():
    colorAssignment()
    for i in range(len(lista)):
        print(lista[i].name,":" , lista[i].color)
   
def printTree():
    tree,clf = colorAssignment()
    tree.plot_tree(clf)    
    
