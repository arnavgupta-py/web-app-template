# Web App Template (MVP Skeleton)

A modern, high-performance web application skeleton using the following stack:

- **Frontend**: HTMX, Jinja2, Alpine.js, Tailwind CSS
- **Backend**: Python 3.12, FastAPI, Pydantic
- **Database**: PostgreSQL (via SQLAlchemy & Psycopg)
- **Package Manager**: UV

This template serves as a highly scalable boilerplate. It ships with a 100% height-screen viewport layout that automatically binds to window bounds to prevent overflow scrolling.

## Project Structure

```text
project/
├── app/
│   ├── __init__.py
│   ├── backend/
│   │   ├── main.py       # FastAPI application and routing
│   │   └── schemas.py    # Pydantic validation schemas
│   ├── database/
│   │   ├── models.py     # Generic SQLAlchemy ORM models (Item example)
│   │   └── session.py    # Database connection setup
│   └── frontend/
│       └── templates/
│           ├── base.html          # Base layout (Tailwind, HTMX, Alpine)
│           └── index.html         # Empty starter template
├── pyproject.toml        # UV Dependencies
└── README.md
```

## Setup & Running

This project uses `uv` for lightning-fast dependency management with Python 3.12. PostgreSQL is configured as the primary database.

1. **Database Environment Variable**
   You can connect to your PostgreSQL server by setting the `DATABASE_URL` environment variable. By default, it seamlessly connects to: `postgresql+psycopg://postgres:postgres@localhost:5432/my_app_db`

   To change it before running:
   ```powershell
   # Windows (PowerShell)
   $env:DATABASE_URL="postgresql+psycopg://user:password@host:port/dbname"
   ```

2. **Run the Application**
   Start the development server using `uv run`:
   ```bash
   uv run uvicorn app.backend.main:app --reload
   ```

3. **View the Application**
   Open your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Why This Stack for MVP?

- **FastAPI**: Rapid interface building, easy data validation, excellent typing.
- **HTMX**: AJAX without JavaScript. Keeps the mental model on the server and provides SPA-like interactivity cleanly.
- **Alpine.js**: A rugged, minimal tool for composing client-side behavior directly in markup.
- **Tailwind CSS**: Utility-first CSS framework for making beautiful, responsive designs rapidly.
