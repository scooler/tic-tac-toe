import numpy as np

"""An AI helper class that scores the state of the board"""
class ScoreCalculator:
  def __init__(self, board):
    self.board = board

  def score(self):
    return 0