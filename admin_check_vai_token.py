from flask import Flask, request, jsonify, make_response
import jwt
import requests
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = "rahees_secret_key"


def token_required(func):
    @wraps(func)
    def decorated(*args,**kwargs):
        # token = request.args.get("token") #feteching token from params
        token = request.headers.get("token")   #fetching token from headers
        print("printting inside decorator ",token)

        if not token:
            return jsonify({"meassage":"Token is missing"}),403
        try:
            data = jwt.decode(token,app.config["SECRET_KEY"])
        except:
            return jsonify({"message":"Token is invalid"})

        return func(*args,**kwargs)
    return decorated



def pass_token_in_headers(original_fun):
    @wraps(original_fun)
    def decorated_headers(*args, **kwargs):
        token =None

        if "token" in request.headers:
            token = request.headers["token"]
        if not token:
            return jsonify({"message":"Token is missing! "}),401

        try:
            current_user = jwt.decode(token,app.config["SECRET_KEY"])
            # if current_user.get("Admin") == True:
            #     print("Aaj to kaam ho he gya hai")
            # current_user = User.query.filter_by(public_id=data["public_id"]).first()
        except:
            return jsonify({"message":"Token is invalid! "}),401
        return original_fun(current_user, *args, **kwargs)
    return decorated_headers



@app.route("/login",methods=['POST'])
def login():
    usr_cred = request.get_data()
    # print("encoded values are ",type(usr_cred.decode("UTF-8")))
    user = request.get_json()
    
    # user_pass = request.get_json("user_pass")
    user_name = user["user_name"]
    user_pass = user["user_pass"]
    admin_status = user["admin"]
    print("user_name = ",user_name," user_pass = ",user_pass)
    if user_name and user_pass:
        token = jwt.encode({"user_name":user_name,
        "user_pass":user_pass,
        "admin":admin_status,
        "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=2)},app.config["SECRET_KEY"])
        print("token ",token)
    return jsonify({"token":token.decode("UTF-8")})


@app.route("/unprotected")
def unprotected():
    return jsonify({"messsage":"This is a unprotected route anybody can access"})


@app.route("/protected")
@token_required
@pass_token_in_headers
def protected(current_user):
    print("value of current user = ",current_user)
    if current_user.get("admin") == True:
        status = requests.get(url="http://127.0.0.1:5001/second_route")
        print("Congrat's you are a Admin level person you can acccess the route ")
        return "Congrat's you are a Admin level person you can acccess the route"
    else:
        print("Sorry you can't access this route only ADMIN can ")
        return "Sorry you can't access this route only ADMIN can"

    return jsonify({"messsage":"This is a protected route only authenticated person can access"})

if __name__ == "__main__":
    app.run(debug=True)