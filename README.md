# 🧠 CrisisAlert Backend

This is the backend of **CrisisAlert** — a real-time emergency reporting platform using **Python FastAPI**.

## 🚀 Features

- Receive crisis reports via POST request
- Serve list of all reports via GET
- CORS-enabled to allow frontend communication
- Clean and lightweight REST API

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- CORS Middleware

## 📦 Installation & Run

```bash
git clone https://github.com/imransharp/crisisalert-backend.git
cd crisisalert-backend

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
