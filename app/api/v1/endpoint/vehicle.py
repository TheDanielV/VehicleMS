from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.schema.vehicle import VehicleCreate, VehicleResponse
from app.crud.vehicle import *
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


@router.delete("/vehicle/{vehicle_id}", response_model=dict)
def delete_vehicle_route(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle_response = delete_vehicle_by_id(db, vehicle_id)
    if vehicle_response:
        return {"success": True, "message": "Vehiculo Borrado"}
    else:
        return {"success": False, "message": "Vehiculo no eliminado"}
