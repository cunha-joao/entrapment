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
                    x = int(input())
                    print(f"Player {state.get_acting_player()}, choose a row: ")
                    y = int(input())
                    return EntrapmentAction(x, y)
                else:
                    print("1 - Move two pieces")
                    print("2 - Move one piece and place a wall")
                    print(f"Player {state.get_acting_player()}, choose you next move:")
                    choice = int(input())

                    if choice == 1:
                        for i in range(1, 2):
                            print(f"Player {state.get_acting_player()}, choose a column"
                                  f"(with the roamer you wish to move): ")
                            x = int(input())
                            print(f"Player {state.get_acting_player()}, choose a row"
                                  f"(with the roamer you wish to move): ")
                            y = int(input())
                            return EntrapmentAction(x, y)

                    elif choice == 2:
                        print(f"Player {state.get_acting_player()}, choose a column (with the roamer you wish to move): ")
                        x = int(input())
                        print(f"Player {state.get_acting_player()}, choose a row (with the roamer you wish to move): ")
                        y = int(input())
                        print(f"Player {state.get_acting_player()}, choose a column: ")
                        x_wall = int(input())
                        print(f"Player {state.get_acting_player()}, choose a row: ")
                        y_wall = int(input())
                        return EntrapmentAction(x, y, x_wall, y_wall)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: EntrapmentState):
        # ignore
        pass

    def event_end_game(self, final_state: EntrapmentState):
        # ignore
        pass
