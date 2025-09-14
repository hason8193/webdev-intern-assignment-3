#!/bin/bash

# Exit on any failure
set -e

echo "Starting Django application..."

# Wait for database to be ready (if using external database)
echo "Waiting for database..."
sleep 5

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist (optional)
echo "Creating superuser if needed..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
" || echo "Superuser creation skipped"

# Start the application with Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn gscores.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120 \
    --max-requests 1000 \
    --max-requests-jitter 100 \
    --access-logfile - \
    --error-logfile -