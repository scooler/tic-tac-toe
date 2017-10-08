
# from .pygame.display import UIDisplay
from .asci.board import Board
from pygame.locals import *
import pygame, sys,os

class Game:
  def __init__(self):
    # self.display = UIDisplay()
    self.board = Board()
    self.current_player = 1

  def start(self):
    self.game_loop()

  def game_loop(self):
    while not self.board.is_finished():
      self.board.draw()
      self.handle_input2()

    self.board.draw()

  def handle_input2(self):
    key = input("use keys 1-9 for fields 1|2|3 etc\n>")
    self.board.input_key(int(key) - 1, self.current_player)
    self.switch_player()



  def handle_input(self):
    # for event in pygame.event.get():
    event = pygame.event.wait()
    if event.type == QUIT:
      sys.exit(0)
    print(event)
    print(pygame.key.get_focused())

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
          print('left')
      if event.key == pygame.K_RIGHT:
          print('right')

    # Doesn't work :/
    # if event.type == MOUSEBUTTONDOWN and event.button == 1:
    #   print(event)
    #   self.display.input(event.pos[0], event.pos[1], self.current_player)
    #   self.switch_player()


  def switch_player(self):
    if self.current_player == 1:
      self.current_player = 2
    else:
      self.current_player = 1
