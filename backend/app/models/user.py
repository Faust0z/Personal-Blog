from ..extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str] = db.mapped_column(db.String, nullable=False)
    date_created: db.Mapped[datetime] = db.mapped_column(db.DateTime, default=datetime.now, nullable=False)

    articles: db.Mapped[list["Article"]] = db.relationship(back_populates="user")

    def __repr__(self):
        return f"<User id={self.id} name={self.name}>"
