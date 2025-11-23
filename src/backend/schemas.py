# schemas.py
from sqlmodel import SQLModel
from datetime import datetime
from typing import Optional

class AppointmentCreate(SQLModel):
    patient_id: int
    doctor_id: int
    datetime: datetime
    status: Optional[str] = "pending"


class PrescriptionCreate(SQLModel):
    patient_id: int
    doctor_id: int
    medication_name: str
    dosage: str
    notes: str


class MedicalHistoryCreate(SQLModel):
    patient_id: int
    description: str
