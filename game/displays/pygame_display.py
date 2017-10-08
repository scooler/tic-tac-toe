import pygame
from .board import Board


SCREEN_SIZE = (600, 600)
class UIDisplay:
  def __init__(self):
    pygame.init()

    self.window = pygame.display.set_mode(SCREEN_SIZE)
    self.board = Board(self.window)
    self.window.fill((0,0,0))

  def draw(self):
    self.draw_board()
    pygame.display.update()

  def draw_board(self):
    for i in range(1, 3):
      pygame.draw.line(self.screen, BORDER_COLOR, (200*i, 0), (200*i, 600), 2)
      pygame.draw.line(self.screen, BORDER_COLOR, (0, 200*i), (600, 200*i), 2)

  def input(self, x, y, current_player): # here it's a raw mouse input (x & y are screen coordinates)
    print("x: ", x, "y: ", y)
    board_x = int(x / 200)
    board_y = int(y / 200)
    self.board.move(board_x, board_y, current_player)