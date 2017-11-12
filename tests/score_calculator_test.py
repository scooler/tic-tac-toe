import unittest
import numpy as np
from game.players.score_calculator import ScoreCalculator

def empty_board():
  np.zeros((3, 3))
class ScoreCalculatorTest(unittest.TestCase):

  def test_constructor(self):
    self.assertEqual([], ScoreCalculator([]).board)

  def test_score_for_empty_board(self):
    self.assertEqual(0, ScoreCalculator(empty_board()).score())
