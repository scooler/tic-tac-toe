import unittest
import numpy as np
from game.players.rule_player import RulePlayerV1
from game.players.rule_player import RulePlayerV2

class RulePlayerTest(unittest.TestCase):
  def test_constructor(self):
    self.assertEqual(2, RulePlayerV1(1).other_player)
    self.assertEqual(1, RulePlayerV1(2).other_player)

  def test_two_in_a_row_other_player(self):
    player = RulePlayerV1(1)
    self.assertEqual(True, player.two_in_a_row(np.array([0, 2, 2]), 2))
    self.assertEqual(True, player.two_in_a_row(np.array([2, 0, 2]), 2))
    self.assertEqual(True, player.two_in_a_row(np.array([2, 2, 0]), 2))

  def test_not_two_in_a_row_other_player(self):
    player = RulePlayerV1(2)
    # same player
    self.assertEqual(False, player.two_in_a_row(np.array([0, 2, 2]), 1))
    self.assertEqual(False, player.two_in_a_row(np.array([2, 0, 2]), 1))
    self.assertEqual(False, player.two_in_a_row(np.array([2, 2, 0]), 1))

    self.assertEqual(False, player.two_in_a_row(np.array([2, 1, 1]), 1))
    self.assertEqual(False, player.two_in_a_row(np.array([1, 2, 1]), 1))
    self.assertEqual(False, player.two_in_a_row(np.array([1, 1, 2]), 1))

    self.assertEqual(False, player.two_in_a_row(np.array([2, 1, 0]), 1))
    self.assertEqual(False, player.two_in_a_row(np.array([1, 0, 2]), 1))
    self.assertEqual(False, player.two_in_a_row(np.array([2, 0, 1]), 1))

  def test_get_input_rows(self):
    player = RulePlayerV1(1)
    board = np.zeros((3, 3))
    board[1, 0] = 2
    board[2, 0] = 2
    self.assertEqual([0, 0], player.get_input(board))

  def test_get_input_cols(self):
    player = RulePlayerV1(1)
    board = np.zeros((3, 3))
    board[0, 0] = 2
    board[0, 1] = 2
    self.assertEqual([0, 2], player.get_input(board))

  def test_get_input_v2_win(self):
    player = RulePlayerV2(1)
    board = np.zeros((3, 3))
    board[0, 0] = 1 # I have a chance to win
    board[0, 1] = 1
    board[1, 0] = 2 # and so does the oponent
    board[1, 1] = 2
    self.assertEqual([0, 2], player.get_input(board)) # I should pick winning and not blocking the other from winning
