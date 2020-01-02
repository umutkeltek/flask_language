import pymongo as PyMongo
from pymongo import mongo_client, MongoClient
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from LanguageClass import a,b,c

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/language_db"
app.config['MONGO_DBNAME'] = 'language_db'
mongo = PyMongo(app)
client = MongoClient()
db = client['language_db']
collection = db['languages']

collection.insert_one(c.make_dic())
collection.insert_one(b.make_dic())


# language1= {"language": "Türkçe",
#         "Add": "Eklemek",
#       "tags":
# client = MongoClient()
# client = MongoClient('localhost', 27017)
# db = client['language_db'] # or db = client.test_database
# collection = db['languages']

@app.route("/language/all", methods=["GET"])
def show_all():
    output = []
    for lng in collection.find():
        output.append({'name': lng["name"], 'add': lng["add"], 'delete': lng["delete"], 'edit': lng["edit"]}) #'_id': lng.id.str
    return jsonify({"result": output})


@app.route("/language/<name>", methods=["GET"])
def get_one_language(name):
    lng = collection.find_one({"name": name})
    output = {'name': lng["name"], 'add': lng["add"], 'delete': lng["delete"], 'edit': lng["edit"]}
    return jsonify({"result": output})

@app.route("/language/all", methods=["POST"])
def add_language():
    name = request.json["name"]
    add = request.json["add"]
    delete = request.json["delete"]
    edit = request.json["edit"]
    collection.insert({"name": name, "add":add, "delete":delete, "edit":edit})
    return "Your entity has been add successfully"

@app.route("/language/delete/<string:id>")  # dinamik url
def delete(id):
    return "Deleted" + id


if __name__ == "__main__":
    app.run(debug=True)
