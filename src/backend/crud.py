# crud.py
from sqlmodel import Session, select
from models import User, Doctor, DoctorAccount, Appointment, Prescription, MedicalHistory
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

def get_user_by_password_and_cnp(password: str, cnp: str):
    with Session(engine) as session:
        statement = select(User).where(
            User.password == password,
            User.cnp == cnp)
        return session.exec(statement).first()

def get_user(patient_id: int):
    with Session(engine) as session:
        return session.get(User, patient_id)

# <------------------ Doctor ------------------>

def get_doctors():
    with Session(engine) as session:
        return session.exec(select(Doctor)).all()

def get_doctor(doctor_id: int):
    with Session(engine) as session:
        return session.get(Doctor, doctor_id)

def get_doctor_account_by_email(email: str):
    with Session(engine) as session:
        statement = select(DoctorAccount).where(DoctorAccount.email == email)
        return session.exec(statement).first

def create_doctor_account(account: DoctorAccount):
    with Session(engine) as session:
        session.add(account)
        session.commit()
        session.refresh(account)
        return account

# <------------------ Appointment ------------------>


def create_appointment(appointment: Appointment):
    with Session(engine) as session:
        session.add(appointment)
        session.commit()
        session.refresh(appointment)
        return appointment

def get_user_appointments(patient_id: int):
    with Session(engine) as session:
        statement = select(Appointment).where(Appointment.patient_id == patient_id)
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

def get_user_prescriptions(patient_id: int):
    with Session(engine) as session:
        statement = select(Prescription).where(Prescription.patient_id == patient_id)
        return session.exec(statement).all()

# <------------------ Medical History ------------------>


def create_medical_history(entry: MedicalHistory):
    with Session(engine) as session:
        session.add(entry)
        session.commit()
        session.refresh(entry)
        return entry

def get_user_medical_history(patient_id: int):
    with Session(engine) as session:
        statement = select(MedicalHistory).where(MedicalHistory.patient_id == patient_id)
        return session.exec(statement).all()

