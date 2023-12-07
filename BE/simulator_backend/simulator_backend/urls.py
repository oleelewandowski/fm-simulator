"""
Konfiguracja URL dla projektu simulator_backend.

Lista `urlpatterns` kieruje URL-e do widoków. Aby uzyskać więcej informacji, proszę zobaczyć:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Przykłady:
Widoki oparte na funkcjach
    1. Dodaj import:  from my_app import views
    2. Dodaj URL do urlpatterns:  path('', views.home, name='home')
Widoki oparte na klasach
    1. Dodaj import:  from other_app.views import Home
    2. Dodaj URL do urlpatterns:  path('', Home.as_view(), name='home')
Dołączanie innej konfiguracji URL
    1. Importuj funkcję include(): from django.urls import include, path
    2. Dodaj URL do urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Ścieżka do panelu administracyjnego Django
    path('admin/', admin.site.urls),
    # Dołączenie URL-i z aplikacji signal_processor
    path('signal_processor/', include('fm_simulator.urls')),
]
