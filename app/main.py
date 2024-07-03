from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/properties/add", response_model=schemas.Property)
def add_new_property(property: schemas.PropertyCreate, db: Session = Depends(get_db)):
    return crud.create_property(db=db, property=property)

@app.get("/api/properties/fetch", response_model=list[schemas.Property])
def fetch_all_properties(locality_name: str = None, locality_id: int = None, db: Session = Depends(get_db)):
    if locality_name:
        locality = crud.get_locality_by_name(db, locality_name)
        if locality:
            return crud.get_properties_by_locality(db, locality.locality_id)
        else:
            raise HTTPException(status_code=404, detail="Locality not found")
    elif locality_id:
        return crud.get_properties_by_locality(db, locality_id)
    else:
        raise HTTPException(status_code=400, detail="Provide locality_name or locality_id")

@app.put("/api/properties/update", response_model=schemas.Property)
def update_property_details(
    property_id: int = Body(...), 
    locality_id: int = Body(...), 
    owner_name: str = Body(...), 
    db: Session = Depends(get_db)
):
    updated_property = crud.update_property(db, property_id, locality_id, owner_name)
    if not updated_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return schemas.Property(
        property_id=updated_property.property_id,
        property_name=updated_property.property_name,
        locality=updated_property.locality.locality_name,
        owner_name=updated_property.owner_name
    )

@app.delete("/api/properties/delete", response_model=schemas.Property)
def delete_property_record(property: schemas.PropertyDelete, db: Session = Depends(get_db)):
    deleted_property = crud.delete_property(db, property.property_id)
    if not deleted_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return deleted_property

@app.get("/api/localities/all", response_model=list[schemas.Locality])
def get_all_localities(db: Session = Depends(get_db)):
    return db.query(models.Locality).all()
