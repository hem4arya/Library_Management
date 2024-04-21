from flask import Blueprint, request, redirect, url_for
from main.services.librarianService import librarianService
from auth_middelware import tocken_required, token_decode
from jwt.exceptions import DecodeError
from datetime import datetime

librarianController = Blueprint("librarianController", __name__)


# not made college_pic upload api becoz of lack of knowledge on postman 'll create with html pages
@librarianController.route("/l_signup", methods=["POST"])
def createLibrarian():
    data = request.form
    output = librarianService.create(data=data)
    if output == False:
        return ("Check you Body Paramerters")
    print(output)
    return "Librarian Created"


# no need to enter LIBRARIAN ID '''''''Librarian will get infomation about  himself''''''
@librarianController.route("/get_l_info", methods=["GET"])
@tocken_required
def getAllLibrarian():
    id = token_decode()
    return librarianService.getalllibrarian(id=id)

# form-data format
# book_barcode_no = 1
# book_name = 'a'


@librarianController.route('/add_book', methods=['POST'])
@tocken_required
def add_Book():
    librarian_id = token_decode()
    data = request.form
    return librarianService.add_Book(librarian_id, data)

# Just login and visit the route with get method to get all the books under the current librarian


@librarianController.route('/get_all_books', methods=['GET'])
@tocken_required
def get_all_books():
    id = token_decode()
    return librarianService.get_all_books(id)


# This will search the book by the book_barcode_no or any KEYWORD in the book_name.
@librarianController.route('/search_book/<book_info>', methods=['GET'])
@tocken_required
def search_book_by_input(book_info):
    result = librarianService.search_book_by_input(book_info)
    return result


@librarianController.route('/get_student', methods=['GET'])
@tocken_required
def getStudent():
    return librarianService.getPendingStudents()


@librarianController.route('/s_request/<id>', methods=['POST'])
@tocken_required
def handel_request(id):
    data = request.form['approval']
    return librarianService.handelRequest(data, id)


@librarianController.route('/issue_book', methods=['POST'])
@tocken_required
def issuebook():
    librarian_id = token_decode()
    data = request.form
    date = datetime.now()
    date = date.strftime('%Y-%m-%d %H:%M:%S')

    print(date)

    return librarianService.issuebook(librarian_id, data, date)


@librarianController.route('/receive_book', methods=['PUT'])
@tocken_required
def receivebook():
    #librarian_id = token_decode()
    simsid = request.form['simsid']
    bookcode = request.form['bookcode']
    print(simsid)
    print(bookcode)
    receivedate = datetime.now()
    Bookdate = receivedate.strftime('%Y-%m-%d %H:%M:%S')
    print(Bookdate)

    return librarianService.receivebook(simsid, bookcode, Bookdate)
