# Use an official Python runtime
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies if requirements.txt exists
RUN pip install --no-cache-dir --upgrade pip && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Run the application
CMD ["python", "app.py"]
