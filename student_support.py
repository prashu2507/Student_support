from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime
import json
import json
from flask_cors import CORS

  # Enable CORS for all routes
from fuzzywuzzy import process  # For matching user input with questions

# Load question data from JSON
with open("questions.json") as f:
    question_data = json.load(f)

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'

# Flask extensions
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

# Dummy data for testing
assignments = [
    {"subject": "Math", "due_date": "2024-12-25", "description": "Complete Chapter 5 exercises"},
    {"subject": "Science", "due_date": "2024-12-22", "description": "Submit Lab Report"}
]

exams = [
    {"subject": "Math", "exam_date": "2024-12-30", "preparation_notes": "Review chapters 1-4"},
    {"subject": "History", "exam_date": "2024-12-28", "preparation_notes": "Prepare for essay questions"}
]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').lower()

    if 'assignment' in message:
        # Respond with assignments
        response = "Upcoming Assignments:\n"
        for assignment in assignments:
            response += f"{assignment['subject']} - Due Date: {assignment['due_date']} - {assignment['description']}\n"
    elif 'exam' in message:
        # Respond with exams
        response = "Upcoming Exams:\n"
        for exam in exams:
            response += f"{exam['subject']} - Exam Date: {exam['exam_date']} - {exam['preparation_notes']}\n"
    else:
        response = "I'm sorry, I didn't understand that. Ask me about assignments or exams."

    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
