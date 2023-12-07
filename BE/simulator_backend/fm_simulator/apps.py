from django.apps import AppConfig

class FmSimulatorConfig(AppConfig):
    # Ustawienia domyślnego pola autoinkrementacji dla modeli
    default_auto_field = 'django.db.models.BigAutoField'
    # Nazwa aplikacji w projekcie Django
    name = 'fm_simulator'
