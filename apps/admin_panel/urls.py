from django.urls import path , re_path
from .views import admin
urlpatterns = [
    re_path(r'/',admin)
]