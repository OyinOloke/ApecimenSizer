from fastapi import FastAPI
from database import database, engine, metadata
from models import specimens
from schemas import SpecimenCreate, SpecimenOut

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


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
