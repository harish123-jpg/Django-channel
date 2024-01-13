from django.urls import path

from .views import messages_page

urlpatterns = [
    path('chat/', messages_page, name='home')
]
