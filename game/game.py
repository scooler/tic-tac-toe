
# from .pygame.display import UIDisplay
from .asci.board import Board
from pygame.locals import *
import pygame, sys,os
from .players.human_player import HumanPlayer
from .players.random_player import RandomPlayer

class Game:
  def __init__(self):
    # self.display = UIDisplay()
    self.board = Board()
    self.players = [HumanPlayer(), RandomPlayer()]
    self.current_player = 1

  def start(self):
    self.game_loop()

  def game_loop(self):
    while not self.board.is_finished():
      self.board.draw()
      self.handle_input()
      self.switch_player()

    self.board.draw()

  def handle_input(self):
    coords = self.players[self.current_player - 1].get_input(self.board.board)
    self.board.move(coords[0], coords[1], self.current_player)


  def switch_player(self):
    if self.current_player == 1:
      self.current_player = 2
    else:
      self.current_player = 1
