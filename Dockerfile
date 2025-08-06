FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install required system packages (for ujson and others)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set final working directory
WORKDIR /app/src

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "openapi_server.main:app", "--host", "0.0.0.0", "--port", "8080"]
