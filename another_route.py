from flask import Flask, request, jsonify, make_response
import jwt
import requests
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_sercret_key"

@app.route("/second_route")
def second_route():
    print("token is feteched here ")
    return "Successfully called by another route"


if __name__ == "__main__":
    app.run(debug=True,port=5001)