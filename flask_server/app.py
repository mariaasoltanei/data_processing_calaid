from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
app.config["MONGO_URI"] = uriMongodb
mongo = PyMongo(app)