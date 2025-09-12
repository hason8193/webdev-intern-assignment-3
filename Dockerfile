# Use official Python runtime as base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=gscores.settings

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Create staticfiles directory
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Create entrypoint script
RUN echo '#!/bin/bash\n\
    set -e\n\
    \n\
    echo "Waiting for database..."\n\
    while ! nc -z db 5432; do\n\
    sleep 0.1\n\
    done\n\
    echo "Database available!"\n\
    \n\
    echo "Running migrations..."\n\
    python manage.py migrate\n\
    \n\
    echo "Loading initial data..."\n\
    python manage.py import_scores --batch-size=1000 2>/dev/null || echo "Data already imported or import failed"\n\
    \n\
    echo "Creating superuser..."\n\
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='\''admin'\'').exists() or User.objects.create_superuser('\''admin'\'', '\''admin@example.com'\'', '\''admin123'\'')" 2>/dev/null || echo "Superuser already exists"\n\
    \n\
    echo "Starting server..."\n\
    exec "$@"' > /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

# Expose port
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Default command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "gscores.wsgi:application"]