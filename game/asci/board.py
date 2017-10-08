import numpy as np
import os

class Board:
  def __init__(self):
    self.board = np.zeros((3, 3), dtype=np.int8)

  def draw(self):
    os.system('clear')
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
    if self.is_finished(): print(self.result)

  def move(self, x, y, current_player): # x & y are here 0-2 (board array indexs)
    self.board[x, y] = current_player


  def are_same_and_non_zero(self, array):
    return np.unique(array).size == 1 and array[0] != 0

  def is_board_full(self):
    return not np.any(np.unique(self.board) == 0)

  def is_finished(self):
    for i in range(0, 3):
      if self.are_same_and_non_zero(self.board[i, :]):
        self.result = 'Won {} - row {}'.format(self.player(self.board[i, 0]), i)
        return True # rows
      if self.are_same_and_non_zero(self.board[:, i]):
        self.result = 'Won {} - col {}'.format(self.player(self.board[i, 0]), i)
        return True # columns
    if self.are_same_and_non_zero(np.diag(self.board)):
      self.result = 'Won {} - diagonal {}'.format(self.player(self.board[i, 0]), i)
      return True # diagonal
    if self.are_same_and_non_zero(np.diag(np.flipud(self.board))):
      self.result = 'Won {} - anty-diagonal {}'.format(self.player(self.board[i, 0]), i)
      return True # anty-diagonal

    if self.is_board_full():
      self.result = 'Draw'
      return True # draw

    return False

  def player(self, player_no):
    if player_no == 1: return 'Player 1 (X)'
    if player_no == 2: return 'Player 2 (O)'
