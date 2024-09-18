from datetime import datetime

from ninja import Field, Schema

from post.models import Post


class CreatePostRequest(Schema):
    title: str
    content: str
    user_id: int


class _AuthorInfo(Schema):
    id: int
    username: str
    email: str


class PostResponse(Schema):
    id: int
    title: str
    content: str
    author: _AuthorInfo
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def resolve_created_at(obj: Post) -> str:
        return obj.created_at.strftime('%Y-%m-%dT%H:%M:%SZ')

    @staticmethod
    def resolve_updated_at(obj: Post) -> str:
        return obj.updated_at.strftime('%Y-%m-%dT%H:%M:%SZ')


class PostListResponse(Schema):
    id: int
    title: str
    created_at: datetime
    author_name: str = Field(alias="author.username")

    @staticmethod
    def resolve_created_at(obj: Post) -> str:
        return obj.created_at.strftime('%Y-%m-%dT%H:%M:%SZ')
