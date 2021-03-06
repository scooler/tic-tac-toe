from game.displays.asci_display import ASCIDisplay
from game.displays.pygame_display import PygameDisplay
import pygame
import time
import sys
from pygame.locals import *

class ConsolePlayer:
  def __init__(self, player_no):
    self.player_no = player_no

  def get_input(self, board):
    key = input("use keys 1-9 for fields 1|2|3 etc\n>")
    key = int(key) - 1
    board_y = key % 3
    board_x = int(key / 3)
    return [board_x, board_y]

class ConsolePlayer:
  def __init__(self, player_no):
    self.player_no = player_no

  def get_input(self, board):
    key = input("use keys 1-9 for fields 1|2|3 etc\n>")
    key = int(key) - 1
    board_y = key % 3
    board_x = int(key / 3)
    return [board_x, board_y]

  def display_class(self):
    return ASCIDisplay


class PygamePlayer:
  def __init__(self, player_no):
    self.player_no = player_no

  def get_input(self, board):
    while True:
      event = pygame.event.wait()
      if event.type == QUIT:
        sys.exit(0)

      if event.type == MOUSEBUTTONDOWN and event.button == 1:
        print('Position: ', event.pos)
        board_x = int(event.pos[0] / 200)
        board_y = int(event.pos[1] / 200)
        return [board_x, board_y]

  def display_class(self):
    return PygameDisplay