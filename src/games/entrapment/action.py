class EntrapmentAction:
    """
    an entrapment action takes the value of the row and column of where to place the initial roamers
    after each player has placed 3 roamers each action will take the type of move each player wishes to make and the
    coordinates of where to change the roamers or where to put a wall
    """
    __col: int
    __row: int
    __new_col: int
    __new_row: int
    __wall_col: int
    __wall_row: int
    __move_type: int

    def __init__(self, col: int, row: int, new_col: int, new_row: int, wall_col: int, wall_row: int, move_type: int):
        self.__col = col
        self.__row = row
        self.__new_col = new_col
        self.__new_row = new_row
        self.__wall_col = wall_col
        self.__wall_row = wall_row
        self.__move_type = move_type

    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row

    def get_new_col(self):
        return self.__new_col

    def get_new_row(self):
        return self.__new_row

    def get_wall_col(self):
        return self.__wall_col

    def get_wall_row(self):
        return self.__wall_row

    def get_move_type(self):
        return self.__move_type
