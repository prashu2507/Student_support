from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from models import SessionLocal, Assignment, Exam

# Initialize the scheduler
scheduler = BackgroundScheduler()

# Function to check upcoming assignments
def check_assignments_reminder():
    db = SessionLocal()
    assignments = db.query(Assignment).filter(Assignment.due_date > datetime.now()).all()
    for assignment in assignments:
        print(f"Reminder: {assignment.subject} assignment due on {assignment.due_date}")
    db.close()

# Function to check upcoming exams
def check_exam_reminder():
    db = SessionLocal()
    exams = db.query(Exam).filter(Exam.exam_date > datetime.now()).all()
    for exam in exams:
        print(f"Reminder: {exam.subject} exam on {exam.exam_date}")
    db.close()

# Add jobs to the scheduler
scheduler.add_job(check_assignments_reminder, 'interval', minutes=30)  # Check every 30 minutes
scheduler.add_job(check_exam_reminder, 'interval', minutes=30)  # Check every 30 minutes

# Start the scheduler
def start_scheduler():
    scheduler.start()
