from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.schema.vehicle import VehicleCreate, VehicleResponse
from app.crud.vehicle import create_vehicle, get_vehicle_by_owner
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=VehicleResponse)
def create_new_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db, vehicle)


@router.get("/{vehicle_owner}", response_model=VehicleResponse)
def read_vehicle(vehicle_owner: str, db: Session = Depends(get_db)):
    db_vehicle = get_vehicle_by_owner(db, vehicle_owner)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle
