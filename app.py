
from flask_mysqldb import MySQL
from main.controller.librarianController import librarianController
from main.controller.loginController import loginController
from main.controller.studentController import studentController
from main import createdb


app = createdb()

app.register_blueprint(studentController)
app.register_blueprint(librarianController)
app.register_blueprint(loginController)
# db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# a
# app.config['MYSQL_DB'] = db['mysql_db']

#mysql = MySQL(app)


@app.route('/')
def index():
    # def llibraian_singup():
    #      if request.method =='POST':
    #           librarianDetails = request.form
    #           name = librarianDetails['adminName']
    #           password = librarianDetails['password']
    #           cur = mysql.connection.cursor()
    #           cur.execute("INSERT INTO librarian(username,password)VALUES(%s, %s)",(name, password))
    #           mysql.connection.commit()
    #           cur.close()
    #           return 'success'
    #      return render_template('index.html')
    return "Website Working"

    app.run(debug=True)
