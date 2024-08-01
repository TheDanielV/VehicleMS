# MecanicaMs/app/crud/vehicle.py

from sqlalchemy.orm import Session
from app.models.domain.vehicle import Vehicle
from app.models.schema.vehicle import VehicleCreate


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vehicle(
        marca=vehicle.marca,
        modelo=vehicle.modelo,
        placa=vehicle.placa,
        usuario_id=vehicle.usuario_id
    )
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def get_vehicle_by_owner(db: Session, usuario_id: str):
    return db.query(Vehicle).filter(Vehicle.usuario_id == usuario_id).first()
