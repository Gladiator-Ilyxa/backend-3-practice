from pydantic import BaseModel

class MasterOut(BaseModel):
    id: int
    name: str
    specialization: str

    class Config:
        from_attributes = True  # для Pydantic v2 / SQLAlchemy