from ..extensions import db
from ..models import Article, Tag, User
from datetime import datetime

def get_articles_srv(title=None, tags=None, user=None, date=None):
    stmt = db.select(Article)

    if title:
        stmt = stmt.where(Article.title.ilike(f"%{title}%"))
    if user:
        stmt = stmt.join(Article.user).where(User.name == user)
    if date:
        try:
            dt = datetime.fromisoformat(date)
            stmt = stmt.where(db.func.date(Article.date_created) == dt.date())
        except ValueError:
            pass
    if tags:
        tag_list = [t.strip() for t in tags.split(",") if t.strip()]
        if tag_list:
            stmt = stmt.join(Article.tags).where(Tag.name.in_(tag_list))

    articles = db.session.execute(stmt).scalars().all()
    return articles


def get_article_by_id_srv(art_id: int):
    article = db.session.get(Article, art_id)
    return article


def create_article_srv(data: dict):
    tags_data = data.pop("tags", [])
    article = Article(**data)

    if tags_data:
        for t in tags_data:
            # Handle both dict and Tag objects safely
            if isinstance(t, dict):
                tag_name = t.get("name")
            elif isinstance(t, Tag):
                tag_name = t.name
            else:
                tag_name = str(t)
            
            if tag_name:
                tag = db.session.query(Tag).filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                article.tags.append(tag)

    db.session.add(article)
    db.session.commit()
    return article


def delete_article_srv(art_id: int) -> bool:
    article = db.session.get(Article, art_id)
    if article:
        db.session.delete(article)
        db.session.commit()
        return True
    return False

