from typing import Any

from django.db.models.query import QuerySet
from ninja import Field, Schema
from ninja.pagination import PaginationBase


class CustomPagination(PaginationBase):
    class Input(Schema):
        page: int = Field(1, ge=1)
        per_page: int = Field(10, ge=1, le=100)

    class Output(Schema):
        items: list
        page: int = Field(examples=[1])
        per_page: int = Field(examples=[10])
        total: int = Field(examples=[100])

    def paginate_queryset(
        self,
        queryset: QuerySet,
        pagination: Input,
        **params: Any,
    ) -> dict[str, Any]:
        start = (pagination.page - 1) * pagination.per_page
        end = start + pagination.per_page
        return {
            'items': queryset[start:end],
            'page': pagination.page,
            'per_page': pagination.per_page,
            'total': queryset.count(),
        }
