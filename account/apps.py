"""Модуль, содержащий основную конфигурацию приложения account. """

from django.apps import AppConfig


class AccountConfig(AppConfig):
    """. """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
