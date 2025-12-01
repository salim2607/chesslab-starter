from django.urls import path
from . import views

app_name = 'chess_app'

# SOLUTION 2.5: URLS APPLICATION - COMPLÈTE
# Configuration des URLs de l'application chess_app

urlpatterns = [
    # Page d'accueil - URL: http://127.0.0.1:8000/
    path('', views.home, name='home'),
    
    # Création de partie - URL: http://127.0.0.1:8000/game/new/
    path('game/new/', views.create_game, name='create_game'),
    
    # Page de jeu principale - URL: http://127.0.0.1:8000/game/1/
    path('game/<int:game_id>/', views.play_game, name='play_game'),
    
    # Rejoindre une partie - URL: http://127.0.0.1:8000/game/1/join/white/
    path('game/<int:game_id>/join/<str:color>/', views.join_game, name='join_game'),
    
    # BONUS - Joueurs en ligne - URL: http://127.0.0.1:8000/players/
    path('players/', views.online_players, name='online_players'),
]