from ..extensions import db
from .associations import articles_have_tags
from datetime import datetime


class Article(db.Model):
    __tablename__ = "articles"
    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    title: db.Mapped[str] = db.mapped_column(db.String, nullable=False)
    content: db.Mapped[str] = db.mapped_column(db.String, nullable=False)
    date_created: db.Mapped[datetime] = db.mapped_column(db.DateTime, default=datetime.now, )
    user_id = db.mapped_column(db.ForeignKey("users.id"), nullable=False)

    user: db.Mapped["User"] = db.relationship(back_populates="articles")
    tags: db.Mapped[list["Tag"]] = db.relationship(secondary=articles_have_tags, back_populates="articles")

    def __repr__(self):
        return f"<Article id={self.id} title={self.title}>"
