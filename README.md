# 💰 Personal Expense Tracker

A lightweight, full-stack personal expense tracking web application built with FastAPI, SQLite, and vanilla HTML/CSS/JavaScript.

## 🚀 Features
- **Full REST API CRUD Operations**: Create, read, and delete expense entries.
- **Persistent Storage**: SQLite database with automatic table initialization.
- **Data Validation**: Strict type checking with Pydantic schemas.
- **Interactive API Documentation**: Auto-generated Swagger UI at `/docs`.
- **Live Frontend Dashboard**: Real-time spending total (₹), category breakdown chips, and category filtering.

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, Uvicorn
- **Database**: SQLite3
- **Validation**: Pydantic
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)

## 📦 How to Run Locally

1. Install dependencies:
   ```bash
   py -m pip install -r requirements.txt