# main.py
from fastapi import FastAPI
from sqlmodel import Session, select

from database import create_db_and_tables
from models import User
from crud import get_users, create_user
from fastapi import HTTPException
from models import User, Doctor, Appointment, Prescription, MedicalHistory
from crud import (
    get_user_by_email, get_user, get_doctors, get_doctor,
    create_appointment, get_user_appointments, get_doctor_appointments,
    create_prescription, get_user_prescriptions,
    create_medical_history, get_user_medical_history
)




app = FastAPI()

@app.post("/login")
def login(email: str, password: str):
    user = get_user_by_email(email)
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return user



@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Backend is running!"}

# <------------------ User ------------------>


@app.get("/users")
def list_users():
    return get_users()

@app.post("/users")
def add_user(user: User):
    return create_user(user)


@app.get("/users/{user_id}")
def get_user_endpoint(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# <------------------ Doctor ------------------>


@app.get("/doctors")
def list_doctors():
    return get_doctors()

@app.get("/doctors/{doctor_id}")
def get_doctor_endpoint(doctor_id: int):
    doctor = get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

# <------------------ Appointments ------------------>



@app.post("/appointments")
def add_appointment(appointment: Appointment):
    return create_appointment(appointment)

@app.get("/appointments/user/{user_id}")
def list_user_appointments(user_id: int):
    return get_user_appointments(user_id)

@app.get("/appointments/doctor/{doctor_id}")
def list_doctor_appointments(doctor_id: int):
    return get_doctor_appointments(doctor_id)

# <------------------ Prescriptions ------------------>




@app.post("/prescriptions")
def add_prescription(prescription: Prescription):
    return create_prescription(prescription)

@app.get("/prescriptions/user/{user_id}")
def list_user_prescriptions(user_id: int):
    return get_user_prescriptions(user_id)


# <------------------ Medical History ------------------>



@app.post("/medical_history")
def add_medical_history(entry: MedicalHistory):
    return create_medical_history(entry)

@app.get("/medical_history/user/{user_id}")
def list_medical_history(user_id: int):
    return get_user_medical_history(user_id)
