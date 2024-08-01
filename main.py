from fastapi import FastAPI
from app.api.v1.endpoint import vehicle
from app.db.init_db import init_db

app = FastAPI()

app.include_router(vehicle.router, prefix="/vehicle", tags=["vehicle"])


@app.on_event("startup")
def on_startup():
    init_db()
