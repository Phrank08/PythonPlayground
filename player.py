import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
            pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
            square = random.choice(game.available_moves())
            return square

    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
         valid_square = False
         val = None
         while not valid_square:
              square = input(self.letter + '\'s turn. Input move [0-9]:')
              """
              we're going to check rhat this is a correct value by trying to cast
              it to an integer, and if it's not, then we say its invalid
              if that spot is not available on the board, we also say it's invalid
              """
              try:
                   val = int(square)
                   if val not in game.available_moves():
                        raise ValueError
                   valid_square = True # if these are successful, that perfect
              except ValueError:
                   print("Invalid Square. Try again.")

                   return val