# Dockerfile
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the container port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

