from app.db.database import Base, engine
import app.models.domain.vehicle  # Asegúrate de importar los modelos aquí


# Se inicia labase de datos y de ser el caso crea la tabla
def init_db():
    print("Creando tablas en la base de datos...")
    try:
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas exitosamente.")
    except Exception as e:
        print(f"Error al crear tablas: {e}")
