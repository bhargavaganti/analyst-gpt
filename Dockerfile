# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy the images folder to the container
COPY app/static/images /app/app/static/images

# Expose the port the app runs on
EXPOSE 8080

# Start the application with the increased timeout
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--timeout", "360", "app:create_app()"]

