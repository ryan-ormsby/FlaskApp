import shopify
import app
from config import * #get config variables

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME) #from config.py
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

def editorder(ordertoaddrisk):
    addrisk = shopify.OrderRisk({'order_id': ordertoaddrisk})
    addrisk.message = "This order was placed from a proxy IP"
    addrisk.recommendation = "cancel"
    addrisk.score = "1.0"
    addrisk.source = "External"
    addrisk.display = True
    addrisk.cause_cancel = True
    addrisk.save()
