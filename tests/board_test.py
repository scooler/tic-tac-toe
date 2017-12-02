import unittest
import numpy as np
from game.board import Board

# def empty_board():
#   return np.zeros((3, 3))

class BoardTest(unittest.TestCase):

  def test_constructor(self):
    b1 = Board(array = [[0,0,0], [0,0,0], [0,0,0]]).board
    b2 = Board().board
    self.assertTrue(np.array_equal(b1, b2))