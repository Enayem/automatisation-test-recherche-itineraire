########################################################################################
#                                                                                      #
#Programe de génération d'une "TestSuite SMMV"                                         #
#Main                                                                                  #
#Auteur : Omar ENAYEH 11/2016                                                          #
# IXXI                                                                                 #
########################################################################################

import sys
import uuid
import csv
from datetime import *
import argparse
import os.path
import codecs
import requests
import pytz
import xml.etree.ElementTree as ET
app_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_root)
from Structure_TestSuite_SMMV import HeadGlobal, testSuiteHead, testSuiteBottom, BottomGlobal,   testStepHead, testStepBottom, assertionItiScript, testCaseHead, testCaseBottom
from proxy import proxies


parser = argparse.ArgumentParser(description="Cet outils permet de générer un fichier Yml et/ou un projet SoapUI à partir d'un fichier csv contenant des RI")
parser.add_argument('--soapUiProject', action='store_true', help='si présent le fichier xml du projet SoapUI sera généré')
parser.add_argument('--yml', action='store_true', help='si présent le fichier yml sera généré et pourra être utilisé sur http://appli-sv002028.info.ratp/itineraires/fr/ratp/pdc par exemple' )
parser.add_argument('--rvbServer', help='adresse du serveur smartMove (utilisé pour SoapUI)', required=True)
parser.add_argument('--csvPath', help='Chemin complet + nom du fichier csv en entrée', required=True)
parser.add_argument('--nomFichier', help='Nom du fichier en sortie par defaut Test_Multi_ri', default='Test_Multi_ri')
parser.add_argument('--prefixTestCase', help='Prefix à utiliser pour les cas de test SoapUI ou YML', default ='RI')
parser.add_argument('--dateRI', help='Si présent, la date des requêtes de RI(format AAAA-MM-DDTHH:mm:ss) ')

args= parser.parse_args()



rvb_url = args.rvbServer + "/SmartMovePort"

listProfil = ["rvbFaster","profil1","profil2","profil3","profil4","profil5","profi6","profil7","profil8","profil9","profil10"]

tz = pytz.timezone('Europe/Paris')
dateRI=datetime.now(tz)
if args.dateRI :
    dateRI = datetime.strptime(args.dateRI+"+0100", "%Y-%m-%dT%H:%M:%S%z")
    
print("")
print("La date de RI est ", dateRI.isoformat())
print("")

