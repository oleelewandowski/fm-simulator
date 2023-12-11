"""
Konfiguracja WSGI dla projektu simulator_backend.

Udostępnia wywoływalny obiekt WSGI jako zmienną na poziomie modułu o nazwie ``application``.

Aby uzyskać więcej informacji na temat tego pliku, zobacz
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Ustawienie domyślnego modułu ustawień Django dla tego projektu
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simulator_backend.settings')

# Tworzenie i konfiguracja aplikacji WSGI
application = get_wsgi_application()
