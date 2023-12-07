from django.urls import path
from .views import simulate_fm_modulation

urlpatterns = [
    # Ścieżka do symulacji modulacji FM
    path('simulate_fm/', simulate_fm_modulation, name='simulate_fm_modulation'),
]