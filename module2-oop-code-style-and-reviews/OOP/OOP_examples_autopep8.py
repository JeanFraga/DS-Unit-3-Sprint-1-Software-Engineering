"""
CLasses to represent games
"""

from random import random


class Game:
    """
    General representation of an abstract game.
    """

    fun_level = 5

    def __init__(self, rounds=2, player1='Owen', player2='Jean'):
        self.rounds = rounds
        self.steps = 5
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """
        Print players
        """
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_rounds(self):
        """
        increment number of rounds
        """
        self.rounds += 1

    def winner(self):
        """
        randomly pick a winner
        """
        return self.player1 if random() > 0.5 else self.player2


class Tic(Game):
    """
    subclass of Game called Tictactoe
    """

    def __init__(self, rounds=3, player1='Riley', player2='Amer'):
        super().__init__(rounds, player1, player2)

    def print_players(self):
        print('{} is playing TicTacToe with {}'.format(
            self.player1, self.player2))