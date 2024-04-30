from flask import Flask, jsonify
from pymongo import MongoClient
import requests


def create_app():
    app = Flask(__name__)

    # Configura la connessione al database MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mars_weather']
    collection = db['weather_data']

    return app
