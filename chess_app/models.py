from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    """
     MODÈLE GAME - COMPLET
    Représente une partie d'échecs complète avec deux joueurs
    """
    
    # CHOIX POUR LES CHAMPS
    STATUS_CHOICES = [
        ('waiting', 'En attente'),    # En attente de joueurs
        ('active', 'En cours'),       # Partie en cours
        ('finished', 'Terminée'),     # Partie terminée
    ]
    
    TURN_CHOICES = [
        ('white', 'Blanc'),           # Tour des blancs
        ('black', 'Noir'),            # Tour des noirs
    ]
    
    # CHAMPS DU MODÈLE
    
    # Joueur blanc - peut être vide (partie en attente)
    white_player = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,    # Si user supprimé, garde la partie
        null=True,                    # Peut être NULL
        blank=True,                   # Peut être laissé vide
        related_name='games_as_white' # user.games_as_white.all()
    )
    
    # Joueur noir - peut être vide (partie en attente)
    black_player = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='games_as_black' # user.games_as_black.all()
    )
    
    # Statut de la partie (waiting/active/finished)
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES,       # Limite aux choix définis
        default='waiting'             # Par défaut en attente
    )
    
    # Tour actuel (white/black)
    current_turn = models.CharField(
        max_length=5, 
        choices=TURN_CHOICES, 
        default='white'               # Les blancs commencent toujours
    )
    
    # État du plateau en notation FEN
    board_state = models.TextField(
        default='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        help_text='Position du plateau en notation FEN'
    )
    
    # Timestamps automatiques
    created_at = models.DateTimeField(auto_now_add=True)  # Date création
    updated_at = models.DateTimeField(auto_now=True)      # Date modification
    
    class Meta:
        """Configuration de la classe"""
        ordering = ['-created_at']  # Plus récent en premier
    
    def __str__(self):
        """Représentation textuelle de l'objet"""
        return f"Partie #{self.id} - {self.get_status_display()}"
    
    def get_absolute_url(self):
        """URL pour accéder à cette partie"""
        from django.urls import reverse
        return reverse('chess_app:play_game', kwargs={'game_id': self.id})


class Move(models.Model):
    """
    TODO 1.2: MODÈLE MOVE - À COMPLÉTER
    Représente un coup joué dans une partie d'échecs
    """
    
    # TODO: Définir les champs du modèle
    # game (ForeignKey vers Game)
    game = models.ForeignKey(
        Game, 
        on_delete=models.CASCADE,   
        related_name='moves'          
    )

    # player (ForeignKey vers User)

    # move_number (IntegerField)

    # piece (CharField)

    # from_square (CharField)

    # to_square (CharField)

    # timestamp (DateTimeField)

    
    """
    class Meta:
    
        ordering = ['move_number']  # Trier par ordre chronologique
    
    def __str__(self):
    
        return f"{self.move_number}. {self.piece}{self.to_square}"

    """