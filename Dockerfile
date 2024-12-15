# Base image
FROM python:3.10

# Working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 4000

# Start server
CMD ["gunicorn", "football_booking.wsgi:application", "--bind", "0.0.0.0:4000"]
