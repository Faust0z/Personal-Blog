from backend.app.extensions import db

articles_have_tags = db.Table(
    "article_tag",
    db.Column("article_id", db.ForeignKey("articles.id"), primary_key=True),
    db.Column("tag_id", db.ForeignKey("tags.id"), primary_key=True)
)
