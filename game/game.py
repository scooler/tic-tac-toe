
from .displays.asci_display import ASCIDisplay
from .displays.pygame_display import PygameDisplay
from .board import Board
from pygame.locals import *
import pygame, sys,os
from .players.human_player import ConsolePlayer
from .players.human_player import PygamePlayer
from .players.random_player import RandomPlayer

class Game:
  def __init__(self):
    self.board = Board()
    self.select_game_type()
    self.setup_displays()

    self.current_player = 1

  def select_game_type(self):
    game_type = input('What game type? H = Human, R = Random (so HH is PvP)')
    game_type = game_type.upper()
    players = []
    for i in range(0, 2):
      if game_type[i] == 'H':
        players.append(ConsolePlayer(i))
      else:
        if game_type[i] == 'R':
          players.append(RandomPlayer(i))
        else:
          if game_type[i] == 'P':
            players.append(PygamePlayer(i))

    self.players = players

  def setup_displays(self):
    self.displays = [
      self.players[0].display_class()(self.board),
      self.players[1].display_class()(self.board)
    ]

  def start(self):
    self.game_loop()
    self.finish()

  def game_loop(self):
    while not self.board.is_finished():
      self.displays[self.current_player-1].draw()
      self.board.show_player_info(self.current_player)
      self.handle_input()
      self.switch_player()

  def finish(self):
    self.displays[self.current_player-1].draw()
    ASCIDisplay(self.board).show_results()

  def handle_input(self):
    coords = self.players[self.current_player - 1].get_input(self.board.board)
    self.board.move(coords[0], coords[1], self.current_player)


  def switch_player(self):
    if self.current_player == 1:
      self.current_player = 2
    else:
      self.current_player = 1
