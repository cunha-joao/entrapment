class EntrapmentAction:
    """
    an entrapment action takes the value of the row and column of where to place the initial roamers
    after each player has placed 3 roamers each action will take the type of move each player wishes to make and the
    coordinates of where to change the roamers or where to put a wall
    """
    __col: int
    __row: int

    def __init__(self, col: int, row: int):
        self.__col = col
        self.__row = row

    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row
