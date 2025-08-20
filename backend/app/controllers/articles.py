from flask import Blueprint, request
from marshmallow import ValidationError
from ..services.articles import get_articles_srv, create_article_srv, get_article_by_id_srv, delete_article_srv
from ..schemas import ArticleSchema, ArticleCreateSchema

articles_bp = Blueprint("articles", __name__, url_prefix="/articles")

@articles_bp.get("/")
def get_articles_endp():
    title = request.args.get("title")
    tags = request.args.get("tags")
    user = request.args.get("user")
    date = request.args.get("date")
    articles = get_articles_srv(title, tags, user, date)
    return ArticleSchema(many=True).dump(articles), 200


@articles_bp.get("/<int:art_id>")
def get_article_by_id_endp(art_id: int):
    article = get_article_by_id_srv(art_id)
    if article:
        return ArticleSchema().dump(article), 200
    else:
        return {"error": "Article not found"}, 404


@articles_bp.post("/")
def post_article_endp():
    if not request.is_json:
        return {"error": "Content-Type must be application/json"}, 415
    
    data = request.get_json()
    try:
        data = ArticleCreateSchema().load(data)
    except ValidationError as err:
        return {"errors": err.messages}, 400
    
    try:
        article = create_article_srv(data)
        if article:
            return ArticleSchema().dump(article), 201
    except Exception as e:
        return {"error": "Could not create article"}, 400


@articles_bp.delete("/<int:art_id>")
def delete_article_endp(art_id: int):
    success = delete_article_srv(art_id)
    if success:
        return {"message": f"Article {art_id} deleted"}, 200
    else:
        return {"message": f"Article {art_id} not found"}, 404
