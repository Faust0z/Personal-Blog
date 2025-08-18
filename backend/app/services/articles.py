from backend.app.extensions import db
from backend.app.models import Article

def get_articles_srv():
    stmt = db.select(Article)
    articles = db.session.execute(stmt).scalars().all()
    return [art.to_dict() for art in articles]


def get_article_by_id_srv(art_id: int):
    article = db.session.get(Article, art_id)
    return article.to_dict()


def create_article_srv(data: dict):
    article: Article = Article(**data)
    if article:
        db.session().add(article)
        db.session().commit()
        return True
    return False


def delete_article_srv(art_id: int):
    article = db.session.get(Article, art_id)
    if article:
        db.session().delete(article)
        db.session.commit()
