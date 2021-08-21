from django import forms


class LoginForm(forms.Form):
    """Создает форму для авторизации пользователя через имя пользователя и пароль. """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
