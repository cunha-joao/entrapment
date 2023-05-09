from typing import Optional

from games.entrapment.action import EntrapmentAction
from games.entrapment.result import EntrapmentResult
from games.state import State


class EntrapmentState(State):
    EMPTY_CELL = -1

    def __init__(self, num_rows: int = 7, num_cols: int = 7):
        super().__init__()

        if num_rows < 7:
            raise Exception("the number of rows must be 7 or over")
        if num_cols < 6:
            raise Exception("the number of rows must be 6 or over")

        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_rows

        """
        the grid
        """
        self.__grid = [[EntrapmentState.EMPTY_CELL for _i in range(self.__num_rows)] for _j in range(self.__num_cols)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 3 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 2):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player:
                    return True

        # check for 3 up and down
        for row in range(0, self.__num_rows - 2):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player:
                    return True

        # check upward diagonal
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 2):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 2):
            for col in range(0, self.__num_cols - 2):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player:
                    return True
        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: EntrapmentAction) -> bool:
        col = action.get_col()
        row = action.get_row()
        new_col = action.get_new_col()
        new_row = action.get_new_row()
        wall_col = action.get_wall_col()
        wall_row = action.get_wall_row()

        # valid column
        if col < 0 or col >= self.__num_cols:
            print("Invalid column!")
            return False
        # valid row
        if row < 0 or row >= self.__num_rows:
            print("Invalid row!")
            return False

        # valid new column
        if new_col < 0 or new_col >= self.__num_cols:
            print("Invalid new column!")
            return False
        # valid new row
        if new_row < 0 or new_row >= self.__num_rows:
            print("Invalid new row!")
            return False

        # valid wall column
        if wall_col < 0 or wall_col >= self.__num_cols:
            print("Invalid column!")
            return False
        # valid wall row
        if wall_row < 0 or wall_row >= self.__num_rows:
            print("Invalid row!")
            return False

        # each roamer can only move one house at a time
        if new_col > (col + 1):
            print("Invalid new column! (can only move one house at a time)")
            return False
        if new_row > (row + 1):
            print("Invalid new row! (can only move one house at a time)")
            return False

        return True

    # check the stage of the game (initial stage where the players place their three roamers or playing stage, where the
    # players make their moves)
    def check_stage(self):
        if self.__turns_count > 6:
            stage = 1
            return stage

    def update(self, action: EntrapmentAction):
        col = action.get_col()
        row = action.get_row()
        new_col = action.get_new_col()
        new_row = action.get_new_row()
        wall_col = action.get_wall_col()
        wall_row = action.get_wall_row()
        move_type = action.get_move_type()

        # place roamers in the initial stage
        if move_type == 0:
            if self.__grid[row][col] < 0:
                self.__grid[row][col] = self.__acting_player

        # change two roamers positions
        if move_type == 1:
            if self.check_stage() == 1:
                if self.__grid[row][col] == self.get_acting_player():
                    self.__grid[new_row][new_col] = self.get_acting_player()
                    self.__grid[row][col] = EntrapmentState.EMPTY_CELL

        # place walls
        if move_type == 2:
            if self.check_stage() == 1:
                if self.__grid[row][col] == self.get_acting_player():
                    self.__grid[new_row][new_col] = self.get_acting_player()
                    self.__grid[row][col] = EntrapmentState.EMPTY_CELL
            if self.__grid[wall_row][wall_col] < 0:
                if self.__acting_player == 0:
                    wall_ref = 3
                    self.__grid[wall_row][wall_col] = wall_ref
                elif self.__acting_player == 1:
                    wall_ref = 2
                    self.__grid[wall_row][wall_col] = wall_ref

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: 'R ',
                  1: 'B ',
                  2: 'BW',
                  3: 'RW',
                  EntrapmentState.EMPTY_CELL: '  '
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end=" ")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()

        for row in range(0, self.__num_rows):
            print('|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = EntrapmentState(self.__num_rows)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[EntrapmentResult]:
        if self.__has_winner:
            return EntrapmentResult.LOOSE if pos == self.__acting_player else EntrapmentResult.WIN
        if self.__is_full():
            return EntrapmentResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        grid: list[list[int]] = []
        for i in range(self.get_num_rows()):
            for j in range(self.get_num_cols()):
                grid.append([i, j])

        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda pos: EntrapmentAction(pos[0], pos[1]),
                grid))
        )

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
