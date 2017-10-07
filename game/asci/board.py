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

  def move(self, x, y, current_player): # x & y are here 0-2 (board array indexs)
    self.board[x, y] = current_player
    print(self.board)


