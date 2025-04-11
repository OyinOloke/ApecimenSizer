from sqlalchemy import Table, Column, Integer, String, Float
from database import metadata

specimens = Table(
    "specimens",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(100)),
    Column("specimen_size", Float),
    Column("magnification", Float),
    Column("actual_size", Float),
)
