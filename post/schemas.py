from datetime import datetime

from ninja import Schema


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
