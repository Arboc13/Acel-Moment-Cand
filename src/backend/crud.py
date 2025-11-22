# crud.py
from sqlmodel import Session, select
from models import User, Doctor, Appointment, Prescription, MedicalHistory
from database import engine

def get_users():
    with Session(engine) as session:
        return session.exec(select(User)).all()

def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

# <------------------ User ------------------>

def get_user_by_email(email: str):
    with Session(engine) as session:
        statement = select(User).where(User.email == email)
        return session.exec(statement).first()

def get_user(user_id: int):
    with Session(engine) as session:
        return session.get(User, user_id)

# <------------------ Doctor ------------------>

def get_doctors():
    with Session(engine) as session:
        return session.exec(select(Doctor)).all()

def get_doctor(doctor_id: int):
    with Session(engine) as session:
        return session.get(Doctor, doctor_id)

# <------------------ Appointment ------------------>


def create_appointment(appointment: Appointment):
    with Session(engine) as session:
        session.add(appointment)
        session.commit()
        session.refresh(appointment)
        return appointment

def get_user_appointments(user_id: int):
    with Session(engine) as session:
        statement = select(Appointment).where(Appointment.user_id == user_id)
        return session.exec(statement).all()

def get_doctor_appointments(doctor_id: int):
    with Session(engine) as session:
        statement = select(Appointment).where(Appointment.doctor_id == doctor_id)
        return session.exec(statement).all()

# <------------------ Prescription ------------------>


def create_prescription(prescription: Prescription):
    with Session(engine) as session:
        session.add(prescription)
        session.commit()
        session.refresh(prescription)
        return prescription

def get_user_prescriptions(user_id: int):
    with Session(engine) as session:
        statement = select(Prescription).where(Prescription.user_id == user_id)
        return session.exec(statement).all()

# <------------------ Medical History ------------------>


def create_medical_history(entry: MedicalHistory):
    with Session(engine) as session:
        session.add(entry)
        session.commit()
        session.refresh(entry)
        return entry

def get_user_medical_history(user_id: int):
    with Session(engine) as session:
        statement = select(MedicalHistory).where(MedicalHistory.user_id == user_id)
        return session.exec(statement).all()

