from datetime import datetime
from typing import Self

from ninja import Field, FilterSchema, Schema
from pydantic import model_validator
from django.core.exceptions import ValidationError

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
    start_date: str | None = Field(None, q='created_at__gte')
    end_date: str | None = Field(None, q='created_at__lte')

    @model_validator(mode='after')
    def check_date_range(self) -> Self:
        # 如果開始日期和結束日期都是 None，則不進行任何檢查
        if self.start_date is None and self.end_date is None:
            return self

        if not all([self.start_date, self.end_date]):
            raise ValidationError('開始日期和結束日期必須同時提供或同時不提供')

        # 顯式告訴 Mypy 這兩個變數在這裡是非 None 的
        assert self.start_date is not None
        assert self.end_date is not None

        try:
            start_date_dt = datetime.strptime(self.start_date, '%Y-%m-%d')
            end_date_dt = datetime.strptime(self.end_date, '%Y-%m-%d')
        except ValueError:
            raise ValidationError('日期格式無效，應為 YYYY-MM-DD')

        if start_date_dt > end_date_dt:
            raise ValidationError('開始日期必須早於結束日期')

        return self
