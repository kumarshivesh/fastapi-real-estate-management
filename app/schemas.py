from pydantic import BaseModel

class PropertyBase(BaseModel):
    property_name: str
    locality: str
    owner_name: str

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    property_id: int

    class Config:
        orm_mode = True

class Locality(BaseModel):
    locality_id: int
    locality_name: str

    class Config:
        orm_mode = True

class PropertyDelete(BaseModel):
    property_id: int
