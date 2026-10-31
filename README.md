# Personal Expense Tracker

A lightweight, full-stack personal expense tracking web application built with FastAPI, SQLite, and vanilla HTML/CSS/JavaScript.

**Live Demo:** [https://expense-tracker-fyb2.onrender.com](https://expense-tracker-fyb2.onrender.com)

---

## Features
- **Full REST API CRUD Operations**: Create, view, and delete expense entries seamlessly.
- **Persistent Storage**: SQLite database with automatic table initialization on startup.
- **Data Validation**: Strict request/response payload validation via Pydantic models.
- **Interactive Documentation**: Auto-generated Swagger UI accessible directly at `/docs`.
- **Live Frontend Dashboard**: Real-time spending total (₹), category breakdown chips, and instant category filtering.

---

## Tech Stack
- **Backend**: Python 3, FastAPI, Uvicorn
- **Database**: SQLite3
- **Validation**: Pydantic
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)

---

## How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/AtchyutaTanmayaKannegolla/expense-tracker.git](https://github.com/AtchyutaTanmayaKannegolla/expense-tracker.git)
cd expense-tracker