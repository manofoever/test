# Use the official Python image as the base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container


# Copy the Flask application code into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir flask

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]

