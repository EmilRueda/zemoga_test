from pydantic import BaseModel
from pydantic import Field

from fastapi import Request

# Models

## Users
class User(BaseModel):
    idportfolio: int = Field(
        ...,
    )
    description: str = Field(
        ...,
        min_lenght=20,
        max_lenght=255
    )
    experience_summary: str = Field(
        ...,
        min_lenght=20,
        max_lenght=255
    )
    id: int = Field(
        ...,
    )
    image_url: str = Field(
        ...,
        min_lenght=2,
        max_lenght=255
    )
    last_names: str = Field(
        ...,
        min_lenght=2,
        max_lenght=50,
    )
    names: str = Field(
        ...,
        min_lenght=2,
        max_lenght=30,
    )
    tittle: str = Field(
        ...,
        min_lenght=2,
        max_lenght=150
    )
    twitter_user_id: str = Field(
        ...,
        min_lenght=2,
        max_lenght=150
    )
    twitter_user_name: str = Field(
        ...,
        min_lenght=2,
        max_lenght=150
    )
    user_id: str = Field(
        ...,
        min_lenght=2,
        max_lenght=20
    )


## Login form
class LoginForm():
    def __init__(self, request: Request):
        self.request: Request = request
        self.user_id: str = Field(
            ...,
            min_lenght=2,
            max_lenght=20
        )
    async def load_data(self):
        form = await self.request.form()
        self.user_id = form.get("user_id")
