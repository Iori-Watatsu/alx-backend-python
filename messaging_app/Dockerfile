# Use Python 3.10 base image
FROM python:3.10
# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1 ENV 
PYTHONUNBUFFERED=1
# Set working directory
WORKDIR /app
# Copy requirements file
COPY requirements.txt /app/
# Install dependencies
RUN pip install --upgrade pip && pip install -r 
requirements.txt
# Copy project files
COPY . /app/
# Expose Django default port
EXPOSE 8000
# Run Django development server
CMD ["python", "manage.py", "runserver", 
"0.0.0.0:8000"]
