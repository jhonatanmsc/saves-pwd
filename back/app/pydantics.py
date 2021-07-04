from typing import List

from pydantic import BaseModel


class PhrasePydantic(BaseModel):
    title: str
    secrets: List[dict]
