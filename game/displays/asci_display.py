# from board import Board
import os

class ASCIDisplay:
  def __init__(self, board):
    self.board = board

  def show_results(self):
    print(self.board.result)

  def draw(self):
    os.system('clear')
    self.draw_board()

  def draw_board(self):
    for i in range(0, self.board.x_size):
      line = ''
      for j in range(0, self.board.y_size):
        if self.board.board[i, j] == 0:
          line += ' '
        if self.board.board[i, j] == 1:
          line += 'X'
        if self.board.board[i, j] == 2:
          line += 'O'

        if j < self.board.y_size - 1:
          line += '|'

      print(line)
      if i < self.board.x_size - 1:
        print("------")


