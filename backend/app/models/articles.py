from backend.app.__init__ import db

class Person(db.Model):
    __tablename__ = "Articles"
    pid = db.Column(db.Ingeger, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)

