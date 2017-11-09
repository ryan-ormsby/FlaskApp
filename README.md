# FlaskApp
Learning sample Python app using Flask and the ShopifyAPI

Run app with `FLASK_APP=app.py flask run`

Requires addrisk.db, you can use mine or generate one using `db_initialize.py`

Requires a `config.py` file including:
`API_KEY = 'yourkeyhere'
PASSWORD = 'yourpasswordhere'
SHOP_NAME = 'shopnamehere'`
 and if you want to use secure forms with WTF:
`WTF_CSRF_ENABLED = True
SECRET_KEY = 'your-key-here'`

These will changes once OAUTH2 is implemented.
