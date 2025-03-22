from django.apps import AppConfig


class HelloworldConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "helloworldplugin"  # Must match plugin folder/symlink name
    verbose_name = "Hello World"
