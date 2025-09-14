#!/bin/bash
# Railway deployment script

echo "Setting up Railway deployment environment..."

# Generate a random secret key for Django
DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

echo "Please set these environment variables in your Railway dashboard:"
echo ""
echo "SECRET_KEY=${DJANGO_SECRET_KEY}"
echo "DEBUG=False"
echo "ALLOWED_HOSTS=your-app.railway.app,localhost,127.0.0.1"
echo ""
echo "If you're using a database service, Railway will automatically provide DATABASE_URL"
echo "Otherwise, the app will use SQLite as fallback."
echo ""
echo "After setting these variables, redeploy your application."