from utils import generate_id
from flask import Flask, request, send_file, render_template
from pymongo import MongoClient


# Mongo class -> pip install pymongo
class Mongo:
    __mongo = MongoClient("mongodb://localhost:27017")
    __db = __mongo.StFiles
    __collection = __db.save

    def add(self, AddFile: str, AddAuthor: str):
        self.AddFile = AddFile
        self.AddAuthor = AddAuthor
        scheme = {
            "id": generate_id().generate_id(),
            "file": self.AddFile,
            "author": self.AddAuthor
        }
        self.__collection.insert_one(scheme)
        return scheme["id"]

    def find(self, FindID: str, FindAuthor: str):
        self.FindID = FindID
        self.FindAuthor = FindAuthor

        if result := self.__collection.find_one({"id": self.FindID, "author": self.FindAuthor}, {"_id": 0, "file": 1})["file"]:
            return result


class App:
    __app = Flask(__name__)

    @__app.route("/")
    def home():
        return render_template("index.html")

    @__app.route("/upload")
    def upload():
        return render_template("upload.html")

    @__app.route("/save", methods=["POST"])
    def save():
        get_file = request.files["file"]
        get_author = request.form.get("author")
        Mongo().add(f"./Files/{get_file.filename}", get_author)

        return Mongo().add(f"./Files/{get_file.filename}", get_author)

    @__app.route("/getfile/<id>/<author>")
    def getfile(id, author):
        return send_file(Mongo().find(id, author), as_attachment=True)
    
    __app.run()

if __name__ == "__main__":
    App()