if(args.soapUiProject):
    nomFichierSortie =  args.nomFichier+".xml" 
    print("")
    print("")
    print("""########################################################################################""")
    print("""#Programe de génération d'une "TestSuite SMMV"                                         #""")
    print("""#Serveur smartMove cible : """, rvb_url)
    print("""#nomFichierSortie  : """,nomFichierSortie)
    print("""########################################################################################""")
    print("")
    print("")
    
    customProprieties={}
    
    
    with codecs.open(nomFichierSortie, 'w', 'utf8') as fichierSortie:
        fichierSortie.write (HeadGlobal.format(projectName = args.nomFichier, uuid1=uuid.uuid1(), uuid2=uuid.uuid1(), uuid3=uuid.uuid1()))
        fichierSortie.write (testSuiteHead.format(TestSuiteName = args.nomFichier, uuid1=uuid.uuid1()))
            
        for profilIndex in listProfil:
        
            print("""########################################################################################""")
            print("""#Test Case   : """,args.nomFichier + " " + profilIndex)
            fichierSortie.write (testCaseHead.format(TestSuiteName = args.nomFichier + " " + profilIndex, uuid2=uuid.uuid1()))
           

            #TODO Faire des tests d'encodage avant la génération
            with open(args.csvPath,  newline='', encoding='latin-1') as csvfile:
              CSVRI = csv.DictReader(csvfile, delimiter=';')
              cmpt = 1 
              CSVRI.fieldnames
              
              
              for ri in CSVRI:
                    print ("Création cas de test ",ri['AdressStart'] + " -- " + ri['AdressEnd'])
                    
                    #GeoCoding de adressStart et adressEnd 
                    #On vérifie que l'adresse n'a pas été déjà géocodée et enregistrée 
                    if "lat " + ri['AdressStart'].strip() not in customProprieties :
                        payload={'f':'g', 'key':'RATP12RHF592GJDRJGRDKGL52', 'profile':'ratp',  'free': ri['AdressStart'], 'Referer':'http://www.ratp.fr', 'ref':'1'}
                        adressStart_oym_geoCodeXml = requests.get('http://ratp-staging2.onyourmap.com/oym?', params=payload, proxies=proxies)
                        
                        if(adressStart_oym_geoCodeXml.status_code == requests.codes.ok and 
                        adressStart_oym_geoCodeXml.text [2:5] == "xml" ## Test si la réponse est de l'xml ( <?xml version="1.0" encoding="iso-8859-1" ?> )
                        ):
                            startLong = ET.fromstring(adressStart_oym_geoCodeXml.text).find('addresses').find('address').find('longitude').text
                            startLat = ET.fromstring(adressStart_oym_geoCodeXml.text).find('addresses').find('address').find('latitude').text

                            customProprieties["lat " + ri['AdressStart'].strip()] = startLat
                            customProprieties["long " + ri['AdressStart'].strip()] = startLong
                        else :
                            if(adressStart_oym_geoCodeXml.text [2:5] != "xml"):
                                print ( r"/!\ /!\ probleme de geoCoding sur l'adresse : ",ri['AdressStart'] )
                    
                    if "lat " + ri['AdressEnd'].strip() not in customProprieties :    
                        payload={'f':'g', 'key':'RATP12RHF592GJDRJGRDKGL52', 'profile':'ratp',  'free': ri['AdressEnd'], 'Referer':'http://www.ratp.fr', 'ref':'1'}
                        adressEnd_oym_geoCodeXml = requests.get('http://ratp-staging2.onyourmap.com/oym?', params=payload, proxies=proxies)
                        if(adressEnd_oym_geoCodeXml.status_code == requests.codes.ok and
                        adressEnd_oym_geoCodeXml.text [2:5] == "xml" ## Test si la réponse est de l'xml ( <?xml version="1.0" encoding="iso-8859-1" ?> )
                        ):
                            
                            EndLong = ET.fromstring(adressEnd_oym_geoCodeXml.text).find('addresses').find('address').find('longitude').text
                            EndLat = ET.fromstring(adressEnd_oym_geoCodeXml.text).find('addresses').find('address').find('latitude').text
                            
                            customProprieties["lat " + ri['AdressEnd'].strip()] = EndLat
                            customProprieties["long " + ri['AdressEnd'].strip()] = EndLong
                        else:
                            
                            if(adressEnd_oym_geoCodeXml.text [2:5] != "xml"):
                                print ( r"/!\ /!\ probleme de geoCoding sur l'adresse : ",ri['AdressEnd'] )
                    
                    
                        
                    fichierSortie.write (testStepHead.format(prefix = args.prefixTestCase, numTest=int(ri['Indice']), testName=ri['AdressStart'] + " -- " + ri['AdressEnd'], uuid1=uuid.uuid1(), uuid2=uuid.uuid1(), urlRvb=rvb_url))
                    fichierSortie.write ("""						<con:request>\n""")
                    fichierSortie.write ("""<![CDATA[<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:smar="http://smartmove.ixxi/">\\r\n""")
                    fichierSortie.write ("""  <soap:Header/>{}\n""".format(r"\r"))
                    fichierSortie.write ("""  <soap:Body>{}\n""".format(r"\r"))
                    fichierSortie.write ("""    <smar:getItinerary>{}\n""".format(r"\r"))
                    fichierSortie.write ("""         <startPoint type="address" latitude=${lat} longitude=${long}/>{r}\n""".format(lat = "{#TestCase#lat " + ri['AdressStart'].strip() +"}", long = "{#TestCase#long " + ri['AdressStart'].strip() +"}",r = r"\r"))
                    fichierSortie.write ("""         <endPoint type="address" latitude=${lat} longitude=${long}/>{r}\n""".format(lat = "{#TestCase#lat " + ri['AdressEnd'].strip() +"}", long = "{#TestCase#long " + ri['AdressEnd'].strip() +"}",r = r"\r"))
                    fichierSortie.write ("""         <time>{}</time>{}\n""".format(dateRI.isoformat() ,r"\r"))
                    fichierSortie.write ("""         <startFrom>{}</startFrom>{}\n""".format(ri['startFrom'],r"\r"))
                    fichierSortie.write ("""         <withTrafficEvents>{}</withTrafficEvents>{}\n""".format(ri['withTrafficEvents'],r"\r"))
                    fichierSortie.write ("""         <prefJourney>{profil}</prefJourney>{r}\n""".format(profil=profilIndex,r=r"\r"))
                    listPreferNetwork = ri['preferNetwork'].split()
                    for pnItem in listPreferNetwork:
                        fichierSortie.write ("""         <prefNetworks>{pn}</prefNetworks>{r}\n""".format(pn=pnItem,r=r"\r"))
                    fichierSortie.write ("""         <withMobility>false</withMobility>{}\n""".format(r"\r"))
                    fichierSortie.write ("""         <withDetails>true</withDetails>{}\n""".format(r"\r"))
                    fichierSortie.write ("""   </smar:getItinerary>{}\n""".format(r"\r"))
                    fichierSortie.write ("""  </soap:Body>{}\n""".format(r"\r"))
                    fichierSortie.write ("""</soap:Envelope>]]>\n""")
                    fichierSortie.write ("""						</con:request>\n""")
                    

                    
                    #Création de l'assertion pour vérifier l'itinéraire enmprunter 
                    fichierSortie.write(assertionItiScript.format( uuid1=uuid.uuid1()))
                    fichierSortie.write ("""<![CDATA[<res>\n""")
                    tabAssertion = ri['assertion1'].split(',')
                    i = 0
                    while (i +3 <= len(tabAssertion)):
                        modeAsser = tabAssertion[i]
                        lineAsser = tabAssertion[i+1]
                        origAsser = tabAssertion[i+2]
                        destAsser = tabAssertion[i+3]
                        i = i + 4
                        fichierSortie.write ("""  <segment>\n""")
                        fichierSortie.write ("""    <mode>{}</mode>\n""".format(modeAsser))
                        fichierSortie.write ("""    <line>{}</line>\n""".format(lineAsser))
                        fichierSortie.write ("""    <origine>{}</origine>\n""".format(origAsser))
                        fichierSortie.write ("""    <destination>{}</destination>\n""".format(destAsser))
                        fichierSortie.write ("""  </segment>\n""")
                    fichierSortie.write("""</res>]]>\n""")
                    fichierSortie.write("""                                </content>\n""")
                    fichierSortie.write("""                                <allowWildcards>false</allowWildcards>\n""")
                    fichierSortie.write("""                            </con:configuration>\n""")
                    fichierSortie.write("""                        </con:assertion>\n""")
                    fichierSortie.write (testStepBottom.format(uuid1=uuid.uuid1(), uuid2=uuid.uuid1()))
                        
                        
                    
                            
                    cmpt=cmpt+1

            fichierSortie.write ("""    <con:properties>\n""")
            for name, value in customProprieties.items() :
                fichierSortie.write ("""      <con:property>\n""")
                fichierSortie.write ("""         <con:name>{}</con:name>\n""".format(name))
                fichierSortie.write ("""         <con:value>"{}"</con:value>\n""".format(value))
                fichierSortie.write ("""      </con:property>\n""")
            fichierSortie.write ("""    </con:properties>\n""")
                
                            
            fichierSortie.write (testCaseBottom)
        fichierSortie.write (testSuiteBottom)
        fichierSortie.write (BottomGlobal)
    print("")
    print("# {} cas de test créés".format(cmpt - 1))
    print("""Fin de génération d'une "TestSuite SMMV" \n\n """)

