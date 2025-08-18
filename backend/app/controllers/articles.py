from flask import Blueprint, jsonify, request
from backend.app.services.articles import get_articles_srv, create_article_srv, get_article_by_id_srv, delete_article_srv

articles_bp = Blueprint("articles", __name__, url_prefix="/articles")

@articles_bp.get("/")
def get_articles_endp():
    return jsonify(get_articles_srv()), 200


@articles_bp.get("/<int:id>")
def get_article_by_id_endp(art_id: int):
    article = get_article_by_id_srv(art_id)
    if not article:
        return jsonify(article), 200
    else:
        return jsonify({"error": "Article not found"}), 404


@articles_bp.post("/")
def post_article_endp():
    data = request.get_json()
    try:
        article = create_article_srv(data)
        return jsonify(article), 201
    except Exception as e:
        return jsonify({"error": "Could not create article"}), 400


@articles_bp.delete("/<int:id>")
def delete_article_endp(art_id: int):
    success = delete_article_srv(art_id)
    if success:
        return jsonify({f"message: Article {art_id} deleted"}), 201
    else:
        return jsonify({f"message: Article {art_id} not found"}), 201
