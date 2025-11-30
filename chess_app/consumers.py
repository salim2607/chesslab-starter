import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Game, Move

class GameConsumer(WebsocketConsumer):
    """
    TODO 3.3 & 4.1: CONSUMER WEBSOCKET - À COMPLÉTER
    """
    
    def connect(self):
        """
        TODO 3.4: MÉTHODE CONNECT - À COMPLÉTER
        """
        # TODO: Récupérer l'ID de partie
        self.game_id = None  # À compléter
        
        # TODO: Créer le nom du groupe
        self.game_group_name = None  # À compléter

        # TODO: Rejoindre le groupe
        # À compléter...
        
        # TODO: Accepter la connexion
        # À compléter...

    def disconnect(self, close_code):
        """
        TODO 3.5: MÉTHODE DISCONNECT - À COMPLÉTER
        """
        # TODO: Quitter le groupe
        # À compléter...

    def receive(self, text_data):
        """
        TODO 4.1: MÉTHODE RECEIVE - À COMPLÉTER
        """
        try:
            # TODO: Parser le JSON
            data = None  # À compléter
            
            # TODO: Extraire le type de message
            message_type = None  # À compléter
            
            # TODO: Router selon le type
            if message_type == 'move':
                pass  # À compléter
            elif message_type == 'join_game':
                pass  # À compléter
            elif message_type == 'resign':
                pass  # À compléter
                
        except Exception as e:
            # TODO: Gérer l'erreur
            pass

    def handle_move(self, data):
        
        try:
            game = Game.objects.get(id=self.game_id)
            
            user = self.scope['user']
            
            if (game.current_turn == 'white' and game.white_player == user) or \
            (game.current_turn == 'black' and game.black_player == user):
                
                Move.objects.create(
                    game=game,
                    player=user,
                    move_number=game.moves.count() + 1,
                    piece=data.get('piece', 'P'),
                    from_square=data['from'],
                    to_square=data['to']
                )

                game.current_turn = 'black' if game.current_turn == 'white' else 'white'
                
                fen = data.get('fen')
                if fen:
                    game.board_state = fen
                game.save()

                async_to_sync(self.channel_layer.group_send)(
                    self.game_group_name,
                    {
                        'type': 'move_message',
                        'move': {
                            'from': data['from'],
                            'to': data['to'],
                            'piece': data.get('piece', 'P'),
                            'player': user.username,
                        }
                    }
                )
            else:
                
                self.send(text_data=json.dumps({
                    'type': 'error',
                    'message': 'Ce n\'est pas votre tour'
                }))
                
        except Exception as e:
            print(f" Erreur handle_move: {str(e)}")
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': f'Erreur lors du mouvement: {str(e)}'
            }))

    def handle_join(self):
        user = self.scope['user']
        async_to_sync(self.channel_layer.group_send)(
            self.game_group_name,
            {
                'type': 'game_update_message',
                'message': f'{user.username} a rejoint la partie'
            }
        )


    
    def handle_resign(self):
        try:
            
            game = Game.objects.get(id=self.game_id)
            user = self.scope['user']
            
            
            if game.white_player == user:
                winner = game.black_player
            elif game.black_player == user:
                winner = game.white_player
            else:
                return  
            
            
            game.status = 'finished'
            game.save()
            
            
            async_to_sync(self.channel_layer.group_send)(
                self.game_group_name,
                {
                    'type': 'game_update_message',
                    'message': f'{user.username} a abandonné. {winner.username if winner else "L\'adversaire"} gagne!'
                }
            )
            
        except Exception as e:
            print(f" Erreur handle_resign: {str(e)}")

    def move_message(self, event):
        
        move = event['move']
        self.send(text_data=json.dumps({
            'type': 'move',
            'from': move['from'],
            'to': move['to'],
            'piece': move['piece'],
            'player': move['player'],
        }))

    def game_update_message(self, event):
        self.send(text_data=json.dumps({
            'type': 'game_update',
            'message': event['message']
        }))

