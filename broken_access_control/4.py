from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

@app.route("/deneme", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    if username=="user" and password=="1234":
        id = "pseudo123"
        #encoded_jwt = jwt.encode({"username": username, "id": id}, "pseudosecret", algorithm="HS256")
        encoded_jwt = jwt.encode({"username": username, "id": id}, "pseudosecret", algorithm=None)
        return jsonify({"data":encoded_jwt})
    else:
        return "error"
    
@app.route("/settings", methods=["GET"])    
def settings():
    pass

# jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])