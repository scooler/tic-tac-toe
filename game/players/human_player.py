class HumanPlayer:
  def get_input(self, board):
    key = input("use keys 1-9 for fields 1|2|3 etc\n>")
    key = int(key) - 1
    board_y = key % 3
    board_x = int(key / 3)
    return [board_x, board_y]