from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='depistclic-home'),
    path('questions/', views.get_question, name='depistclic-questions'),
    path('questions/<int:question_order>/', views.get_question,
         name='depistclic-get_question'),
    path('synthese/', views.synthese, name="depistclic-synthese"),
    path('comment/', views.comment_page, name="depistclic-comment"),
    path('mentions/', views.mentions_legales, name="depistclic-mentions"),
    path('politique/', views.politique_de_confidentialite, name="depistclic-politique"),
    path('cookies/', views.politique_de_cookies, name="depistclic-cookies"),
    path('equipe/', views.equipe, name="depistclic-equipe"),
    path('outils/', views.outils, name="depistclic-outils"),
]
