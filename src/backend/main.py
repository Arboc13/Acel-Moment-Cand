from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlmodel import Session, SQLModel
from models import User, Doctor, Appointment, Prescription, MedicalHistory
from crud import (
    get_user_by_email, get_user, get_doctors, get_doctor,
    create_appointment, get_user_appointments, get_doctor_appointments,
    create_prescription, get_user_prescriptions,
    create_medical_history, get_user_medical_history
)
from database import create_db_and_tables, engine

app = FastAPI()
SQLModel.metadata.create_all(engine)


# ----- CORS SETTINGS -----
origins = [
    "http://localhost:5173",  # your React frontend
    "http://localhost:3000",  # optional: another local frontend port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # allow requests from these URLs
    allow_credentials=True,
    allow_methods=["*"],     # allow GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],     # allow any headers
)
# --------------------------

# --- Startup event ---
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- Global exception handler ---
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Log exception (optional)
    print(f"Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": f"Unexpected error: {str(exc)}"}
    )

# --- Root ---
@app.get("/")
def root():
    return {"message": "Backend is running!"}

# --- Login ---
@app.post("/login")
def login(email: str, password: str):
    try:
        user = get_user_by_email(email)
        if not user or user.password != password:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Login failed: {str(e)}")

# --- Users ---
@app.get("/users/{user_id}")
def get_user_endpoint(user_id: int):
    try:
        user = get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving user: {str(e)}")

# --- Doctors ---
@app.get("/doctors")
def list_doctors():
    try:
        return get_doctors()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving doctors: {str(e)}")

@app.get("/doctors/{doctor_id}")
def get_doctor_endpoint(doctor_id: int):
    try:
        doctor = get_doctor(doctor_id)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        return doctor
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving doctor: {str(e)}")

# --- Appointments ---
@app.post("/appointments")
def add_appointment(appointment: Appointment):
    try:
        return create_appointment(appointment)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not create appointment: {str(e)}")

@app.get("/appointments/user/{user_id}")
def list_user_appointments(user_id: int):
    try:
        return get_user_appointments(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not fetch user appointments: {str(e)}")

@app.get("/appointments/doctor/{doctor_id}")
def list_doctor_appointments(doctor_id: int):
    try:
        return get_doctor_appointments(doctor_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not fetch doctor appointments: {str(e)}")

# --- Prescriptions ---
@app.post("/prescriptions")
def add_prescription(prescription: Prescription):
    try:
        return create_prescription(prescription)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not create prescription: {str(e)}")

@app.get("/prescriptions/user/{user_id}")
def list_user_prescriptions(user_id: int):
    try:
        return get_user_prescriptions(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not fetch user prescriptions: {str(e)}")

# --- Medical History ---
@app.post("/medical_history")
def add_medical_history(entry: MedicalHistory):
    try:
        return create_medical_history(entry)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not create medical history entry: {str(e)}")

@app.get("/medical_history/user/{user_id}")
def list_medical_history(user_id: int):
    try:
        return get_user_medical_history(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not fetch medical history: {str(e)}")
