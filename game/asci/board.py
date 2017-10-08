import numpy as np
import os

class Board:
  def __init__(self, size=(3, 3)):
    self.board = np.zeros(size, dtype=np.int8)
    self.x_size = self.board.shape[0]
    self.y_size = self.board.shape[1]

  def draw(self):
    os.system('clear')
    self.draw_board()

  def draw_board(self):
    for i in range(0, self.x_size):
      line = ''
      for j in range(0, self.y_size):
        if self.board[i, j] == 0:
          line += ' '
        if self.board[i, j] == 1:
          line += 'X'
        if self.board[i, j] == 2:
          line += 'O'

        if j < self.y_size - 1:
          line += '|'

      print(line)
      if i < self.x_size - 1:
        print("------")
    if self.is_finished(): print(self.result)

  def move(self, x, y, current_player):
    self.board[x, y] = current_player


  def are_same_and_non_zero(self, array):
    return np.unique(array).size == 1 and array[0] != 0

  def is_board_full(self):
    return not np.any(np.unique(self.board) == 0)

  def is_finished(self):
    for i in range(0, self.x_size):                     # rows
      if self.are_same_and_non_zero(self.board[i, :]):
        self.result = 'Won {} - row {}'.format(self.player(self.board[i, 0]), i)
        return True

    for i in range(0, self.y_size):                     # columns
      if self.are_same_and_non_zero(self.board[:, i]):
        self.result = 'Won {} - col {}'.format(self.player(self.board[0, i]), i)
        return True

    if self.are_same_and_non_zero(np.diag(self.board)): # diagonal
      self.result = 'Won {} - diagonal {}'.format(self.player(self.board[1, 1]), i)
      return True

    if self.are_same_and_non_zero(np.diag(np.flipud(self.board))): # anty-diagonal
      self.result = 'Won {} - anty-diagonal {}'.format(self.player(self.board[1, 1]), i)
      return True

    if self.is_board_full():
      self.result = 'Draw'
      return True # draw

    return False

  def player(self, player_no):
    if player_no == 1: return 'Player 1 (X)'
    if player_no == 2: return 'Player 2 (O)'

  def show_player_info(self, player_no):
    print("It's turn of ", self.player(player_no))
