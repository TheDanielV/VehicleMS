from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:SecretPassword@vehiclesql.orangecliff-243aedf8.australiaeast.azurecontainerapps.io/vehicle"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear una clase base para los modelos
Base = declarative_base()

# Crear un sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
