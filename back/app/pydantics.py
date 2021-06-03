from typing import Optional

from pydantic import BaseModel


class PhrasePydantic(BaseModel):
    key: str
    message: str
    tags: Optional[list] = []


class PhraseUpdatePydantic(BaseModel):
    key: Optional[str]
    message: Optional[str]
    tags: Optional[list]
