from games.entrapment.player import EntrapmentPlayer
from games.entrapment.state import EntrapmentState
from games.game_simulator import GameSimulator


class EntrapmentSimulator(GameSimulator):

    def __init__(self, player1: EntrapmentPlayer, player2: EntrapmentPlayer, num_rows: int = 7, num_cols: int = 7):
        super(EntrapmentSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return EntrapmentState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: EntrapmentState):
        # ignored for this simulator
        pass

    def end_game(self, state: EntrapmentState):
        # ignored for this simulator
        pass
