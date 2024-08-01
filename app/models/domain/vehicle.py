# app/models/domain/persona.py

from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base


# Se crea el modelo paara un usuario
class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(255), index=True)
    modelo = Column(String(255), index=True)
    placa = Column(String(255), unique=True,index=True)
    usuario_id = Column(String(255), index=True)
