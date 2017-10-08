import numpy as np
from game.displays.null_display import NullDisplay

"""The simple rule AI - if oponent has 2 in a row - block it"""
class RulePlayerV1:
  def __init__(self, player_no):
    self.player_no = player_no
    if player_no == 1:
      self.other_player = 2
    else:
      self.other_player = 1

  def get_input(self, board):
    for i in range(0, board.shape[0]):                     # rows
      if self.two_in_a_row(board[i, :]):
        # print('Found two in row ', i)
        y = np.where(board[i, :] == 0)[0][0]
        return [i, y]

    for i in range(0, board.shape[1]):                     # columns
      if self.two_in_a_row(board[:, i]):
        # print('Found two in col ', i)
        x = np.where(board[:, i] == 0)[0][0]
        return [x, i]

    if self.two_in_a_row(np.diag(board)): # diagonal
      # print('Found two on diag ')
      diag_pos = np.where(np.diag(board) == 0)[0][0]
      return [diag_pos, diag_pos]

    if self.two_in_a_row(np.diag(np.flipud(board))): # anty-diagonal
      # print('Found two on anty-diag ')
      anty_diag_pos = np.where(np.diag(np.flipud(board)) == 0)[0][0]
      return [board.shape[0] - 1 - anty_diag_pos, anty_diag_pos]
    # print('not found - falling back to random')
    return self.random_input(board)

  def random_input(self, board):
    empty_indexes = np.where(board == 0)
    zipped = np.column_stack(empty_indexes)
    np.random.shuffle(zipped)
    return zipped[0]

  def two_in_a_row(self, row):
    row = row.copy()
    row.sort()
    if row[0] == 0 and row[1] == self.other_player and row[2] == self.other_player: return True
    return False

  def display_class(self):
    return NullDisplay