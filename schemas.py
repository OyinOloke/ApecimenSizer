from pydantic import BaseModel

class SpecimenCreate(BaseModel):
    username: str
    specimen_size: float
    magnification: float

class SpecimenOut(BaseModel):
    id: int
    username: str
    specimen_size: float
    magnification: float
    actual_size: float
