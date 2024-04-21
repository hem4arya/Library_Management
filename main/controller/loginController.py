from flask import Blueprint, request
from main.services.loginServices import loginServices

loginController = Blueprint("loginController", __name__)


@loginController.route("/l_login", methods=["POST"])
def librarian_login():

    data = request.form
    return loginServices.librarianLoginService(data)


@loginController.route("/s_login", methods=["POST"])
def student_login():

    data = request.form
    return loginServices.studentlogin(data)
