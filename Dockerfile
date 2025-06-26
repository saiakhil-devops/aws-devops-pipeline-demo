# Base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy application code and requirements
COPY app/ app/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
