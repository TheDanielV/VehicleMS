from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.schema.vehicle import VehicleCreate, VehicleResponse
from app.crud.vehicle import *
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=dict)
def create_new_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    result = create_vehicle(db, vehicle)
    if result is None:
        raise HTTPException(status_code=404, detail="El vehiculo ya existe")
    return result


@router.get("/{vehicle_owner}", response_model=List[VehicleResponse])
def read_vehicles(vehicle_owner: str, db: Session = Depends(get_db)):
    db_vehicles = get_vehicle_by_owner(db, vehicle_owner)
    if not db_vehicles:
        raise HTTPException(status_code=404, detail="No existen vehiculos")
    return db_vehicles


@router.delete("/{vehicle_id}", response_model=dict)
def delete_vehicle_route(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle_response = delete_vehicle_by_id(db, vehicle_id)
    if vehicle_response:
        return {"success": True, "message": "Vehiculo Borrado"}
    else:
        return {"success": False, "message": "Vehiculo no eliminado"}
