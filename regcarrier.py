#regcarrier.py
import shopify, json, app, requests
import urllib3
urllib3.disable_warnings()
#from flask import request
from config import * #get config variables

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME) #from config.py
csurl = shop_url + "/carrier_services.json"

with open('carrier_service.json') as json_data:
    d = json.load(json_data)

print(csurl)
print(d)

regcarrier = requests.post(csurl, json=d)
#print(regcarrier.text)
print(regcarrier.status_code)

#print(regcarrier.response)
