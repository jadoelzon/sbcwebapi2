from flask import Flask
app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sbc'
app.config['MYSQL_DB'] = 'aimsdb3'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'