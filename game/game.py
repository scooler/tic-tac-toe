
from .displays.asci_display import ASCIDisplay
from .displays.pygame_display import PygameDisplay
from .board import Board
from pygame.locals import *
import pygame, sys,os
from .players.human_player import ConsolePlayer
from .players.human_player import PygamePlayer
from .players.random_player import RandomPlayer
from .players.rule_player import RulePlayerV1
from .players.rule_player import RulePlayerV2

GAME_TYPES = {
  'C': ConsolePlayer,
  'R': RandomPlayer,
  'P': PygamePlayer,
  '1': RulePlayerV1,
  '2': RulePlayerV2
}

class Game:
  def __init__(self):
    self.board = Board()
    self.select_game_type()
    self.setup_displays()

    self.current_player = 1

  def select_game_type(self):
    game_type = input('What game type? C (console), P(pygame), R(random), 1(AI v1), 2(AI v2) (so HH is PvP in console)')
    game_type = game_type.upper()
    players = []
    for i in range(0, 2):
      players.append(GAME_TYPES[game_type[i]](i + 1))

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
