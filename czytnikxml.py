import xml.etree.ElementTree as ET   
import sys
  
myroot=''  
def setXml(root,tree):  
    global myroot  
    global mytree  
    myroot=root  
    mytree=tree  
def readPrisoner():  
    global myroot  
    for osadzony in myroot.findall('osadzony'):  
        osadzonyId=osadzony.attrib['id']  
        imie=osadzony.find('imie').text
        nazwisko=osadzony.find('nazwisko').text
        plec=osadzony.find('plec').text  
        adres=osadzony.find('adres').text  
        zakladkarny=osadzony.find('zakladkarny').text
        pobyt=osadzony.find('pobyt').text  
        print(
        "  Imię: ",imie,"\n",
        " Nazwisko: ", nazwisko,"\n",
        " Płeć: ", plec, "\n",
        " Adres zamieszkania: ",adres,"\n",  
        " Miejsce odbywania kary: ",zakladkarny,"\n",
        " Id: ",osadzonyId, "\n",
        " Czas trwania kary: ", pobyt)  
        print("----------------------------")  
    input("Przyciśnij dowolny klawisz aby kontynuować...")      
def getId():  
    global myroot  
    temp = 0  
    for osadzony in myroot.findall('osadzony'):  
        id= int(osadzony.attrib['id'])  
        if id>temp:  
            temp=id  
    return temp+1       
def newPrisoner(ET):  
    global myroot  
    global mytree  
    print("Wprowadź nowego więźnia")  
    imie=input("Imie:")
    nazwisko=input("Nazwisko:")
    plec=input("Płeć(M/K):")  
    adres=input("Adres:")  
    zakladkarny=input("Miejsce odbywania kary:")
    pobyt=input("Czas odbywania kary:")          
    nextId=getId()  
    newrecord = ET.SubElement(myroot, "osadzony",id=str(nextId))  
    ET.SubElement(newrecord, "imie", name="imie").text = imie
    ET.SubElement(newrecord, "nazwisko", name="nazwisko").text = nazwisko
    ET.SubElement(newrecord, "plec", name="plec").text = plec
    ET.SubElement(newrecord, "adres", name="adres").text = adres  
    ET.SubElement(newrecord, "zakladkarny", name="zakladkarny").text = zakladkarny
    ET.SubElement(newrecord, "pobyt", name="pobyt").text = pobyt  
    mytree.write("Wiezienie.xml")    
    print("Wprowadzono więźnia...")  
def deletePrisoner():  
    global myroot  
    global mytree  
    deleteRecord=int(input("Wprowadź numer ID więźnia którego chcesz usunąć: "))  
    for osadzony in myroot.findall('osadzony'):  
        delid= int(osadzony.attrib['id'])  
        if delid == deleteRecord:  
            myroot.remove(osadzony)              
            mytree.write("Wiezienie.xml")  
            print("Usunięto więźnia...")      
def updatePrisoner():  
    global myroot  
    global mytree  
    updateRecord=int(input("Wprowadź ID kontaktu który chcesz zaktualizować: "))  
    for osadzony in myroot.findall('osadzony'):  
        upid= int(osadzony.attrib['id'])  
        if upid == updateRecord:  
            imie = osadzony.find('imie').text
            nazwisko=osadzony.find('nazwisko').text
            plec=osadzony.find('plec').text
            adres = osadzony.find('adres').text  
            zakladkarny = osadzony.find('zakladkarny').text  
            imie=osadzony.find('imie').text
            pobyt=osadzony.find('pobyt').text
            imie = input("Wprowadź imię:") or imie  
            osadzony.find('imie').text= imie
            nazwisko = input("Wprowadź nazwisko:") or nazwisko
            nazwisko.find('nazwisko').text= nazwisko
            plec = input("Wprowadź płeć(M/K):") or plec  
            osadzony.find('plec').text= plec  
            adres = input("Wprowadź adres:") or adres  
            osadzony.find('adres').text= adres  
            zakladkarny = input("Wprowadź miejsce osadzenia:") or zakladkarny  
            osadzony.find('zakladkarny').text= zakladkarny  
            pobyt = input("Wprowadź czas pobytu:") or pobyt
            pobyt.find('pobyt').text= pobyt
            mytree.write("Wiezienie.xml")  
            print("Więźień zaktualizowany...") 

try:  
    mytree = ET.parse('Wiezienie.xml') 
    myroot = mytree.getroot()  
    choice=int(input(' Co chcesz zrobić?\n 1.Lista więźniów\n 2.Nowy więźeń \n 3.Aktualizacja więźnia \n 4.Usunięcie więźnia \n'))  
    setXml(myroot,mytree)  
    newPrisoner(ET) if choice ==2 else ""  
    updatePrisoner() if choice ==3 else ""     
    deletePrisoner() if choice ==4 else ""  
    readPrisoner() if choice ==1 else ""     
except OSError as err:  
    print("OS error: {0}".format(err))  
except:  
    print("Unexpected error:", sys.exc_info()[0])  
    raise  
