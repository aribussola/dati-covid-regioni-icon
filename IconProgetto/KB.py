from MainClass import lista,colorAssignment

colorAssignment()

def trovaRegioniRosse():
    listaRed = {}
    #colorAssignment()
    for i in range(len(lista)):
        if(lista[i].color == 'red'):
            listaRed[lista[i].name] = True
    return listaRed

def assegnaColori():
    #colorAssignment()
    stringa = ""
    listaColori = {}
    for i in range(len(lista)):
        #atomo regione_colore = true
        colore = lista[i].color[0]
        stringa = (lista[i].name+"_"+colore)
        listaColori[stringa] = True
    return listaColori

listaColori = assegnaColori()

def createListaAdiacenze():
    listaAdiacenze = {}
    listaAdiacenze["CampaniaBasilicata"]=True
    listaAdiacenze["BasilicataCalabria"]=True
    listaAdiacenze["CalabriaSicilia"]=True
    listaAdiacenze["SiciliaSardegna"]=True
    listaAdiacenze["PugliaBasilicata"]=True
    listaAdiacenze["PugliaMolise"]=True
    listaAdiacenze["MoliseAbruzzo"]=True
    listaAdiacenze["PugliaCampania"]=True
    listaAdiacenze["MoliseCampania"]=True
    listaAdiacenze["MoliseLazio"]=True
    listaAdiacenze["AbruzzoLazio"]=True
    listaAdiacenze["CampaniaLazio"]=True
    listaAdiacenze["AbruzzoMarche"]=True
    listaAdiacenze["LazioToscana"]=True
    listaAdiacenze["LazioUmbria"]=True
    listaAdiacenze["MarcheLazio"]=True
    listaAdiacenze["MarcheUmbria"]=True
    listaAdiacenze["ToscanaUmbria"]=True
    listaAdiacenze["ToscanaMarche"]=True
    listaAdiacenze["ToscanaEmiliaRomagna"]=True
    listaAdiacenze["MarcheEmiliaRomagna"]=True
    listaAdiacenze["ToscanaLiguria"]=True
    listaAdiacenze["EmiliaRomagnaLiguria"]=True
    listaAdiacenze["PiemonteLiguria"]=True
    listaAdiacenze["EmiliaRomagnaPiemonte"]=True
    listaAdiacenze["EmiliaRomagnaLombardia"]=True
    listaAdiacenze["EmiliaRomagnaVeneto"]=True
    listaAdiacenze["PiemonteLombardia"]=True
    listaAdiacenze["PiemonteValleAosta"]=True
    listaAdiacenze["LombardiaTrentinoAltoAdige"]=True
    listaAdiacenze["LombardiaVeneto"]=True
    listaAdiacenze["VenetoTrentinoAltoAdige"]=True
    listaAdiacenze["VenetoFriuliVeneziaGiulia"]=True
    return listaAdiacenze

lista_adiacenza = createListaAdiacenze()

def askColor(regione:str,colore:str):
    
    #controllo regione scritta bene
    if(not regioneEsiste(regione)):
        print("La regione inserita non esiste")
        return
    #controllo colore scritto bene
    if(not (colore == "red" or colore == "yellow" or colore == "orange" or colore == "white")):
        print("Hai inserito un colore non valido")
        return
    
    stringa = regione+"_"+colore
    risposta = findColor(stringa)
    if(risposta):
        print("YES")
    else:
        print("NO")
        
    regione = regione.capitalize()
    rispostaUtente=input("Digitare how per la spiegazione: ")
    if (rispostaUtente.lower()=="how"):
       print("color("+regione+","+colore+") <=> "+stringa)
       rispostaUtente=input("Digitare 'how i' specificando in i il numero dell'atomo per ulteriori informazioni: ")
       if(rispostaUtente.lower()=='how 1'):
           print(stringa + " <=>", risposta)
       else:
           print("Errore di digitazione")
    else:
         print("Errore di digitazione")

def findColor(regione_colore:str):
    if(listaColori.get(regione_colore) == None):
        return False
        #askColor(regione,colore) se e solo se regione_colore
    else:
        return True
        #askColor(regione,colore) se e solo se regione_colore
       
def regioneEsiste(regione:str):
    for i in range(len(lista)):
        if(lista[i].name == regione):
            return True
    return False
    
def notRed(regione:str):
    if(listaColori.get(regione+"_red")==None):
        return True
    else:
        return False

def askPassaggio(regione1:str, regione2:str):
    
    if(not regioneEsiste(regione1)):
        print("La prima regione inserita non esiste")
        return
    if(not regioneEsiste(regione2)):
        print("La prima regione inserita non esiste")
        return
    
    dizFail = {}
    compareString_1=regione1+regione2
    compareString_2=regione2+regione1
    rispostaUtente=""
    
    if (lista_adiacenza.get(compareString_1) == None or lista_adiacenza.get(compareString_2) == None):
        dizFail[1]=True
    else:
        dizFail[1]=False
        
    dizFail[2] = notRed(regione1)
    dizFail[3] = notRed(regione2)
               
    if(dizFail.get(1) == True and dizFail.get(2) == True and dizFail.get(3) == True):
        print("YES")
    else:
        print("NO")
        
    rispostaUtente=input("Digitare how per la spiegazione: ")
    if (rispostaUtente.lower()=="how"):
       print("passaggio("+regione1+","+regione2+") <=> adiacenza("+regione1+","+regione2+") and notRed("+regione1+") and notRed("+regione2+")")
       rispostaUtente=input("Digitare 'how i' specificando in i il numero dell'atomo per ulteriori informazioni: ")
       if(rispostaUtente.lower()=='how 1'):
           print("adiacenza("+regione1+","+regione2+") <=>",dizFail.get(1))
       else:
           if(rispostaUtente.lower()=='how 2'):
               print("notRed("+regione1+") <=> "+regione1+"_yellow or "+regione1+"_white or "+regione1+"_orange")
               rispostaUtente=input("Digitare 'how i' specificando in i il numero dell'atomo per ulteriori informazioni: ")
               if(rispostaUtente.lower()=="how 1"):
                   print(regione1+"_yellow <=> ",findColor(regione1+"_yellow"))
               else:
                   if(rispostaUtente=="how 2"):
                       print(regione1+"_white <=> ",findColor(regione1+"_white"))
                   else:
                       if(rispostaUtente=="how 3"):
                           print(regione1+"_orange <=> ",findColor(regione1+"_orange"))
                       else:
                           print("Errore di digitazione")
           else:
               if(rispostaUtente.lower()=='how 3'):
                   print("notRed("+regione2+") <=> "+regione2+"_yellow or "+regione2+"_white or "+regione2+"_orange")
                   rispostaUtente=input("Digitare 'how i' specificando in i il numero dell'atomo per ulteriori informazioni: ")
                   if(rispostaUtente.lower()=="how 1"):
                       print(regione2+"_yellow <=> ",findColor(regione2+"_yellow"))
                   else:
                       if(rispostaUtente=="how 2"):
                           print(regione2+"_white <=> ",findColor(regione2+"_white"))
                       else:
                           if(rispostaUtente=="how 3"):
                               print(regione2+"_orange <=> ",findColor(regione2+"_orange"))
                           else:
                               print("Errore di digitazione")
               else:
                   print("Errore di digitazione")
    else:
         print("Errore di digitazione")