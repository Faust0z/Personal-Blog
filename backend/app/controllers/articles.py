from flask import Blueprint, jsonify
from backend.app.services.articles import get_articles

articles_bp = Blueprint("articles", __name__, url_prefix="/articles")

@articles_bp.get("/")
def list_articles():
    return jsonify(get_articles())
