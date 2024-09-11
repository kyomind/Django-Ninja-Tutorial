from ninja import Schema


class CreatePostRequest(Schema):
    title: str
    content: str
    user_id: int
