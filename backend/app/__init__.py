from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.app.config.settings import DB_URI

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI

    db.init_app(app)

    @app.route("/")
    def index():
        return "<h1>Hi!</h1>"

    return app