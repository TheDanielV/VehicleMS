# app/models/schema/persona.py

from pydantic import BaseModel


# se crea el Schema (el tipo de dato) para un vehiculo
class VehicleBase(BaseModel):
    marca: str
    modelo: str
    placa: str
    usuario_id: str
    anio: str
    color: str


class VehicleCreate(VehicleBase):
    pass


class VehicleResponse(VehicleBase):
    id: int

    class Config:
        orm_mode = True
