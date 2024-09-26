import re
from typing import Self

from ninja import Field, Schema
from ninja.errors import HttpError
from pydantic import field_validator, model_validator


class CreateUserRequest(Schema):
    username: str = Field(examples=['Alice'])
    email: str = Field(examples=['alice@example.com'])
    password: str = Field(min_length=8, examples=['password123'])
    confirm_password: str = Field(min_length=8, examples=['password123'])
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

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        if self.password != self.confirm_password:
            raise HttpError(400, '密碼和確認密碼必須相同')
        return self
