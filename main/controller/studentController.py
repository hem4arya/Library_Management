from hashlib import file_digest
from flask import Blueprint, request
from main.services.studentServices import studentService
from datetime import datetime
# .

studentController = Blueprint("studentController", __name__)


@studentController.route("/student/signin", methods=["POST"])
def create_Student_Account():

    data = request.form
    file = request.files['identity_img']

    print(file)

    uniquefilename = str(datetime.now().timestamp()).replace(".", "")
    # for uniquq file name using date time  in epoch format
    print(uniquefilename)

    splitfile = file.filename.split(".")  # spliting extention and file name
    print(splitfile)
    ext = splitfile[len(splitfile)-1]

    path1 = f"student_id_image/{uniquefilename}.{ext}"  # getting new filname

    file.save(path1)
# doing same thing for challan image
    file1 = request.files['challan_img']
    print(file1)
    splitefile1 = file.filename.split(".")
    print(splitfile)
    ext1 = splitefile1[len(splitfile)-1]
    path2 = f"chalanImage/{uniquefilename}.{ext1}"
    file1.save(path2)

    return studentService.creatStdCard(data, path1, path2)


@studentController.route("/get_transaction/<smis>", methods=["POST"])
def getTransactions(smis):
    return studentService.getTransactions(smis)
