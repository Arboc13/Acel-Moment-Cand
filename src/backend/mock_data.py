from sqlmodel import Session
from database import engine
from models import User, Doctor, Appointment, Prescription, MedicalHistory
from datetime import datetime, timedelta

# --- Open a DB session ---
with Session(engine) as session:

    # --- USERS ---
    users = [
        User(name="Alice", email="alice@example.com", password="1234", cnp="1"),
        User(name="Bob", email="bob@example.com", password="5678", cnp="2"),
        User(name="Charlie", email="charlie@example.com", password="9013", cnp="3"),
        User(name="David", email="david@example.com", password="7113", cnp="4"),
        User(name="Eve", email="eve@example.com", password="4321", cnp="5"),
    ]
    session.add_all(users)
    session.commit()

    # --- DOCTORS ---
    doctors = [
        Doctor(name="Dr. Smith", specialization="Cardiology"),
        Doctor(name="Dr. Johnson", specialization="Dermatology"),
    ]
    session.add_all(doctors)
    session.commit()

    # --- APPOINTMENTS ---
    appointments = [
        Appointment(patient_id=1, doctor_id=1, datetime=datetime.utcnow() + timedelta(days=1), status="pending"),
        Appointment(patient_id=2, doctor_id=1, datetime=datetime.utcnow() + timedelta(days=2), status="confirmed"),
        Appointment(patient_id=3, doctor_id=2, datetime=datetime.utcnow() + timedelta(days=3), status="pending"),
        Appointment(patient_id=4, doctor_id=2, datetime=datetime.utcnow() + timedelta(days=1), status="confirmed"),
        Appointment(patient_id=5, doctor_id=1, datetime=datetime.utcnow() + timedelta(days=4), status="pending"),
    ]
    session.add_all(appointments)
    session.commit()

    # --- PRESCRIPTIONS ---
    prescriptions = [
        Prescription(patient_id=1, doctor_id=1, medication_name="Ibuprofen", dosage="200mg", notes="Take twice daily"),
        Prescription(patient_id=2, doctor_id=1, medication_name="Paracetamol", dosage="500mg", notes="After meals"),
        Prescription(patient_id=3, doctor_id=2, medication_name="Amoxicillin", dosage="250mg", notes="3 times a day"),
        Prescription(patient_id=4, doctor_id=2, medication_name="Cetirizine", dosage="10mg", notes="Once daily"),
        Prescription(patient_id=5, doctor_id=1, medication_name="Loratadine", dosage="10mg", notes="Once daily"),
    ]
    session.add_all(prescriptions)
    session.commit()

    # --- MEDICAL HISTORY ---
    history = [
        MedicalHistory(patient_id=1, description="Annual check-up"),
        MedicalHistory(patient_id=2, description="Skin rash"),
        MedicalHistory(patient_id=3, description="Allergy testing"),
        MedicalHistory(patient_id=4, description="Blood work"),
        MedicalHistory(patient_id=5, description="Vaccination"),
    ]
    session.add_all(history)
    session.commit()

print("Mock database created with 5 users, 2 doctors, appointments, prescriptions, and medical history!")
