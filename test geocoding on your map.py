#test geocoding on you map 

import requests
import xml.etree.ElementTree as ET


proxies = {
    "http": "http://x2014940:yCJJyA8E@proxy.reseau.ratp:80",
}
adress = "Charles - Michel (METRO)"
payload={'f':'g', 'key':'RATP12RHF592GJDRJGRDKGL52', 'profile':'ratp',  'free': adress, 'Referer':'http://www.ratp.fr', 'ref':'1'}
r = requests.get('http://ratp-staging2.onyourmap.com/oym?', params=payload, proxies=proxies)
print(r.text)

geocodingXml = ET.fromstring(r.text)

longitude = geocodingXml.find('addresses').find('address').find('longitude').text
latitude = geocodingXml.find('addresses').find('address').find('latitude').text
print (longitude, latitude)
