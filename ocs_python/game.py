

class Jeu:
    """
    This is the class representing the current state fo the game (the labyrinthe).

    Args:
        Map number
    """

    def __init__(self, map, forbidden_symbols=None):
        """
        Builder of our game object which is the current state of the game
        """

        self.map = ''
        self.position_joueur = -1
        for i,symbol in enumerate(map):
            if symbol != 'X':
                self.map = self.map + symbol
            else:
                self.map = self.map + ' '
                self.position_joueur = i

        self.nombre_col = len(map.split('\n')[0]) + 1
        self.nombre_lignes = len(map.split('\n'))
        self.interdits = forbidden_symbols


    def __repr__(self):
        """
        Special method which format our board game.

        Returns:
            formatted string
        """

        map_to_print = ''
        for i,symbol in enumerate(self.map):
            if i != self.position_joueur:
                map_to_print = map_to_print + symbol
            else:
                map_to_print = map_to_print + 'X'

        return map_to_print

    def move_robot(self, direction, distance):
        """
        Function which moves the robot according to the letter types by the player,
        and checks if the position is permitted.
        :param direction: str
        :param distance: int
        :return: 0 if the party continues, 1 if the robot has won
        """

        dic_to_add = {
            's':self.nombre_col,
            'n':-self.nombre_col,
            'e':1,
            'w':-1,
            }

        position_tmp = dic_to_add[direction]*distance

        if position_tmp > len(self.map) or position_tmp < 0:
            raise ValueError("Impossible to move the robot out of the board game.")

        elif self.map[position_tmp] in self.interdits or self.map[position_tmp] == '\n':
            raise ValueError("Impossible to move the robot on this spot.")

        else:
            self.position_joueur = position_tmp

        if self.map[position_tmp] == 'U':
            return 1

        return 0

