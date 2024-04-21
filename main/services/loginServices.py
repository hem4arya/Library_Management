from .. import mysql
from datetime import datetime, timedelta
import jwt


from flask import make_response


class loginServices():

    def librarianLoginService(data):

        cur = mysql.connection.cursor()
        cur.execute(
            f"SELECT id, name ,username FROM librarian WHERE username = '{data['username']}' and password = '{data['password']}'")
        result = cur.fetchall()
        librariandata = result[0]
        print(librariandata)

        exp_time = datetime.now() + timedelta(minutes=15)
        epoc_time = int(exp_time.timestamp())
        payload = {
            "payload": librariandata,
            "exp": epoc_time
        }
        jwtoken = jwt.encode(payload, "sarthak", algorithm="HS256")

        return make_response({"jwtoken": jwtoken}, 200)

    def studentlogin(data):
        cur = mysql.connection.cursor()
        cur.execute(
            f"SELECT id,approval FROM student WHERE sima = '{data['sima']}'")

        result = cur.fetchall()
        result = result[0]
        value = result['approval']
        if value == 'approved':
            return "logdin"
        if value == 'pending':
            return make_response({"message": "your request is pending "}, )
        else:
            return make_response({"message": "your request is denied tyr to fill form again"}, 404)
