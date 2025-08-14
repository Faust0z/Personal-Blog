from backend.app.extensions import db
from backend.app.models.associations import articles_have_tags
from datetime import datetime

class Tag(db.Model):
    __tablename__ = "tags"
    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str] = db.mapped_column(db.String, nullable=False)
    date_created: db.Mapped[datetime] = db.mapped_column(db.DateTime, default=datetime.now, )

    articles: db.Mapped[list["Article"]] = db.relationship(secondary=articles_have_tags, back_populates="tags")

    def __repr__(self):
        return f"<Article id={self.id} name={self.name}>"

    def to_dict(self) -> dict:
        return {
            "ID": self.id,
            "Name": self.name,
            "Date Created": self.date_created
        }