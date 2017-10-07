from .board import Board
import os

class ASCIDisplay:
  def __init__(self):
    self.board = Board()

  def draw(self):
    os.system('clear')
    self.board.draw()

  def input_key(self, key, current_player):
    print("key: ", key)
    board_y = key % 3
    board_x = int(key / 3)
    self.board.move(board_x, board_y, current_player)


