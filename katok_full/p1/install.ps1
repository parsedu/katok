# ==========================================
# НАСТРОЙКИ СКРИПТА
# ==========================================
$ErrorActionPreference = "Stop" # Останавливать скрипт при любой ошибке

Write-Host "=== STARTING PROJECT SETUP: Bookmarks ===" -ForegroundColor Green

# ==========================================
# 1. ПОИСК PYTHON И СОЗДАНИЕ VENV
# ==========================================

# Проверяем наличие py (Python Launcher) или python
if (Get-Command "py" -ErrorAction SilentlyContinue) {
    $SysPython = "py"
    Write-Host "--> Detected Python Launcher: 'py'" -ForegroundColor Gray
} elseif (Get-Command "python" -ErrorAction SilentlyContinue) {
    $SysPython = "python"
    Write-Host "--> Detected standard Python: 'python'" -ForegroundColor Gray
} else {
    Write-Error "CRITICAL ERROR: Python not found! Please install Python from python.org."
    exit 1
}

Write-Host "--> Creating virtual environment (env)..." -ForegroundColor Cyan
# Удаляем старое, если есть, чтобы не было конфликтов
if (Test-Path "env") { Remove-Item "env" -Recurse -Force }

# Создаем venv используя системный python
try {
    & $SysPython -m venv env
} catch {
    Write-Error "Failed to create virtual environment. Error: $_"
    exit 1
}

# Путь к python внутри виртуального окружения
$VenvPy = ".\env\Scripts\python.exe"

# Проверяем, создался ли python.exe
if (-not (Test-Path $VenvPy)) {
    Write-Error "CRITICAL ERROR: Virtual environment created, but '$VenvPy' is missing."
    exit 1
}

# ==========================================
# 2. УСТАНОВКА ЗАВИСИМОСТЕЙ
# ==========================================
Write-Host "--> Upgrading pip and installing Django/Pillow..." -ForegroundColor Cyan
& $VenvPy -m pip install --upgrade pip
& $VenvPy -m pip install "Django~=4.1.0" Pillow

# ==========================================
# 3. СОЗДАНИЕ ПРОЕКТА DJANGO
# ==========================================
Write-Host "--> Creating Django project 'bookmarks'..." -ForegroundColor Cyan
if (Test-Path "bookmarks") { Remove-Item "bookmarks" -Recurse -Force }

# Создаем проект в текущей папке (.)
& $VenvPy -m django startproject bookmarks .

if (-not (Test-Path "bookmarks\settings.py")) {
    Write-Error "Django project creation failed. 'bookmarks\settings.py' not found."
    exit 1
}

# ==========================================
# 4. СОЗДАНИЕ ПРИЛОЖЕНИЯ ACCOUNT
# ==========================================
Write-Host "--> Creating app 'account'..." -ForegroundColor Cyan
& $VenvPy manage.py startapp account

# ==========================================
# 5. СОЗДАНИЕ СТРУКТУРЫ ПАПОК
# ==========================================
Write-Host "--> Creating directories..." -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path "account\templates\account" | Out-Null
New-Item -ItemType Directory -Force -Path "account\templates\registration" | Out-Null
New-Item -ItemType Directory -Force -Path "account\static\css" | Out-Null
New-Item -ItemType Directory -Force -Path "media\users" | Out-Null

# ============================================================
# 6. ЗАПИСЬ ФАЙЛОВ (Here-Strings)
# ============================================================

Write-Host "--> Writing configuration files..." -ForegroundColor Cyan

# --- settings.py ---
$settings = @"
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-setup-script-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarks.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

# Auth settings
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# Email settings (console for dev)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Media settings
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
"@
Set-Content -Path "bookmarks\settings.py" -Value $settings -Encoding UTF8

# --- bookmarks/urls.py ---
$projUrls = @"
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"@
Set-Content -Path "bookmarks\urls.py" -Value $projUrls -Encoding UTF8

# --- account/models.py ---
$models = @"
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
"@
Set-Content -Path "account\models.py" -Value $models -Encoding UTF8

