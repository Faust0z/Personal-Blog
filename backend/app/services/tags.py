from backend.app.extensions import db
from backend.app.models import Tag

def get_tags_cont():
    stmt = db.select(Tag)
    tags = db.session().execute(stmt).scalars().all()
    return [tag.to_dict() for tag in tags]
