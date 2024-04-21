import jwt
from main import mysql
from functools import wraps
from flask import request, make_response, redirect
from jwt.exceptions import DecodeError
# .


def tocken_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        import app
        #DIRECTLY PUT TOKEN IN [Authorization] Field NO NEED OF BEARER
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
            print(token)
        else:

            return make_response({"message": "Authentication Token is missing!",
                                  "data": None,
                                  "error": "Unauthorized"}, 401)

        ## USING TRY AND EXCEPT TO HANDLE THE ERRORS WHEN THERE IS INVALID OR EXPIRED SIGNATURE
        try:
            data = jwt.decode(token, "sarthak", algorithms=["HS256"])
        except DecodeError as e:
            print("Redirect to Signup Page")
            return(f"{e}")
        except jwt.exceptions.ExpiredSignatureError as e:
            print("Redirec to Signup Page")
            return(f"{e}")

        except e:
            return(f"{e}")

        librarianid = data['payload']['id']
        print(librarianid)

        cur = mysql.connection.cursor()
        cur.execute(
            f"SELECT id FROM librarian WHERE id='{librarianid}'")
        result = cur.fetchall()
        print(result)

        #changed this
        fetchlibID = (result[0])
        print(type(fetchlibID.get('id')))

        if librarianid == fetchlibID.get('id'):
            return f(* args, **kwargs)
        else:
            return make_response({"message": "INVALID_ROLE!"}, 404)
        ####### CHANGES END HERE  ##########
    return decorated
#made new function to deode the jwt token and retrive librarian_id
def token_decode():
    if "Authorization" in request.headers:
            token = request.headers["Authorization"] #### No need of split
            data = jwt.decode(token, "sarthak", algorithms=["HS256"])
            librarianid = data['payload']['id']
            print('Token Decoded\nId = ', librarianid)
            return librarianid
    else:
        return None
