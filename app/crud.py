from sqlalchemy.orm import Session
from . import models, schemas

def get_locality_by_name(db: Session, locality_name: str):
    return db.query(models.Locality).filter(models.Locality.locality_name == locality_name).first()

def create_locality(db: Session, locality_name: str):
    db_locality = models.Locality(locality_name=locality_name)
    db.add(db_locality)
    db.commit()
    db.refresh(db_locality)
    return db_locality

def create_property(db: Session, property: schemas.PropertyCreate):
    locality = get_locality_by_name(db, property.locality)
    if not locality:
        locality = create_locality(db, property.locality)
    db_property = models.Property(property_name=property.property_name, locality_id=locality.locality_id, owner_name=property.owner_name)
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return schemas.Property(
        property_id=db_property.property_id,
        property_name=db_property.property_name,
        locality=locality.locality_name,
        owner_name=db_property.owner_name,
    )

def get_properties_by_locality(db: Session, locality_id: int):
    properties = db.query(models.Property).filter(models.Property.locality_id == locality_id).all()
    return [
        schemas.Property(
            property_id=property.property_id,
            property_name=property.property_name,
            locality=property.locality.locality_name,
            owner_name=property.owner_name
        )
        for property in properties
    ]

def update_property(db: Session, property_id: int, locality_id: int, owner_name: str):
    db_property = db.query(models.Property).filter(models.Property.property_id == property_id).first()
    if db_property:
        db_property.locality_id = locality_id
        db_property.owner_name = owner_name
        db.commit()
        db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int):
    db_property = db.query(models.Property).filter(models.Property.property_id == property_id).first()
    if db_property:
        locality_name = db_property.locality.locality_name  # Access locality name before deleting
        db.delete(db_property)
        db.commit()
        return schemas.Property(
            property_id=db_property.property_id,
            property_name=db_property.property_name,
            locality=locality_name,
            owner_name=db_property.owner_name
        )
    return None
