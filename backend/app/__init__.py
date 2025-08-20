from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from .config.settings import DB_URI
from . import models
from .controllers.articles import articles_bp
from .controllers.tags import tags_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Create the tables here to make sure Flask is initiated
    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db)

    app.register_blueprint(articles_bp)
    app.register_blueprint(tags_bp)

    @app.route("/")
    def index():
        return "<h1>Hi!</h1>"

    return app