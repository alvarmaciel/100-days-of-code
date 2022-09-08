from flask import Flask

app = Flask(__name__)
app.debug = True

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
