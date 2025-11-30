from django.contrib import admin
from .models import Game, Move

"""
class MoveInline(admin.TabularInline):
    
    model = Move
    extra = 0
    readonly_fields = ['timestamp']  # Correct - le champ existe dans le modèle Move


@admin.register(Game)
class GameAdmin(admin.ModelAdmin): 
    list_display = ['id', 'white_player', 'black_player', 'status', 'current_turn', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['white_player__username', 'black_player__username']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [MoveInline]

"""


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    """
    TODO 1.6: ADMIN MOVE - À COMPLÉTER
    """
    # TODO: Définir les colonnes à afficher
    list_display = []  # À compléter
    
    # TODO: Ajouter des filtres
    list_filter = []  # À compléter
    
    # TODO: Ajouter la recherche
    search_fields = []  # À compléter
    
    # TODO: Définir les champs en lecture seule
    readonly_fields = []  # À compléter