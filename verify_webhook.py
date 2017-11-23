#verify webhook

import hashlib, base64, hmac, json, settings

def shopify_webhook(f):

  def _hmac_is_valid(body, secret, hmac_to_verify):
    hash            = hmac.new(secret, body, hashlib.sha256)
    hmac_calculated = base64.b64encode(hash.digest())
    return hmac_calculated == hmac_to_verify

  @wraps(f)
  def wrapper(request, *args, **kwargs):
    # Try to get required headers and decode the body of the request.
    try:
      webhook_topic = request.META['HTTP_X_SHOPIFY_TOPIC']
      webhook_hmac  = request.META['HTTP_X_SHOPIFY_HMAC_SHA256']
      webhook_data  = json.loads(request.body)
    except:
      return HttpResponseBadRequest()

    # Verify the HMAC.
    if not _hmac_is_valid(request.body, settings.SHOPIFY_API_SECRET, webhook_hmac):
      return HttpResponseForbidden()

    # Otherwise, set properties on the request object and return.
    request.webhook_topic = webhook_topic
    request.webhook_data  = webhook_data
    return f(request, args, kwargs)

  return wrapper


import shopify

shopify.Session.setup(api_key=api_key, secret=api_secret)

session = shopify.Session(
    myshopify_domain,
    access_token,
)

shopify.ShopifyResource.activate_session(session)
for webhook in shopify.Webhook.find():
    print webhook.to_dict()
