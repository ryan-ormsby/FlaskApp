import shopify
import app

API_KEY = '2bd540a2e9b438f56fc7ce0b53559f6b'
PASSWORD = 'f3a6d8439fc7dcaa9a96898ef77d1889'
SHOP_NAME = 'ryanink'

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

#order = shopify.Order()
#order.email = "ryantest@test.com"
#order.note = "python app test order"
#order.fulfillment_status = "fulfilled"
#order.send_receipt = True
#order.send_fulfillment_receipt = False
#order.line_items = [{"variant_id": 51710689299, "quantity": 1}]

#success = order.save()
#print success
#print order.attributes

# order = order.reload()
def editorder(ordertoaddrisk):
    addrisk = shopify.OrderRisk({'order_id': ordertoaddrisk})
    # addrisk.order_id = order.id
    addrisk.message = "This order was placed from a proxy IP"
    addrisk.recommendation = "cancel"
    addrisk.score = "1.0"
    addrisk.source = "External"
    # addrisk.merchant_message = "This order was placed from a proxy IP"
    addrisk.display = True
    addrisk.cause_cancel = True
    addrisk.save()
    print addrisk.errors.full_messages()
