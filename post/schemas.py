from datetime import datetime

from ninja import Schema


class CreatePostRequest(Schema):
    title: str
    content: str
    user_id: int


class PostResponse(Schema):
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime
    updated_at: datetime
