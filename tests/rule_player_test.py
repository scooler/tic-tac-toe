import unittest
import numpy as np
from game.players.rule_player import RulePlayerV1

class RulePlayerTest(unittest.TestCase):
  def test_constructor(self):
    self.assertEqual(2, RulePlayerV1(1).other_player)
    self.assertEqual(1, RulePlayerV1(2).other_player)

  def test_two_in_a_row_other_player(self):
    player = RulePlayerV1(1)
    self.assertEqual(True, player.two_in_a_row(np.array([0, 2, 2])))
    self.assertEqual(True, player.two_in_a_row(np.array([2, 0, 2])))
    self.assertEqual(True, player.two_in_a_row(np.array([2, 2, 0])))

  def test_not_two_in_a_row_other_player(self):
    player = RulePlayerV1(2)
    # same player
    self.assertEqual(False, player.two_in_a_row(np.array([0, 2, 2])))
    self.assertEqual(False, player.two_in_a_row(np.array([2, 0, 2])))
    self.assertEqual(False, player.two_in_a_row(np.array([2, 2, 0])))

    self.assertEqual(False, player.two_in_a_row(np.array([2, 1, 1])))
    self.assertEqual(False, player.two_in_a_row(np.array([1, 2, 1])))
    self.assertEqual(False, player.two_in_a_row(np.array([1, 1, 2])))

    self.assertEqual(False, player.two_in_a_row(np.array([2, 1, 0])))
    self.assertEqual(False, player.two_in_a_row(np.array([1, 0, 2])))
    self.assertEqual(False, player.two_in_a_row(np.array([2, 0, 1])))