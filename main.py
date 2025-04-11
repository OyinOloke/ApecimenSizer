from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database, engine, metadata
from models import specimens
from schemas import SpecimenCreate, SpecimenOut

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup...")
    await database.connect()  # Connect to the database on startup
    yield
    print("Application shutdown...")
    await database.disconnect()  # Disconnect from the database on shutdown

app = FastAPI(lifespan=lifespan)

metadata.create_all(engine)

@app.post("/calculate", response_model=SpecimenOut)
async def calculate_specimen(data: SpecimenCreate):
    actual_size = data.specimen_size / data.magnification
    query = specimens.insert().values(
        username=data.username,
        specimen_size=data.specimen_size,
        magnification=data.magnification,
        actual_size=actual_size
    )
    record_id = await database.execute(query)
    return {
        "id": record_id,
        "username": data.username,
        "specimen_size": data.specimen_size,
        "magnification": data.magnification,
        "actual_size": actual_size
    }

@app.get("/records", response_model=list[SpecimenOut])
async def get_records():
    query = specimens.select()
    return await database.fetch_all(query)
