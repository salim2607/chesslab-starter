from django.contrib import admin
from .models import Game, Move

class MoveInline(admin.TabularInline):
    """
    SOLUTION 1.4: INLINE POUR LES COUPS - CORRIGÉ
    """
    model = Move
    extra = 0
    readonly_fields = ['timestamp']  

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """
    SOLUTION 1.5: ADMIN GAME - CORRIGÉ
    """
    list_display = ['id', 'white_player', 'black_player', 'status', 'current_turn', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['white_player__username', 'black_player__username']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [MoveInline]


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    """
    SOLUTION 1.6: ADMIN MOVE - CORRIGÉ
    Les erreurs étaient :
    - 'created_at' n'existe pas dans Move → utiliser 'timestamp'
    - 'id' dans list_display n'est pas nécessaire (affiché par défaut)
    """
    # CORRECTION : Utiliser 'timestamp' au lieu de 'created_at'
    list_display = ['game', 'player', 'piece', 'from_square', 'to_square', 'move_number', 'timestamp']
    
    # CORRECTION : Utiliser 'timestamp' au lieu de 'created_at'
    list_filter = ['game', 'player', 'timestamp']
    
    search_fields = ['player__username', 'game__id']
    
    # CORRECTION : Utiliser 'timestamp' au lieu de 'created_at'
    readonly_fields = ['timestamp']