#register webhook
import shopify, app, json, requests
import urllib3
urllib3.disable_warnings()
from config import * #get config variables

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME) #from config.py
whurl = shop_url + "/webhooks.json"

with open('webhook.json') as json_data:
    d = json.load(json_data)

print(whurl)
print(d)

regwh = requests.post(whurl, json=d)
print(regwh.status_code)
