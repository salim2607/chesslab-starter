from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Game, User

def home(request):   
    # Récupérer les parties en attente
    waiting_games = Game.objects.filter(status='waiting')
    
    # Récupérer les parties actives
    active_games = Game.objects.filter(status='active')
    
    context = {
        'waiting_games': waiting_games,
        'active_games': active_games,
    }
    return render(request, 'chess_app/home.html', context)


@login_required
def create_game(request):
    """
    TODO 2.2: VUE CREATE_GAME - À COMPLÉTER
    Créer une nouvelle partie et rediriger vers le plateau
    """
    # TODO: Créer une nouvelle partie
    game = None  # À compléter
    
    # TODO: Rediriger vers la page de jeu
    return redirect('')  # À compléter

def play_game(request, game_id):
    # Récupérer la partie ou retourner 404
    game = get_object_or_404(Game, id=game_id)
    
    # Déterminer le rôle de l'utilisateur
    user_role = 'spectator'
    if request.user.is_authenticated:
        if game.white_player == request.user:
            user_role = 'white'
        elif game.black_player == request.user:
            user_role = 'black'
        elif not game.white_player:
            user_role = 'available_white'
        elif not game.black_player:
            user_role = 'available_black'
    
    # Déterminer si c'est le tour de l'utilisateur
    is_my_turn = False
    if user_role in ['white', 'black']:
        if (user_role == 'white' and game.current_turn == 'white') or \
           (user_role == 'black' and game.current_turn == 'black'):
            is_my_turn = True
    
    # Construire l'URL WebSocket
    websocket_url = f"ws://{request.get_host()}/ws/game/{game.id}/"
    
    context = {
        'game': game,
        'user_role': user_role,
        'is_my_turn': is_my_turn,
        'websocket_url': websocket_url,
    }
    return render(request, 'chess_app/play_game.html', context)

@login_required
def join_game(request, game_id, color):
    """
    TODO 2.4: VUE JOIN_GAME - À COMPLÉTER
    Rejoindre une partie existante comme blanc ou noir
    """
    # TODO: Récupérer la partie
    game = None  # À compléter
    user = None  # À compléter
    # TODO: Assigner le joueur selon la couleur
    if color == 'white' and not game.white_player:
        # TODO: Assigner le joueur blanc
        pass  # À compléter
        # TODO: Vérifier si la partie peut devenir active
        pass  # À compléter
        
    elif color == 'black' and not game.black_player:
        # TODO: Assigner le joueur noir
        pass  # À compléter
        # TODO: Vérifier si la partie peut devenir active
        pass  # À compléter
    
    # Sauvegarder la partie
    game.save()
    
    # TODO: Rediriger vers la page de jeu
    return redirect('')  # À compléter

def online_players(request):
    """
    BONUS: Page des joueurs en ligne
    """
    players = User.objects.filter(is_active=True)
    return render(request, 'chess_app/online_players.html', {'players': players})