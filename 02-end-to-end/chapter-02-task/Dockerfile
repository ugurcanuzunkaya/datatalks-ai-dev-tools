FROM node:20-slim as frontend-builder

WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend ./
RUN npm run build

FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy backend
COPY backend/pyproject.toml backend/uv.lock* ./
RUN uv pip install --system -r pyproject.toml

COPY backend/src ./src
COPY backend/ruff.toml .

# Copy frontend build
COPY --from=frontend-builder /app/frontend/dist ./static

# Expose port
EXPOSE 8000

# Run
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
