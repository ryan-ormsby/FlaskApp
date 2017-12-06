import shopify, json, app, requests
import urllib3
urllib3.disable_warnings()
#from flask import request
from config import * #get config variables

def addcharge():
    shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME) #from config.py
    regurl = shop_url + "/recurring_application_charges.json"

    with open('charge.json') as json_data:
        d = json.load(json_data)

    print(regurl)
    print(d)

    regcharge = requests.post(regurl, json=d)
    response_json = regcharge.json()
    conurl = response_json['recurring_application_charge']['confirmation_url']

    print(regcharge.status_code)
    print(conurl)

    return conurl
