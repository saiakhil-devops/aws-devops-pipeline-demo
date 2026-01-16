# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy dependency file first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set environment variable (optional for Flask-style apps)
ENV FLASK_APP=app/app.py

# Run the app
CMD ["python", "app/app.py"]
