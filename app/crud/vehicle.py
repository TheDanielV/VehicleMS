# MecanicaMs/app/crud/vehicle.py
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models.domain.vehicle import Vehicle
from app.models.schema.vehicle import VehicleCreate


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vehicle(
        marca=vehicle.marca,
        modelo=vehicle.modelo,
        placa=vehicle.placa,
        usuario_id=vehicle.usuario_id,
        anio=vehicle.anio,
        color=vehicle.color
    )
    try:
        db.add(db_vehicle)
        db.commit()
        db.refresh(db_vehicle)
        return {"detail": "Vehiculo creado"}
    except IntegrityError as ie:
        db.rollback()
        return None


def get_vehicle_by_owner(db: Session, usuario_id: str):
    return db.query(Vehicle).filter(Vehicle.usuario_id == usuario_id).all()


def delete_vehicle_by_id(db: Session, vehicle_id: int):
    # Obtener el objeto a eliminar
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if vehicle is None:
        return False
    else:
        try:
            db.delete(vehicle)
            db.commit()
        except IntegrityError:
            db.rollback()  # Deshacer los cambios en caso de error
            return False
        return True
