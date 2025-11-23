from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from datetime import datetime

from database import engine, create_db_and_tables

from models import User, Doctor, Appointment, Prescription, MedicalHistory
from crud import (
    get_user_by_password_and_cnp, get_user, get_doctors, get_doctor,
    create_appointment, get_user_appointments, get_doctor_appointments,
    create_prescription, get_user_prescriptions,
    create_medical_history, get_user_medical_history
)

from schemas import AppointmentCreate, PrescriptionCreate, MedicalHistoryCreate
from crud import get_user_by_password_and_cnp

# -------------------- APP INIT --------------------
app = FastAPI()


# -------------------- CORS --------------------
origins = [
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------- STARTUP --------------------
@app.on_event("startup")
def startup():
    create_db_and_tables()


# -------------------- GLOBAL ERROR HANDLER --------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"\n--- SERVER ERROR ---\n{exc}\n")
    return JSONResponse(
        status_code=500,
        content={"detail": f"Unexpected error: {str(exc)}"}
    )


# -------------------- ROOT --------------------
@app.get("/")
def root():
    return {"message": "Backend is running!"}


# -------------------- LOGIN --------------------
@app.post("/login")
def login(password: str, cnp: str):

    """
    email = credentials.get("cnp")
    password = credentials.get("parola")

    user = get_user_by_email(email)
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return user
    """
    data = User(password = password, cnp = cnp)
    return get_user_by_password_and_cnp(password, cnp)

# -------------------- PATIENTS --------------------
@app.get("/patients/{patient_id}")
def get_patient_endpoint(patient_id: int):
    patient = get_user(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


# -------------------- DOCTORS --------------------
@app.get("/doctors")
def list_doctors():
    return get_doctors()


@app.get("/doctors/{doctor_id}")
def get_doctor_endpoint(doctor_id: int):
    doctor = get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


# -------------------- APPOINTMENTS --------------------
@app.post("/appointments")
def add_appointment(patient_id: int, doctor_id: int, datetime: datetime):
    data = Appointment(patient_id=patient_id, doctor_id=doctor_id, datetime=datetime)
    return create_appointment(data)


@app.get("/appointments/user/{patient_id}")
def list_user_appointments(patient_id: int):
    return get_user_appointments(patient_id)


@app.get("/appointments/doctor/{doctor_id}")
def list_doctor_appointments(doctor_id: int):
    return get_doctor_appointments(doctor_id)


# -------------------- PRESCRIPTIONS --------------------
@app.post("/prescriptions")
def add_prescription(patient_id:int, doctor_id:int, medication_name:str, dosage:str, notes:str):
    data = Prescription(patient_id = patient_id,doctor_id = doctor_id,medication_name = medication_name,dosage = dosage,notes = notes)
    return create_prescription(data)


@app.get("/prescriptions/user/{patient_id}")
def list_user_prescriptions(patient_id: int):
    return get_user_prescriptions(patient_id)


# -------------------- MEDICAL HISTORY --------------------
@app.post("/medical_history")
def add_medical_history(patient_id: int, description: str ):
    data = MedicalHistory(patient_id=patient_id, description=description)
    return create_medical_history(data)


@app.get("/medical_history/user/{patient_id}")
def list_medical_history(patient_id: int):
    return get_user_medical_history(patient_id)
