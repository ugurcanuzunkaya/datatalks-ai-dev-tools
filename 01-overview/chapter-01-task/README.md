# Django TODO App

A simple, robust, and beautiful TODO application built with Django. Designed to help you manage tasks efficiently with a modern user interface.

## Features

- **✨ Modern UI**: Clean, card-based layout with Google Fonts (Inter) and Bootstrap 5.
- **📅 Smart Date Picker**: Easily assign due dates with a picker that prevents selecting past dates.
- **✅ Task Management**: Create, edit, delete, and mark tasks as complete.
- **📱 Responsive**: Fully responsive design that works great on mobile and desktop.
- **🏷️ Visual Status**: Clear visual indicators for pending and completed tasks.

## Tech Stack

- **Python**: Core programming language.
- **Django**: High-level Python web framework.
- **Bootstrap 5**: Frontend framework for styling.
- **JavaScript**: For interactive form elements.
- **uv**: Fast Python package installer and resolver.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>/01-overview/chapter-01-task
    ```

2.  **Initialize the environment and install dependencies with `uv`:**
    ```bash
    uv sync
    ```
    Or manually:
    ```bash
    uv venv
    source .venv/bin/activate
    uv add django
    ```

3.  **Apply migrations:**
    ```bash
    uv run python manage.py migrate
    ```

4.  **Run the development server:**
    ```bash
    uv run python manage.py runserver
    ```

5.  **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:8000`.

## Testing

To run the automated tests:

```bash
uv run python manage.py test
```
