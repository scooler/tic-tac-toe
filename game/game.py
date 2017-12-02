
from .displays.asci_display import ASCIDisplay
from .displays.null_display import NullDisplay
from .displays.pygame_display import PygameDisplay
from .board import Board
from pygame.locals import *
import pygame, sys,os
import numpy as np
from .players.human_player import ConsolePlayer
from .players.human_player import PygamePlayer
from .players.random_player import RandomPlayer
from .players.rule_player import RulePlayerV1
from .players.rule_player import RulePlayerV2
from .players.score_player import ScorePlayer
from .players.look_ahead_player import LookAheadPlayer

GAME_TYPES = {
  'C': ConsolePlayer,
  'R': RandomPlayer,
  'P': PygamePlayer,
  '1': RulePlayerV1,
  '2': RulePlayerV2,
  '3': ScorePlayer,
  '4': LookAheadPlayer
}

class Game:
  def __init__(self, output_enabled = True):
    self.output_enabled = output_enabled
    self.select_game_type()
    self.reversed = False
    self.init_players()
    self.reset() # I thought about calling it setup, but I'd setup it later multiple times :(

  def select_game_type(self):
    game_type = input('What game type? C (console), P(pygame), R(random), 1-4 (AI v1-v4) (so HH is PvP in console)')
    game_type = game_type.upper()
    player_classes = []
    for i in range(0, 2):
      player_classes.append(GAME_TYPES[game_type[i]])
    self.player_classes = player_classes

  def init_players(self):
    players = []
    for i in range(0, 2):
      players.append(self.player_classes[i](i + 1))
    self.players = players

  def setup_displays(self):
    if self.output_enabled:
      self.displays = [
        self.players[0].display_class()(self.board),
        self.players[1].display_class()(self.board)
      ]
    else:
      self.displays = [NullDisplay(), NullDisplay()]

  def start(self):
    self.game_loop()
    self.finish()

  def game_loop(self):
    while not self.board.is_finished():
      self.displays[self.current_player-1].draw()
      if self.output_enabled: self.board.show_player_info(self.current_player)
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

  def reset(self):
    self.board = Board()
    self.setup_displays()

    self.current_player = 1

  def reverse_players(self):
    self.player_classes = [self.player_classes[1], self.player_classes[0]]
    # player_classes = [self.player_classes[0], self.player_classes[1]]
    self.init_players()
    self.reversed = not self.reversed

class GameStats:
  def __init__(self):
    self.game = Game(False)
    self.repeats = 1000
    self.winning_players = []

  def run(self):
    self.run_games()
    self.show_stats()

  def run_games(self):
    for i in range(0, self.repeats):
      self.game.game_loop()
      if self.game.reversed:
        who_won = self.game.board.player_who_won
        if who_won == 1: self.winning_players.append(2)
        if who_won == 2: self.winning_players.append(1)
        if who_won == 0: self.winning_players.append(0)
      else:
        self.winning_players.append(self.game.board.player_who_won)
      self.game.reverse_players()
      self.game.reset()

  def show_stats(self):
    res = np.array(self.winning_players)
    draws = np.where(res == 0)[0].shape[0]
    p1_won = np.where(res == 1)[0].shape[0]
    p2_won = np.where(res == 2)[0].shape[0]
    p1_win_percantage = p1_won/(p1_won+p2_won)*100
    p2_win_percantage = p2_won/(p1_won+p2_won)*100

    print("Player 1 won ", p1_won, " times, Player 2 won ", p2_won, " times - so ", p1_win_percantage, "/", p2_win_percantage," - ", draws, " Draws")
