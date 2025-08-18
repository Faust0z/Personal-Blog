from flask import Blueprint, jsonify
from backend.app.services.tags import get_tags_cont

tags_bp = Blueprint("tags", __name__, url_prefix="/tags")

@tags_bp.get("/")
def get_tags_endp():
    return jsonify(get_tags_cont()), 200