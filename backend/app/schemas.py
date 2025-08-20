from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .extensions import db
from .models import Article, Tag, User


class TagSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        sqla_session = db.session
        load_instance = True
        include_fk = True
        include_relationships = False


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        include_fk = True
        include_relationships = False


class ArticleSchema(SQLAlchemyAutoSchema):
    tags = fields.List(fields.Nested(lambda: TagSchema()))
    username = fields.Method("get_username")

    class Meta:
        model = Article
        sqla_session = db.session
        load_instance = True
        include_fk = True
        include_relationships = True
        exclude = ("user",)

    def get_username(self, obj):
        return obj.user.name if getattr(obj, "user", None) else None


class ArticleCreateSchema(SQLAlchemyAutoSchema):
    tags = fields.List(fields.Nested(lambda: TagSchema(only=("name",))))

    class Meta:
        model = Article
        sqla_session = db.session
        load_instance = False
        include_fk = True
        include_relationships = False
        fields = ("title", "content", "user_id", "tags")

    title = fields.String(required=True)
    content = fields.String(required=True)
    user_id = fields.Integer(required=True)


