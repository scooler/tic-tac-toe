import numpy as np
from game.displays.null_display import NullDisplay
from game.displays.asci_display import ASCIDisplay

class RandomPlayer:
  def __init__(self, player_no):
    self.player_no = player_no

  def get_input(self, board):
    empty_indexes = np.where(board == 0)
    zipped = np.column_stack(empty_indexes)
    np.random.shuffle(zipped)
    return zipped[0]

  def display_class(self):
    return ASCIDisplay
    # return NullDisplay