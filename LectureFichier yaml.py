import yaml
import codecs

with codecs.open(r"C:\Users\X2014940\Documents\IXXI\RI de ref\Session SSA 29112016\itinerariesOutput rvb02 profils.xml.Con365.Walk1.5.yml", 'r', 'utf8') as fichierYaml:
    resultatRi = yaml.load(fichierYaml)
    print(resultatRi[0]['itinerarySmartMove'][0]['mode'])

    for ri in resultatRi :
        print (ri['caseNumber'], end=" : ")
        print (ri['result'])
