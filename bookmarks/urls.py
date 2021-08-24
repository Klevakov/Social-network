"""
bookmarks URL Configuration
The `urlpatterns` list routes URLs to views.
"""

from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
]
