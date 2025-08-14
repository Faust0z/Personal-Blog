from backend.app.extensions import db
from backend.app.models import Article

def get_articles():
    stmt = db.select(Article)
    articles = db.session.execute(stmt).scalars().all()
    return [art.to_dict() for art in articles]