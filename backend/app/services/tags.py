from ..extensions import db
from ..models import Tag

def get_tags_cont():
    stmt = db.select(Tag)
    tags = db.session.execute(stmt).scalars().all()
    return tags
