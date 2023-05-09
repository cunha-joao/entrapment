from games.entrapment.player import EntrapmentPlayer
from games.entrapment.state import EntrapmentState
from games.game_simulator import GameSimulator

class EntrapmentSimulator(GameSimulator):

    #def __init__(self, player1: EntrapmentPlayer, player2: EntrapmentPlayer, num_rows: int = 7, num_cols: int = 7):
     #   super(EntrapmentSimulator, self).__init__([player1, player2])

    #def __init__(self, player1, player2, num_rows, num_cols, difficulty):

    def __init__(self, player1, player2, difficulty, num_rows=None, num_cols=None):
        super().__init__([player1, player2])
        self._player1 = player1
        self._player2 = player2
        self._difficulty = difficulty
        self._num_rows = num_rows
        self._num_cols = num_cols

        #super().__init__(player1, player2, difficulty)
        """
        the number of rows and cols from the grid
        """
        #self.__num_rows = num_rows
        #self.__num_cols = num_cols

    def init_game(self):
        num_rows = int(self._num_rows) if self._num_rows else 7
        num_cols = int(self._num_cols) if self._num_cols else 7
        return EntrapmentState(num_rows, num_cols)
        #return EntrapmentState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: EntrapmentState):
        # ignored for this simulator
        pass

    def end_game(self, state: EntrapmentState):
        # ignored for this simulator
        pass

#def run(self, difficulty: str):
 #       """
  #      Runs the game until there is a winner or a draw.
   #     """
    #    current_player = self.players[0]
     #   while not self.result:
      #      if current_player.__class__.__name__ == 'HumanEntrapmentPlayer':
       #         move = current_player.get_move(copy.deepcopy(self.state), self.__num_rows, self.__num_cols)
        #    else:
         #       move = current_player.get_move(copy.deepcopy(self.state), difficulty)
          #  self.state = self.state.apply_move(move, current_player.color)
           # self.print_board()
            #self.check_for_winner()
            #if not self.result:
             #   current_player = self.players[(self.players.index(current_player) + 1) % 2]
             
#def run(self, difficulty: str):
def run(self):
    """
    Runs the game until there is a winner or a draw.
    """
    current_player = self.players[0]
    while not self.result:
        if isinstance(current_player, HumanEntrapmentPlayer):
            move = current_player.get_move(copy.deepcopy(self.state), self._num_rows, self._num_cols)
        else:
            move = current_player.get_move(copy.deepcopy(self.state), self._difficulty)
        if move is not None and self.state.validate_action(move):
            self.state = self.state.apply_move(move, current_player.color)
            self.print_board()
            self.check_for_winner()
            
        if not self.result:
            current_player = self.players[(self.players.index(current_player) + 1) % 2]







   
