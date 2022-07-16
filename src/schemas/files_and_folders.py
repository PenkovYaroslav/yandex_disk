from pydantic import BaseModel, validator
from typing import Literal


class CreateFolder(BaseModel):
    href: str
    method: Literal["GET"]
    templated: bool

    @validator('href')
    def check_href(cls, href):
        if 'https:' in href:
            return href
        else:
            raise ValueError("href doesn't contain https:")
