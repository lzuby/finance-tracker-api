# Finance Tracker API

A REST API for tracking personal finance transactions, built from scratch with Python and FastAPI.

## Tech Stack
- Python, FastAPI, SQLite, Uvicorn

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/transactions` | List all transactions |
| POST | `/transactions` | Add a transaction |
| PUT | `/transactions/{id}` | Update a transaction |
| DELETE | `/transactions/{id}` | Delete a transaction |

## Run Locally

git clone https://github.com/lzuby/finance-tracker-api
cd finance-tracker-api
pip install fastapi uvicorn
uvicorn main:app --reload

Visit http://localhost:8000/docs for the interactive API docs.
