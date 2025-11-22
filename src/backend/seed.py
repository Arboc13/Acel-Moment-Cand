# seed.py
from models import Doctor
from database import engine
from sqlmodel import Session

doctors = [
    Doctor(name="Dr. Alice", specialization="Cardiology"),
    Doctor(name="Dr. Bob", specialization="Neurology"),
]

with Session(engine) as session:
    for d in doctors:
        session.add(d)
    session.commit()

print("Seeded doctors!")
