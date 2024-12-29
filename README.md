 Student Support Chatbot

A responsive chatbot application designed to assist students with various queries, such as academic support, scheduling, and general inquiries. This project combines a Flask backend with a modern HTML/CSS/JavaScript frontend.

## Features

- **Student Query Resolution**: AI-powered chatbot for answering student-related questions.
- **Responsive Frontend**: User-friendly interface with chat functionality.
- **Dynamic Chat Handling**: Real-time communication with the chatbot backend.
- **Modular Backend**: Flask-based API to process and respond to user queries.
- **Cross-Origin Support**: CORS-enabled backend for seamless integration.

 Project Structure

```
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
├── templates/
│   └── index.html
├── app.py
├── student_support.py
├── requirements.txt
├── README.md
```

Prerequisites

- Python 3.7+
- Node.js (optional for additional frontend tooling)
- A virtual environment for managing dependencies (recommended)
 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/student-support-chatbot.git
   cd student-support-chatbot
   ```

2. Set up a Python virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install Flask-CORS (if not included in requirements.txt):

   ```bash
   pip install flask-cors
   ```

---
 Running the Project

 Backend (Flask API)

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. Ensure the server is running at `http://127.0.0.1:5000`.

Frontend (HTML/JavaScript)

1. Open `index.html` in your browser.

2. Interact with the chatbot through the input box.

---

Configuration

Backend Configuration
Update `app.py` to adjust the Flask server settings or API endpoints.

Frontend Configuration
Update the `fetch` URL in the `sendMessage` function inside `index.html` or `app.js` to point to your backend's correct address.

---
 Troubleshooting

- **Frontend Not Responding**: 
  - Check the Developer Tools console for errors.
  - Verify the `fetch` URL matches your backend address.

- **CORS Issues**:
  - Ensure Flask-CORS is installed and configured.

- **Backend Errors**:
  - Check Flask logs for error messages.

---
Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

License

This project is licensed under the MIT License. See the `LICENSE` file for details
Acknowledgments

- **Flask Framework** for the robust backend.
- **OpenAI GPT Models** for AI-powered query handling.
- **Bootstrap** for styling and responsive design.
