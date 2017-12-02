import numpy as np

class Board:
  def __init__(self, size = (3, 3), array = None):
    # if array == None:
    if array is None:
      self.board = np.zeros(size, dtype=np.int8)
    else:
      self.board = np.array(array, dtype=np.int8)

    self.x_size = self.board.shape[0]
    self.y_size = self.board.shape[1]
    self.player_who_won = None


  def move(self, x, y, current_player):
    self.board[x, y] = current_player


  def are_same_and_non_zero(self, array):
    return np.unique(array).size == 1 and array[0] != 0

  def is_board_full(self):
    return not np.any(np.unique(self.board) == 0)

  def is_finished(self):
    for i in range(0, self.x_size):                     # rows
      if self.are_same_and_non_zero(self.board[i, :]):
        self.player_who_won = self.board[i, 0]
        self.result = 'Won {} - row {}'.format(self.player(self.player_who_won), i)
        return True

    for i in range(0, self.y_size):                     # columns
      if self.are_same_and_non_zero(self.board[:, i]):
        self.player_who_won = self.board[0, i]
        self.result = 'Won {} - col {}'.format(self.player(self.player_who_won), i)
        return True

    if self.are_same_and_non_zero(np.diag(self.board)): # diagonal
      self.player_who_won = self.board[1, 1]
      self.result = 'Won {} - diagonal {}'.format(self.player(self.player_who_won), i)
      return True

    if self.are_same_and_non_zero(np.diag(np.flipud(self.board))): # anty-diagonal
      self.player_who_won = self.board[1, 1]
      self.result = 'Won {} - anty-diagonal {}'.format(self.player(self.player_who_won), i)

      return True

    if self.is_board_full():
      self.player_who_won = 0 # nobody
      self.result = 'Draw'
      return True # draw

    return False

  def player(self, player_no):
    if player_no == 1: return 'Player 1 (X)'
    if player_no == 2: return 'Player 2 (O)'

  def show_player_info(self, player_no):
    print("It's turn of ", self.player(player_no))
