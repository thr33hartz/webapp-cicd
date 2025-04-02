FROM python:3.10.12-slim

WORKDIR /app

# Prevent Python from writing .pyc files and enable output buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other necessary files
COPY . .

# Use Gunicorn for production
CMD ["gunicorn", "-b", "0.0.0.0:5001", "app:app"]
