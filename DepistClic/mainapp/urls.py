from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='depistclic-home'),
    path('questions/', views.questions, name='depistclic-questions'),
]
