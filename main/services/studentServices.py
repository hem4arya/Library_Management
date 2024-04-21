from .. import mysql
import json

# .


class studentService():

    def creatStdCard(data, path1, path2):

        cur = mysql.connection.cursor()
        cur.execute(
            f"INSERT INTO student(name,class,roll_no,sima,librarian_no,email_id,address,identity_img,challan_img,approval) VALUES('{data['name']}','{data['class']}','{data['roll_no']}','{data['sima']}','{data['librarian_no']}','{data['email_id']}','{data['address']}','{path1}','{path2}','pending') ")
        mysql.connection.commit()
        result = cur.fetchall()
        print(result)
        return ("student account created ")

    def getTransactions(smis):
        cur = mysql.connection.cursor()
        cur.execute(
            f"SELECT bookcode, issuedate FROM booktransactions WHERE simsid = {smis}")

        result = cur.fetchall()
        result = result[0]
        bookcode = result["bookcode"]
        issuedate = result["issuedate"]
        cur.execute(
            f"SELECT book_name FROM books WHERE book_barcode_no = {bookcode}")
        getbook = cur.fetchall()
        getbook = getbook[0]
        getbook = getbook["book_name"]

        print(getbook)

        return json.dumps(getbook)
