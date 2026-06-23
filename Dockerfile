# Start from an official Python base
FROM python:3.10-slim

# Set the working directory inside container
WORKDIR /app

# Copy requirements file first (for caching)
COPY requirements.txt .

# Install all dependencies
RUN pip install -r requirements.txt

# Copy rest of your code
COPY . .

# Tell Docker which port your app uses
EXPOSE 5000

# Command to run when container starts
CMD ["python", "app.py"]