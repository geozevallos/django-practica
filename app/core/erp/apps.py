from django.apps import AppConfig

# Como esta dentro de una carpeta debo cambiar el name con ruta, por eso es core.erp y no erp
class ErpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.erp'
