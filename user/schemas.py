import re

from ninja import Field, Schema
from pydantic import field_validator


class CreateUserRequest(Schema):
    username: str = Field(examples=['Alice'])
    email: str = Field(examples=['alice@example.com'])
    password: str = Field(min_length=8, examples=['password123'])
    bio: str | None = Field(default=None, examples=['Hello, I am Alice.'])

    @field_validator('password')
    @classmethod
    def validate_password_contains_number(cls, v: str) -> str:
        """
        驗證密碼至少包含一個數字
        """
        if not re.search(r'\d', v):
            raise ValueError('密碼必須包含至少一個數字')
        return v
