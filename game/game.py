
from .displays.asci_display import ASCIDisplay
from .board import Board
from pygame.locals import *
import pygame, sys,os
from .players.human_player import HumanPlayer
from .players.random_player import RandomPlayer

class Game:
  def __init__(self):
    # self.display = UIDisplay()
    self.board = Board()
    self.display = ASCIDisplay(self.board)
    self.select_game_type()
    self.current_player = 1

  def select_game_type(self):
    game_type = input('What game type? H = Human, R = Random (so HH is PvP)')
    game_type = game_type.upper()
    players = []
    for i in range(0, 2):
      if game_type[i] == 'H':
        players.append(HumanPlayer(i))
      else:
        if game_type[i] == 'R':
          players.append(RandomPlayer(i))

    self.players = players

  def start(self):
    self.game_loop()
    self.finish()

  def game_loop(self):
    while not self.board.is_finished():
      self.display.draw()
      self.board.show_player_info(self.current_player)
      self.handle_input()
      self.switch_player()

  def finish(self):
    self.display.draw()
    self.display.show_results()

  def handle_input(self):
    coords = self.players[self.current_player - 1].get_input(self.board.board)
    self.board.move(coords[0], coords[1], self.current_player)


  def switch_player(self):
    if self.current_player == 1:
      self.current_player = 2
    else:
      self.current_player = 1
