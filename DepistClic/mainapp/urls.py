from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='depistclic-home'),
    path('questions/', views.get_question, name='depistclic-questions'),
    path('questions/<int:question_order>/', views.get_question,
         name='depistclic-get_question'),
    path('synthese/', views.synthese, name="depistclic-synthese"),
    path('contact/', views.contact, name="depistclic-contact"),
    path('comment/', views.comment_page, name="depistclic-comment"),
    path('team/', views.team, name="depistclic-team"),
    path('mission/', views.mission, name="depistclic-mission"),
    path('pdf/', views.get_pdf, name='depistclic-pdf')
]
