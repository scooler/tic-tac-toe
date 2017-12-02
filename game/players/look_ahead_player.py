import numpy as np
from game.displays.null_display import NullDisplay
from game.displays.asci_display import ASCIDisplay
from game.players.score_calculator import ScoreCalculator
from game.players.score_player import ScorePlayer
from game.board import Board

class LookAheadPlayer:
  def __init__(self, player_no):
    self.player_no = player_no

  def get_input(self, board):
    # best_move = None
    # best_score = -100 # TBD - perhaps use some partial scores to decide somewhat better moves
    for i in range(0, board.shape[0]):
      for j in range(0, board.shape[1]):
        if board[i, j] != 0: continue
        current_board = Board(array = board.copy())
        current_player = self.player_no
        current_board.move(i, j, self.player_no)

        while not current_board.is_finished():
          current_player = self.switch_player(current_player)
          next_move = ScorePlayer(self.player_no).get_input(current_board.board) # that's just one step

          current_board.move(next_move[0], next_move[1], current_player)

        if current_board.player_who_won == self.player_no: # if game played was won by the Player, than finish search (no way to evaluate which wining strategy is better, for now ;P)
          return [i, j]


    return ScorePlayer(self.player_no).get_input(board) # we didn't find a winning solution, so fallback to simple 1-step score based

  def switch_player(self, current_player):
    if current_player == 1:
      return 2
    else:
      return 1


  def display_class(self):
    return ASCIDisplay
    # return NullDisplay
