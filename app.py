from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app)  # Enable CORS for all routes

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
from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialize the sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

@app.route('/analyze_message', methods=['POST'])
def analyze_message():
    data = request.json
    user_message = data.get("message", "")

    # Perform sentiment analysis
    sentiment_scores = sentiment_analyzer.polarity_scores(user_message)
    compound_score = sentiment_scores['compound']
    
    # Determine sentiment category
    if compound_score >= 0.05:
        sentiment = "positive"
    elif compound_score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    # Generate a response based on sentiment
    if sentiment == "positive":
        bot_response = "I'm glad to hear that! How can I assist you further?"
    elif sentiment == "negative":
        bot_response = "I'm sorry to hear that. Let me help you with this issue."
    else:
        bot_response = "Got it. Could you provide more details?"

    # Return response
    return jsonify({
        "user_message": user_message,
        "sentiment": sentiment,
        "response": bot_response,
        "sentiment_scores": sentiment_scores
    })

if __name__ == "__main__":
    app.run(debug=True)
