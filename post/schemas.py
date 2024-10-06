from datetime import datetime

from ninja import Field, FilterSchema, Schema

from post.models import Post


class CreatePostRequest(Schema):
    title: str
    content: str
    user_id: int


class _AuthorInfo(Schema):
    id: int = Field(examples=[1])
    username: str = Field(examples=['Alice'])
    email: str = Field(examples=['alice@exapmple.com'])


class PostResponse(Schema):
    id: int = Field(examples=[1])
    title: str = Field(examples=['Ninja is awesome!'])
    content: str = Field(examples=['This is my first post.'])
    author: _AuthorInfo
    created_at: datetime = Field(examples=['2021-01-01T00:00:00Z'])
    updated_at: datetime = Field(examples=['2021-01-01T00:00:00Z'])

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
    author_name: str = Field(alias='author.username')

    @staticmethod
    def resolve_created_at(obj: Post) -> str:
        return obj.created_at.strftime('%Y-%m-%dT%H:%M:%SZ')


class PostFilterSchema(FilterSchema):
    query: str | None = Field(
        None,
        q=['title__icontains', 'author__username__icontains'],
        min_length=2,
        max_length=10,
    )
