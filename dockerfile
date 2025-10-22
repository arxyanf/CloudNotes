# Use a small Python base
FROM python:3.11-slim

# Set working dir
WORKDIR /app

# Avoid caching the user environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Ensure static files are readable
RUN mkdir -p /app/app/static

# Expose default port (uvicorn will use $PORT on Render)
EXPOSE 8000

# Use shell form so we can expand $PORT
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
