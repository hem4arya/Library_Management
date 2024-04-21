from .. import mysql
import json
from flask_mysqldb import MySQLdb
from flask import make_response


class librarianService():

    def create(data):
        print(type(data))
        try:
            if data['username'] and data['password'] and data['name']:

                cur = mysql.connection.cursor()
                # if data['college_pic']:

                #     cur.execute(
                #         f"INSERT INTO librarian(username,password,name, college_pic)VALUES('{data['username']}','{data['password']}','{data['name']}', '{data['college_pic']}')")
                # else:
                print(data)
                cur.execute(
                    f"INSERT INTO librarian(username,password,name)VALUES('{data['username']}','{data['password']}','{data['name']}')")
                mysql.connection.commit()
                return "librarian created"
        except:
            return False

    def getalllibrarian(id):

        cur = mysql.connection.cursor()
        cur.execute(
            f"SELECT id,username,password,name FROM librarian WHERE id='{id}'")
        result = cur.fetchall()
        mysql.connection.commit()
        print(result)
        return json.dumps(result)

    def add_Book(librarian_id, data):
        if data['book_barcode_no']:
            if data['book_name']:
                cur = mysql.connection.cursor()
                try:
                    cur.execute(
                        f"INSERT into books(book_barcode_no, book_name, librarian_id) values({data['book_barcode_no']}, '{data['book_name']}', {librarian_id});")
                    mysql.connection.commit()
                    return "Book Added Succesfully"
                except MySQLdb.IntegrityError:
                    return "Duplicate Entry for book"

    def get_all_books(id):
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * from books where librarian_id = {id}")

        result = cur.fetchall()
        mysql.connection.commit()
        print(result)
        return json.dumps(result)

    def search_book_by_input(book_info):
        cur = mysql.connection.cursor()
        try:
            book_info = int(book_info)
            print("converted to integer ", book_info)
            cur.execute(
                f'''SELECT * from books where book_barcode_no ={book_info};''')

        except:
            print("not converted to integer ", book_info)
            cur.execute(
                f'''SELECT * from books where MATCH(book_name) AGAINST ("{book_info}");''')

        result = cur.fetchall()
        mysql.connection.commit()
        print(result)
        return json.dumps(result)

    def getPendingStudents():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM student WHERE approval = 'pending'")
        result = cur.fetchall()
        mysql.connection.commit()

        return json.dumps(result)

    def handelRequest(data, id):

        cur = mysql.connection.cursor()
        cur.execute(
            f"UPDATE student SET approval = '{data}' WHERE id = '{id}'")
        mysql.connection.commit()
        return " status has been changed "

    def issuebook(librarian_id, data, date):
        cur = mysql.connection.cursor()
        cur.execute(
            f"INSERT INTO booktransactions(simsid,bookcode,librarianid,issuedate,status)VALUES ('{data['simsid']}','{data['bookcode']}','{librarian_id}','{date}','issued') ")

        cur.execute(
            f"SELECT sima, approval FROM student WHERE sima = '{data['simsid']}'")
        result = cur.fetchall()
        result = result[0]
        approval = result["approval"]
        if approval == 'rejected':
            return make_response({"message": "STUDENT NOT FOUND "}, 404)
        if approval == 'pending':
            return make_response({"message": "STUDENT REQUEST IS PENDING CAN'T ISSUE BOOK"})
        else:
            if cur.rowcount > 0:
                cur.execute(
                    f"SELECT status FROM books WHERE book_barcode_no = '{data['bookcode']}' ")
                result = cur.fetchall()
                result = result[0]
                status = result["status"]
                if status == 'available':

                    cur.execute(
                        f"UPDATE books SET status = 'issued' WHERE book_barcode_no = '{data['bookcode']}'")
                    mysql.connection.commit()
                    return "BOOK IS ISSUED"
                else:
                    return make_response({"message": "BOOK IS ALREADY ISSUED"}, 404)

            else:
                return make_response({"message": "STUDENT NOT FOUND "}, 404)

    def receivebook(simsid, bookcode, Bookdate):
        cur = mysql .connection .cursor()
        cur.execute(
            f"UPDATE booktransactions SET receivedate ='{Bookdate}',status = 'received' WHERE bookcode = {bookcode} AND simsid = {simsid}")
        if cur.rowcount < 0:

            cur.execute(
                f"UPDATE books SET status = 'available' WHERE book_barcode_no = {bookcode}")
            mysql.connection.commit()
            return "working "
        else:
            return make_response({"message": "message"}, 404)
