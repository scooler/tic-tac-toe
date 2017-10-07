import pygame, sys,os
from pygame.locals import *
from .board import Board


SCREEN_SIZE = (600, 600)
class UIDisplay:
  def __init__(self):
    pygame.init()

    self.window = pygame.display.set_mode(SCREEN_SIZE)
    self.board = Board(self.window)
    self.window.fill((0,0,0))

  def draw(self):
    self.board.draw()
    pygame.display.update()
    self.handle_input(pygame.event.get())


  def handle_input(self, events):
    for event in events:
      if event.type == QUIT:
        sys.exit(0)
      else:
        print(event)