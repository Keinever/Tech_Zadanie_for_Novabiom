from pydantic import BaseModel


class PutRow(BaseModel):
    id: int
    taxonname: str
    composition: str
    change_in_abundance: str
    frequency: str
    additive_type: str


class PostRow(BaseModel):
    taxonname: str
    composition: str
    change_in_abundance: str
    frequency: str
    additive_type: str
