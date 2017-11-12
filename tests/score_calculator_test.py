import unittest
import numpy as np
from game.players.score_calculator import ScoreCalculator

def empty_board():
  return np.zeros((3, 3))

class ScoreCalculatorTest(unittest.TestCase):

  def test_constructor(self):
    self.assertEqual([], ScoreCalculator([]).board)

  def test_score_for_empty_board(self):
    self.assertEqual(0, ScoreCalculator(empty_board()).score_for_player(1))
    self.assertEqual(0, ScoreCalculator(empty_board()).score_for_player(2))

  def test_score_counts_single_pair(self):
    board = empty_board()
    board[0,0] = 1
    board[0,1] = 1
    self.assertEqual(1, ScoreCalculator(board).score_for_player(1))
    self.assertEqual(-1, ScoreCalculator(board).score_for_player(2))

  def test_score_counts_multiple_pairs(self):
    board = empty_board()
    board[0,0] = 1
    board[0,1] = 1
    board[1,1] = 1
    self.assertEqual(3, ScoreCalculator(board).score_for_player(1))
    self.assertEqual(-3, ScoreCalculator(board).score_for_player(2))

  def test_score_counts_properly_multiple_selections_without_pair(self):
    # no pairs 2 selections, but on "check kinght move" positions
    board = empty_board()
    board[0,0] = 1
    board[1,2] = 1
    self.assertEqual(0, ScoreCalculator(board).score_for_player(1))
    self.assertEqual(0, ScoreCalculator(board).score_for_player(2))

  def test_score_counts_winning(self):
    board = empty_board()
    board[0,0] = 1
    board[1,1] = 1
    board[2,2] = 1
    self.assertEqual(100, ScoreCalculator(board).score_for_player(1))

  def test_score_counts_loosing(self):
    board = empty_board()
    board[0,0] = 2
    board[1,1] = 2
    board[2,2] = 2
    self.assertEqual(-100, ScoreCalculator(board).score_for_player(1))

  def test_score_for_complex_board(self):
    board = np.array([ # oponent has an unblocked pair (-1), my pair is blocked (0)
      [2, 0, 0],
      [1, 2, 0],
      [1, 0, 0]
    ])
    self.assertEqual(-1, ScoreCalculator(board).score_for_player(1))

    board = np.array([ # I block oponent's pair (0), and have a pair (1)
      [2, 0, 0],
      [0, 2, 0],
      [1, 0, 1]
    ])
    self.assertEqual(1, ScoreCalculator(board).score_for_player(1))
