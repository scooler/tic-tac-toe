import numpy as np

class Board:
  def __init__(self):
    self.board = np.zeros((3, 3), dtype=np.int8)

  def draw(self):
    self.draw_board()

  def draw_board(self):
    for i in range(0, 3):
      line = ''
      for j in range(0, 3):
        if self.board[i, j] == 0:
          line += ' '
        if self.board[i, j] == 1:
          line += 'X'
        if self.board[i, j] == 2:
          line += 'O'

        if j < 2:
          line += '|'

      print(line)
      if i < 2:
        print("------")
    print('Finished?:', self.is_finished())

  def move(self, x, y, current_player): # x & y are here 0-2 (board array indexs)
    self.board[x, y] = current_player


  def are_same_and_non_zero(self, array):
    return np.unique(array).size == 1 and array[0] != 0

  def is_board_full(self):
    return not np.any(np.unique(self.board) == 0)

  def is_finished(self):
    for i in range(0, 3):
      if self.are_same_and_non_zero(self.board[i, :]): return True # rows
      if self.are_same_and_non_zero(self.board[:, i]): return True # columns
    if self.are_same_and_non_zero(np.diag(self.board)): return True # diagonal
    if self.are_same_and_non_zero(np.diag(np.flipud(self.board))): return True # anty-diagonal

    if self.is_board_full(): return True # draw

    return False

