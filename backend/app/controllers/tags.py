from flask import Blueprint
from ..services.tags import get_tags_cont
from ..schemas import TagSchema


tags_bp = Blueprint("tags", __name__, url_prefix="/tags")


@tags_bp.get("/")
def get_tags_endp():
    tags = get_tags_cont()
    return TagSchema(many=True).dump(tags), 200