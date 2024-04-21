from flask_mysqldb import MySQL
from flask import Flask


mysql = MySQL()


def createdb():

    try:
        app = Flask(__name__)
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = '1234'
        app.config['MYSQL_DB'] = 'elibrary'
        app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
        app.autocommit = True

        print(" db is connected")
        mysql.init_app(app)
        return app
    except:
        print("database connection error")
