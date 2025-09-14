from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.db.utils import OperationalError

def health_check(request):
    """Health check endpoint that tests database connectivity"""
    try:
        # Test database connection
        db_conn = connections['default']
        db_conn.cursor()
        return JsonResponse({
            'status': 'healthy',
            'database': 'connected',
            'django': 'running'
        })
    except OperationalError:
        return JsonResponse({
            'status': 'unhealthy',
            'database': 'disconnected',
            'django': 'running'
        }, status=503)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'error': str(e),
            'django': 'running'
        }, status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),  # Health check endpoint
    path('', include('scores.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
