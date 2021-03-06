import numpy as np

WINNING_SCORE = 100

"""An AI helper class that scores the state of the board"""
class ScoreCalculator:
  def __init__(self, board):
    self.board = board
    self.current_score = 0

  def score_for_player(self, player):
    self.add_players_pairs(player)
    self.substract_oponents_pairs(player)
    self.add_wining_condition(player)
    self.substract_loosing_condition(player)
    return self.current_score

  def add_players_pairs(self, player):
    self.current_score += self.find_pairs_count(player)

  def substract_oponents_pairs(self, player):
    self.current_score -= self.find_pairs_count(self.oponent_of_player(player))

  def add_wining_condition(self, player):
    if self.is_three_in_row_present(player): self.current_score += WINNING_SCORE

  def substract_loosing_condition(self, player):
    if self.is_three_in_row_present(self.oponent_of_player(player)): self.current_score -= WINNING_SCORE

  def find_pairs_count(self, player):
    pairs_count = 0
    for i in range(0, self.board.shape[0]):                     # rows
      if self.two_in_a_row(self.board[i, :], player):
        # print('Found two in row ', i)
        y = np.where(self.board[i, :] == 0)[0][0]
        pairs_count += 1
        # return [i, y]

    for i in range(0, self.board.shape[1]):                     # columns
      if self.two_in_a_row(self.board[:, i], player):
        # print('Found two in col ', i)
        x = np.where(self.board[:, i] == 0)[0][0]
        pairs_count += 1
        # return [x, i]

    if self.two_in_a_row(np.diag(self.board), player): # diagonal
      # print('Found two on diag ')
      diag_pos = np.where(np.diag(self.board) == 0)[0][0]
      pairs_count += 1
      # return [diag_pos, diag_pos]

    if self.two_in_a_row(np.diag(np.flipud(self.board)), player): # anty-diagonal
      # print('Found two on anty-diag ')
      anty_diag_pos = np.where(np.diag(np.flipud(self.board)) == 0)[0][0]
      pairs_count += 1
      # return [board.shape[0] - 1 - anty_diag_pos, anty_diag_pos]

    return pairs_count

  def is_three_in_row_present(self, player):
    for i in range(0, self.board.shape[0]):                     # rows
      if self.three_in_a_row(self.board[i, :], player):
        # print('Found two in row ', i)
        return True

    for i in range(0, self.board.shape[1]):                     # columns
      if self.three_in_a_row(self.board[:, i], player):
        # print('Found two in col ', i)
        return True

    if self.three_in_a_row(np.diag(self.board), player): # diagonal
      # print('Found two on diag ')
      return True
      # return [diag_pos, diag_pos]

    if self.three_in_a_row(np.diag(np.flipud(self.board)), player): # anty-diagonal
      # print('Found two on anty-diag ')
      return True

    return False


  def oponent_of_player(self, player):
    if player == 1:
      return 2
    else:
      return 1

  def two_in_a_row(self, row, player):
    row = row.copy()
    row.sort()
    if row[0] == 0 and row[1] == player and row[2] == player: return True
    return False

  def three_in_a_row(self, row, player):
    return np.unique(row).size == 1 and row[0] == player
