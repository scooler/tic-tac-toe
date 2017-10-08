import numpy as np
class RandomPlayer:
  def get_input(self, board):
    empty_indexes = np.where(board == 0)
    zipped = np.column_stack(empty_indexes)
    np.random.shuffle(zipped)
    return zipped[0]