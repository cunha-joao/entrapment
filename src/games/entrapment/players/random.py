from random import randint

from games.entrapment.action import EntrapmentAction
from games.entrapment.player import EntrapmentPlayer
from games.entrapment.state import EntrapmentState
from games.state import State


class RandomEntrapmentPlayer(EntrapmentPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: EntrapmentState):
        # This player only places the 3 roamers in random positions and then places walls randomly across the board
        while True:
            if state.check_stage() != 1:
                new_col = 0
                new_row = 0
                wall_col = 0
                wall_row = 0
                m_type = 0
                return EntrapmentAction(randint(0, state.get_num_cols()), randint(0, state.get_num_rows()), new_col,
                                        new_row, wall_col, wall_row, m_type)
            else:
                m_type = 2
                col = 0
                row = 0
                new_col = 0
                new_row = 0
                return EntrapmentAction(col, row, new_col, new_row, randint(0, state.get_num_cols()),
                                        randint(0, state.get_num_cols()), m_type)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
