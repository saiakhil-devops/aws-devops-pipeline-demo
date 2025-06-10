# Use official Python image
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy your local app folder into /app in the container
COPY app/ .

# Run the app when the container starts
CMD ["python", "app.py"]
