from django.urls import path

from .views import home

urlpatterns = [
    path('ss', home, name='home')
]
