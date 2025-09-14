#!/bin/bash

set -e  # Exit on any error

echo "Starting Django application..."

# Check if we have database configuration
if [ -n "$DATABASE_URL" ] || [ -n "$DATABASE_HOST" ]; then
    echo "Database configuration found, waiting for database..."
    python -c "
import os
import time
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gscores.settings')
django.setup()

from django.db import connections
from django.db.utils import OperationalError

try:
    db_conn = connections['default']
    attempts = 0
    while attempts < 30:
        try:
            db_conn.cursor()
            print('Database connection successful!')
            break
        except OperationalError as e:
            attempts += 1
            print(f'Database unavailable, waiting... (attempt {attempts}/30): {e}')
            time.sleep(2)
    else:
        print('Could not connect to database after 30 attempts')
        exit(1)
except Exception as e:
    print(f'Database connection error: {e}')
    print('Continuing without database connection check...')
"
else
    echo "No database configuration found, skipping database check..."
fi

# Run migrations (will create SQLite if no other DB configured)
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "Creating superuser if needed..."
python manage.py shell << 'EOF'
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print('Superuser created: admin/admin123')
    else:
        print('Superuser already exists')
except Exception as e:
    print(f'Superuser creation error: {e}')
EOF

echo "Starting Gunicorn server..."
exec gunicorn gscores.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers ${WEB_CONCURRENCY:-2} \
    --timeout 120 \
    --keep-alive 2 \
    --max-requests 1000 \
    --max-requests-jitter 100 \
    --access-logfile - \
    --error-logfile - \
    --log-level info