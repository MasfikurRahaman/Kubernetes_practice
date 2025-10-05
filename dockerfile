# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the new Python app
COPY app_new.py app.py

# (Optional) Install dependencies if needed
# RUN pip install --no-cache-dir <package>

# Run the Python app
CMD ["python", "app.py"]

