"""
Source: 
"""
# Imports
import os

import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

basedir = os.path.abspath(os.path.dirname(__file__))

# initializing our app
app = Flask(__name__)
app.debug = True

# Configs
# Our database configurations will go here
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Modules
# SQLAlchemy will be initiated here
db = SQLAlchemy(app)

# Models
# Our relations will be setup here
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    books = db.relationship("Book", backref="author")

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"{self.id}"


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"{self.title} {self.description} {self.year} {self.author_id}"


# Schema Objects
# Our schema objects will go here
class BookObject(SQLAlchemyObjectType):
    class Meta:
        model = Book
        interfaces = (graphene.relay.Node,)


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_books = SQLAlchemyConnectionField(BookObject)
    all_users = SQLAlchemyConnectionField(UserObject)


schema = graphene.Schema(query=Query)
# Routes
# Our GraphQL route will go here
app.add_url_rule(
    "/graphql-api",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True  # for having the GraphiQL interface
    ),
)


@app.route("/")
def index():
    return "Welcome to Book Store Api"


if __name__ == "__main__":
    app.run()
