# Coding Interview Platform

## Goal
A real-time coding interview platform that allows candidates and interviewers to collaborate on code in real-time and execute it safely in the browser.

## Tech Stack
- **Backend**: Python (FastAPI), Socket.IO (python-socketio), uv (Dependency Management), ruff (Linting).
- **Frontend**: React (Vite), Socket.IO Client, Monaco Editor, Pyodide (WASM for execution).
- **Deployment**: Docker (Multi-stage build), Render (or similar).

## Structure
- `backend/`: FastAPI application code.
- `frontend/`: React application code.
- `Dockerfile`: Multi-stage Dockerfile for building both frontend and backend.
- `package.json`: Scripts to run both client and server concurrently.

## How to Use

### Prerequisites
- Node.js (v18+)
- Python (v3.11+)
- `uv` installed (`pip install uv`)

### Installation
1. Install frontend dependencies:
   ```bash
   cd frontend && npm install
   ```
2. Install backend dependencies:
   ```bash
   cd backend && uv sync
   ```
   (Or let `uv run` handle it)

### Running Locally
Run both backend and frontend concurrently:
```bash
npm run dev
```
Access the app at [http://localhost:5173](http://localhost:5173).

### Running with Docker
```bash
docker build -t coding-interview .
docker run -p 8000:8000 coding-interview
```
Access the app at [http://localhost:8000](http://localhost:8000).
