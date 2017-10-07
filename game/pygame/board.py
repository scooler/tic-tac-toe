import numpy as np
import pygame
from pygame.locals import *

BORDER_COLOR = (255, 255, 255)

class Board:
  def __init__(self, screen):
    # self.board = np.array(3, 3)
    self.screen = screen

  def draw(self):
    self.draw_board()

  def draw_board(self):
    for i in range(1, 3):
      pygame.draw.line(self.screen, BORDER_COLOR, (200*i, 0), (200*i, 600), 2)
      pygame.draw.line(self.screen, BORDER_COLOR, (0, 200*i), (600, 200*i), 2)