#fi projet SoapUI

if(args.yml):
    nomFichierSortie =  args.nomFichier+".yml" 
    print("""########################################################################################""")
    print("""#Programe de génération d'un fichier YML pour loutils multi RI Ria                     #""")
    print("""#nomFichierSortie  : """,nomFichierSortie)
    print("""########################################################################################""")
    #, newline='\n'
    with codecs.open(nomFichierSortie, 'w', 'utf8') as fichierSortie:
        fichierSortie.write ("""# Exemple de fichier d'entrée de test de pondération
# Il faut respecter l'indentation (2 espaces, pas de tabulation !)
# Explication des champs :
#
# caseNumber : Numéro du cas de test
# line : Libellé du cas de test
# origin : Adresse de départ
# destination : Adresse d'arrivée
# itineraryCML : Itinéraire attendu par le calculateur.
#                Il s'agit de sections de transport en commun (marche à pied ignorée)
#                Chaque section contient les champs suivants :
#                    mode: Choix du réseau, exemple : "SNCF", "RER", "Bus RATP", "Tram"file:///C:/Users/X2014940/Downloads/itinerariesOutput(1).yml
#                    line: Nom de la ligne, exemple : A, B, H, 1, 256
#                    direction: Direction de la ligne, uniquement à titre informatif (non utilisé pour la comparaison)
#                    origin: Station de départ
#                    destination:  Station d'arrivée
# itineraryAlt (optionnel) : Itineraire alternatif permettant de valider la comparaison d'itinéraire
# mode (optionnel) : Mode de transport, choix possible : "all", "ferre_tram" ou "bus_tram"
# type (optionnel) : Type de route, choix possible : 1 (Le + rapide), 2 (- de corresp.) ou 3 (- de marche) \n""")
        fichierSortie.write ("""\n""")
        with open(args.csvPath,  newline='', encoding='latin-1') as csvfile:
            CSVRI = csv.DictReader(csvfile, delimiter=';')
            cmpt = 1 
            CSVRI.fieldnames
            
            for ri in CSVRI:
                print ("Création cas de test ",ri['AdressStart'] + " -- " + ri['AdressEnd'])
                fichierSortie.write ("""-\n""")
                fichierSortie.write ("""  caseNumber: {}\n""".format(ri['Indice']))
                fichierSortie.write ("""  line: "{testName}"\n""".format(testName=(ri['AdressStart']) + " -- " + ri['AdressEnd']))
                fichierSortie.write ("""  origin: "{origin}"\n""".format(origin=ri['AdressStart']))
                fichierSortie.write ("""  destination: "{destination}"\n""".format(destination=ri['AdressEnd']))
                fichierSortie.write ("""  itineraryCML:\n""")
                tabAssertion = ri['assertion1'].split(',')
                i = 0
                while (i +3 <= len(tabAssertion)):
                    res = tabAssertion[i]
                    numLigne = tabAssertion[i+1]
                    orig = tabAssertion[i+2]
                    dest = tabAssertion[i+3]
                    i = i + 4
                    fichierSortie.write ("""    - {a} mode: {r}, line: '{n}', origin: '{o}', destination: '{d}'{af}\n""".format(r = res, n = numLigne, o = orig, d = dest, a = '{', af = '}' ))
                
                if ri['assertion2']:
                    tabAssertion = ri['assertion2'].split(',')
                    fichierSortie.write ("""  itineraryALT:\n""")
                    i = 0
                    while (i +3 <= len(tabAssertion)):
                        res = tabAssertion[i]
                        numLigne = tabAssertion[i+1]
                        orig = tabAssertion[i+2]
                        dest = tabAssertion[i+3]
                        i = i + 4
                        fichierSortie.write ("""    - {a} mode: {r}, line: '{n}', origin: '{o}', destination: '{d}'{af}\n""".format(r = res, n = numLigne, o = orig, d = dest, a = '{', af = '}' ))
                if ri['assertion3']:
                    fichierSortie.write ("""  itineraryALT:\n""")
                    tabAssertion = ri['assertion3'].split(',')
                    i = 0
                    while (i +3 <= len(tabAssertion)):
                        res = tabAssertion[i]
                        numLigne = tabAssertion[i+1]
                        orig = tabAssertion[i+2]
                        dest = tabAssertion[i+3]
                        i = i + 4
                        fichierSortie.write ("""    - {a} mode: {r}, line: '{n}', origin: '{o}', destination: '{d}'{af}\n""".format(r = res, n = numLigne, o = orig, d = dest, a = '{', af = '}' ))
                
                
                if ri['assertion4']:
                    tabAssertion = ri['assertion4'].split(',')
                    fichierSortie.write ("""  itineraryALT:\n""")
                    i = 0
                    while (i +3 <= len(tabAssertion)):
                        res = tabAssertion[i]
                        numLigne = tabAssertion[i+1]
                        orig = tabAssertion[i+2]
                        dest = tabAssertion[i+3]
                        i = i + 4
                        fichierSortie.write ("""    - {a} mode: {r}, line: '{n}', origin: '{o}', destination: '{d}'{af}\n""".format(r = res, n = numLigne, o = orig, d = dest, a = '{', af = '}' ))
                
                
                if ri['assertion5']:
                    tabAssertion = ri['assertion5'].split(',')
                    fichierSortie.write ("""  itineraryALT:\n""")
                    i = 0
                    while (i +3 <= len(tabAssertion)):
                        res = tabAssertion[i]
                        numLigne = tabAssertion[i+1]
                        orig = tabAssertion[i+2]
                        dest = tabAssertion[i+3]
                        i = i + 4
                        fichierSortie.write ("""    - {a} mode: {r}, line: '{n}', origin: '{o}', destination: '{d}'{af}\n""".format(r = res, n = numLigne, o = orig, d = dest, a = '{', af = '}' ))
               
                    
                cmpt = cmpt +1
            print("")
            print("# {} cas de test créés".format(cmpt - 1))
            print("""Fin de génération d'un fichier YML pour loutils multi RI Ria """)
                
                
                

        
        
        
        
    