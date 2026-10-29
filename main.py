import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Personal Expense Tracker API")

# Allow browser interactions
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL
    );
    """)
    conn.commit()
    conn.close()

init_db()

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: str

# Serve the HTML page at the home URL
@app.get("/", include_in_schema=False)
def serve_index():
    return FileResponse("index.html")

@app.post("/expenses")
def create_expense(expense: ExpenseCreate):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    query = "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (expense.title, expense.amount, expense.category, expense.date))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, "message": "Expense created successfully"}

@app.get("/expenses")
def get_all_expenses():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    if rows_affected == 0:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": f"Expense {expense_id} deleted successfully"}