# --- account/admin.py ---
$admin = @"
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
"@
Set-Content -Path "account\admin.py" -Value $admin -Encoding UTF8

# --- account/forms.py ---
$forms = @"
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
"@
Set-Content -Path "account\forms.py" -Value $forms -Encoding UTF8

# --- account/views.py ---
$views = @"
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'account/edit.html', {
        'user_form': user_form, 
        'profile_form': profile_form
    })
"@
Set-Content -Path "account\views.py" -Value $views -Encoding UTF8

# --- account/urls.py ---
$accUrls = @"
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
"@
Set-Content -Path "account\urls.py" -Value $accUrls -Encoding UTF8

# --- base.html ---
$baseHtml = @"
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <link href='{% static "css/base.css" %}' rel='stylesheet'>
</head>
<body>
    <div id="header">
        <span class="logo">Bookmarks</span>
        {% if request.user.is_authenticated %}
        <ul class="menu">
            <li {% if section == "dashboard" %}class="selected"{% endif %}>
                <a href="{% url "dashboard" %}">My dashboard</a>
            </li>
            <li {% if section == "images" %}class="selected"{% endif %}>
                <a href="#">Images</a>
            </li>
            <li {% if section == "people" %}class="selected"{% endif %}>
                <a href="#">People</a>
            </li>
        </ul>
        {% endif %}

        <span class="user">
        {% if request.user.is_authenticated %}
            Hello {{ request.user.first_name|default:request.user.username }},
            <a href="{% url "logout" %}">Logout</a>
        {% else %}
            <a href="{% url "login" %}">Log-in</a>
        {% endif %}
        </span>
    </div>
    
    {% if messages %}
        <ul class="messages">
            {% for message in messages %}
                <li class="{{ message.tags }}">
                    {{ message|safe }}
                    <a href="#" class="close">x</a>
                </li>
            {% endfor %}
        </ul>
    {% endif %}

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"@
Set-Content -Path "account\templates\base.html" -Value $baseHtml -Encoding UTF8

