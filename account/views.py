"""
Модуль, содержащий представления.
Представление – это функция Python, которая принимает Web-запрос и возвращает Web-ответ.
"""
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


from .forms import LoginForm


def user_login(request):  # pylint: disable=inconsistent-return-statements
    """
    Функция-представление - обработчик авторизации.
    При получении GET запроса - возвращает пустую форум авторизации.
    При получении POST запроса - проводит аутентификацию и авторизацию на сайте.
    """
    # pylint: disable=no-else-return

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  # pylint: disable=invalid-name
            username = cd["username"]
            password = cd["password"]
            try:
                User.objects.get(username=username)
            except ObjectDoesNotExist:
                return HttpResponse("The username you have entered does not exist.")
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse("Authenticated successfully")
                    else:
                        return HttpResponse("Disabled account")
                else:
                    return HttpResponse("Invalid password. Try again.")
    else:
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})
