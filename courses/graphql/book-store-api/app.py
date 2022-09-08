"""
Source: https://vincenttechblog.com/building-web-api-with-python-flask-graphql-sqlalchemy-and-postgresql/
"""

import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


app = Flask(__name__)
app.debug = True

## Configs
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

## Modules
db = SQLAlchemy(app)

## Database Conf
## SQLAlchemy Modules


## Models

## Schema Objects


## Routes
@app.route("/")
def index():
    """
    Route to https://what.ever/
    """
    return "Welcome to El Gato Escaldado Book Store API"


if __name__ == "__main__":
    app.run()
