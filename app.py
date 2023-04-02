from flask import Flask,jsonify,request
from flask_cors import CORS
from MongoClient import MongoConnector


app=Flask(__name__)
CORS(app)
mongoDB=MongoConnector()

@app.route("/")
def hello():
    return jsonify({"Msg":"Hello"})

@app.route("/get_available_students",methods=["GET"])
def get_available_students():
    res=mongoDB.get_available_students()
    return jsonify({"Data":res})

@app.route("/get_my_students",methods=["GET"])
def get_my_students():
    MentorID=request.args.get("MentorID")
    res=mongoDB.get_my_students(MentorID)
    return jsonify({"Data":res})

@app.route("/get_all_students",methods=["GET"])
def get_all_students():
    res=mongoDB.get_all_students()
    return jsonify({"Data":res})

@app.route("/save_students",methods=["POST"])
def save_students():
    mid=request.json["MentorId"]
    slist=request.json["StudentList"]
    print(mid,slist)
    mongoDB.save_students(mid,slist)
    
    return jsonify({"Data":"Saved"})

@app.route("/save_marks",methods=["POST"])
def save_marks():
    req=request.json
    mongoDB.save_marks(req["Uid"],req["Marks"])
    return jsonify({"Data":"Saved"})

@app.route("/submit_marks",methods=["POST"])
def submit_marks():
    req=request.json
    mongoDB.submit_marks(req["Uid"],req["Marks"])
    return jsonify({"Data":"Saved"})

if __name__=="__main__":
    app.run()