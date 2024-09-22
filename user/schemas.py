from ninja import Field, Schema


class CreateUserRequest(Schema):
    username: str = Field(examples=['Alice'])
    email: str = Field(examples=['alice@example.com'])
    password: str = Field(examples=['password123'])
    bio: str | None = Field(default=None, examples=['Hello, I am Alice.'])
