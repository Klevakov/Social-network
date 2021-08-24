"""
Модуль для шаблонов адресов (Uniform Resource Locator – URL).
Каждый URL, определенный в этом модуле, будет связан со своим представлением из модуля  '.views'. ;
"""

from django.urls import path
from . import views

urlpatterns = [  # Обработчики действий со статьями.
    path("login/", views.user_login, name="login"),  # Страничка авторизации
]
