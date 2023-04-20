from random import randint

from games.entrapment.action import EntrapmentAction
from games.entrapment.player import EntrapmentPlayer
from games.entrapment.state import EntrapmentState
from games.state import State


class RandomEntrapmentPlayer(EntrapmentPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: EntrapmentState):
        return EntrapmentAction(randint(0, state.get_num_cols()), randint(0, state.get_num_rows()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
