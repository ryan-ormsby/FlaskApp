# FlaskApp
Run app with `FLASK_APP=app.py flask run`

Requires addrisk.db, you can use mine or generate one using `db_initialize.py`

Requires a 'config.py' file including:
'API_KEY, PASSWORD, SHOP_NAME'
 and if you want to use secure forms with WTF:
'WTF_CSRF_ENABLED = True
SECRET_KEY = 'your-key-here''
