from games.entrapment.action import EntrapmentAction
from games.entrapment.player import EntrapmentPlayer
from games.entrapment.state import EntrapmentState


class HumanEntrapmentPlayer(EntrapmentPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: EntrapmentState):
        state.display()

        while True:
            # noinspection PyBroadException
            try:
                if state.check_stage() != 1:
                    print(f"Player {state.get_acting_player()}, choose a column: ")
                    col = int(input())
                    print(f"Player {state.get_acting_player()}, choose a row: ")
                    row = int(input())
                    new_col = 0
                    new_row = 0
                    wall_col = 0
                    wall_row = 0
                    m_type = 0
                    return EntrapmentAction(col, row, new_col, new_row, wall_col, wall_row, m_type)
                else:
                    print("1 - Move two pieces")
                    print("2 - Move one piece and place a wall")
                    print(f"Player {state.get_acting_player()}, choose you next move:")
                    m_type = int(input())

                    if m_type == 1:
                        for i in range(0, 1):
                            print(f"Player {state.get_acting_player()}, choose the column "
                                  f"with the roamer you wish to move: ")
                            col = int(input())
                            print(f"Player {state.get_acting_player()}, choose the row "
                                  f"with the roamer you wish to move: ")
                            row = int(input())
                            print(f"Player {state.get_acting_player()}, choose the new column "
                                  f"for the roamer: ")
                            new_col = int(input())
                            print(f"Player {state.get_acting_player()}, choose the new row "
                                  f"for the roamer: ")
                            new_row = int(input())
                            wall_col = 0
                            wall_row = 0
                            return EntrapmentAction(col, row, new_col, new_row, wall_col, wall_row, m_type)

                    elif m_type == 2:
                        print(f"Player {state.get_acting_player()}, choose the column with the roamer you wish to move: ")
                        col = int(input())
                        print(f"Player {state.get_acting_player()}, choose the row with the roamer you wish to move: ")
                        row = int(input())
                        print(f"Player {state.get_acting_player()}, choose the new column for the roamer: ")
                        new_col = int(input())
                        print(f"Player {state.get_acting_player()}, choose the new row for the roamer: ")
                        new_row = int(input())
                        print(f"Player {state.get_acting_player()}, choose a column to place a wall: ")
                        wall_col = int(input())
                        print(f"Player {state.get_acting_player()}, choose a row to place a wall: ")
                        wall_row = int(input())
                        return EntrapmentAction(col, row, new_col, new_row, wall_col, wall_row, m_type)
                    else:
                        print("Please choose one of the options below!")
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: EntrapmentState):
        # ignore
        pass

    def event_end_game(self, final_state: EntrapmentState):
        # ignore
        pass
