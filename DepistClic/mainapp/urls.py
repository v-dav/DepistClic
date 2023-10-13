from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='depistclic-home'),
    path('questions/', views.get_question, name='depistclic-questions'),
    path('questions/<int:question_id>/', views.get_question, name='depistclic-get_question'),
    path('synthese/', views.synthese, name="depistclic-synthese"),
    path('store_value/', views.store_value, name='store_value'),
]
