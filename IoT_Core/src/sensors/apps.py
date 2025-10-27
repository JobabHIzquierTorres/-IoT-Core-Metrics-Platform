from django.apps import AppConfig


class SensorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensors'


"""
    App responsable de capturar, validar y almacenar datos de sensores IoT (por ejemplo una Raspberry Pi).

    Funciones principales:
    - Recibe datos desde dispositivos físicos o virtuales.
    - Persiste lecturas en TimescaleDB con timestamp.
    - Expone endpoints API para consulta y envío de datos.
    - Puede generar eventos para procesamiento en tiempo real.
"""
