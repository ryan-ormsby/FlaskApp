#register webhook
import shopify, app, json
from config import * #get config variables

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME) #from config.py
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

def regwebhook():
    addwh = shopify.Webhook()
    addwh.topic = "orders/create"
    addwh.address = "https://shopifyapps.fwd.wf/webhook"
    addwh.format = "json"
    addwh.save()
    print addwh.id


#def create_order_webhook
      # create webhook for order creation if it doesn't exist
#      unless ShopifyAPI::Webhook.find(:all).any?
#        webhook = {
#          topic: 'orders/create',
#          address: "https://#{APP_URL}/giftbasket/webhook/order_create",
#          format: 'json'}
#
#        ShopifyAPI::Webhook.create(webhook)
#      end
#    end
