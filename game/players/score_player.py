import numpy as np
from game.displays.null_display import NullDisplay
from game.displays.asci_display import ASCIDisplay
from game.players.score_calculator import ScoreCalculator

class ScorePlayer:
  def __init__(self, player_no):
    self.player_no = player_no

  def get_input(self, board):
    best_move = None
    best_score = -100
    for i in range(0, board.shape[0]):
      for j in range(0, board.shape[1]):
        if board[i, j] == 0:
          score = ScoreCalculator(board.copy()).score_for_player(self.player_no)
          if score > best_score:
            best_move = [i, j]
            best_score = score

    return best_move

  def display_class(self):
    return ASCIDisplay
    # return NullDisplay