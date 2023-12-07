"""
Konfiguracja ASGI dla projektu simulator_backend.

Udostępnia wywoływalny obiekt ASGI jako zmienną na poziomie modułu o nazwie ``application``.

Aby uzyskać więcej informacji na temat tego pliku, zobacz
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Ustawienie domyślnego modułu ustawień Django dla tego projektu
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simulator_backend.settings')

# Tworzenie i konfiguracja aplikacji ASGI
application = get_asgi_application()
