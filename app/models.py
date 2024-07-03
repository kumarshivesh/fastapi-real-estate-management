from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Locality(Base):
    __tablename__ = "localities"

    locality_id = Column(Integer, primary_key=True, index=True)
    locality_name = Column(String, unique=True, index=True)

class Property(Base):
    __tablename__ = "properties"

    property_id = Column(Integer, primary_key=True, index=True)
    property_name = Column(String, index=True)
    locality_id = Column(Integer, ForeignKey('localities.locality_id'))
    owner_name = Column(String)

    locality = relationship("Locality")