# --- login.html ---
$loginHtml = @"
{% extends "base.html" %}
{% block title %}Log-in{% endblock %}
{% block content %}
    <h1>Log-in</h1>
    {% if form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    {% else %}
        <p>Please, use the following form to log-in:</p>
    {% endif %}
    
    <div class="login-form">
        <form action="{% url 'login' %}" method="post">
            {{ form.as_p }}
            {% csrf_token %}
            <input type="hidden" name="next" value="{{ next }}" />
            <p><input type="submit" value="Log-in"></p>
        </form>
        <p>Forgot your password? <a href="{% url 'password_reset' %}">Reset it here</a>.</p>
        <p>Don't have an account? <a href="{% url 'register' %}">Register here</a>.</p>
    </div>
{% endblock %}
"@
Set-Content -Path "account\templates\registration\login.html" -Value $loginHtml -Encoding UTF8

# --- dashboard.html ---
$dashHtml = @"
{% extends "base.html" %}
{% block title %}Dashboard{% endblock %}
{% block content %}
    <h1>Dashboard</h1>
    <p>Welcome to your dashboard. You can <a href="{% url 'edit' %}">edit your profile</a> or <a href="{% url 'password_change' %}">change your password</a>.</p>
{% endblock %}
"@
Set-Content -Path "account\templates\account\dashboard.html" -Value $dashHtml -Encoding UTF8

# --- register.html ---
$regHtml = @"
{% extends "base.html" %}
{% block title %}Create an account{% endblock %}
{% block content %}
    <h1>Create an account</h1>
    <p>Please, sign up using the following form:</p>
    <form method="post">
        {{ user_form.as_p }}
        {% csrf_token %}
        <p><input type="submit" value="Create my account"></p>
    </form>
{% endblock %}
"@
Set-Content -Path "account\templates\account\register.html" -Value $regHtml -Encoding UTF8

# --- edit.html ---
$editHtml = @"
{% extends "base.html" %}
{% block title %}Edit your account{% endblock %}
{% block content %}
    <h1>Edit your account</h1>
    <p>You can edit your account using the following form:</p>
    <form method="post" enctype="multipart/form-data">
        {{ user_form.as_p }}
        {{ profile_form.as_p }}
        {% csrf_token %}
        <p><input type="submit" value="Save changes"></p>
    </form>
{% endblock %}
"@
Set-Content -Path "account\templates\account\edit.html" -Value $editHtml -Encoding UTF8

# --- register_done.html ---
$regDoneHtml = @"
{% extends "base.html" %}
{% block title %}Welcome{% endblock %}
{% block content %}
    <h1>Welcome {{ new_user.first_name }}!</h1>
    <p>Your account has been successfully created. Now you can <a href="{% url 'login' %}">log in</a>.</p>
{% endblock %}
"@
Set-Content -Path "account\templates\account\register_done.html" -Value $regDoneHtml -Encoding UTF8

# --- logged_out.html ---
$logoutHtml = @"
{% extends "base.html" %}
{% block title %}Logged out{% endblock %}
{% block content %}
    <h1>Logged out</h1>
    <p>You have been successfully logged out.</p>
    <p>You can <a href="{% url 'login' %}">log-in again</a>.</p>
{% endblock %}
"@
Set-Content -Path "account\templates\registration\logged_out.html" -Value $logoutHtml -Encoding UTF8

# --- base.css ---
$css = @"
body { font-family: sans-serif; margin: 0; padding: 0; }
#header { background-color: #41b883; padding: 10px 20px; color: white; overflow: hidden; }
#header .logo { font-weight: bold; font-size: 1.2em; float: left; margin-right: 20px; }
#header .menu { float: left; list-style: none; margin: 0; padding: 0; }
#header .menu li { display: inline; margin-right: 10px; font-weight: bold; }
#header .menu li.selected a { color: white; text-decoration: none; }
#header .menu li a { color: #2c3e50; text-decoration: none; }
#header .user { float: right; }
#header a { color: white; }
#content { padding: 20px; }
ul.messages { list-style: none; padding: 0; margin: 0; }
ul.messages li { padding: 10px; margin-bottom: 10px; }
ul.messages li.success { background-color: #b8e994; color: #009432; }
ul.messages li.error { background-color: #ffb8b8; color: #b33939; }
label { float: left; width: 120px; clear: left; }
input, textarea { margin-bottom: 10px; }
input[type=submit] { background-color: #41b883; color: white; border: none; padding: 10px 20px; cursor: pointer; }
"@
Set-Content -Path "account\static\css\base.css" -Value $css -Encoding UTF8

# --- Заглушки для шаблонов сброса/смены пароля ---
$stub = "{% extends 'base.html' %}{% block content %}<h1>Form</h1><form method='post'>{{ form.as_p }}{% csrf_token %}<p><input type='submit'></p></form>{% endblock %}"
Set-Content "account\templates\registration\password_change_form.html" $stub -Encoding UTF8
Set-Content "account\templates\registration\password_reset_form.html" $stub -Encoding UTF8
Set-Content "account\templates\registration\password_reset_confirm.html" $stub -Encoding UTF8

$stubText = "{% extends 'base.html' %}{% block content %}<h1>Success</h1><p>Action completed.</p>{% endblock %}"
Set-Content "account\templates\registration\password_change_done.html" $stubText -Encoding UTF8
Set-Content "account\templates\registration\password_reset_done.html" $stubText -Encoding UTF8
Set-Content "account\templates\registration\password_reset_complete.html" $stubText -Encoding UTF8

Set-Content "account\templates\registration\password_reset_email.html" "Reset link: {{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}" -Encoding UTF8

# ==========================================
# 7. МИГРАЦИИ И ФИНАЛИЗАЦИЯ
# ==========================================
Write-Host "--> Running migrations..." -ForegroundColor Cyan
& $VenvPy manage.py makemigrations
& $VenvPy manage.py migrate

Write-Host "=== DONE! ===" -ForegroundColor Green
Write-Host "To run the server:"
Write-Host "1. .\env\Scripts\activate"
Write-Host "2. cd bookmarks"
Write-Host "3. python manage.py runserver"