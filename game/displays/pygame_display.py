import pygame

SCREEN_SIZE = (600, 600)
BORDER_COLOR = (123, 123, 123)
class PygameDisplay:
  def __init__(self, board):
    pygame.init()

    self.window = pygame.display.set_mode(SCREEN_SIZE)
    self.board = board

    self.step_x = SCREEN_SIZE[0]/self.board.x_size
    self.step_y = SCREEN_SIZE[1]/self.board.x_size
    self.window.fill((0,0,0))

  def draw(self):
    self.draw_board()
    self.draw_selections()
    pygame.display.update()

  def draw_board(self):
    for i in range(1, self.board.x_size):
      pygame.draw.line(self.window, BORDER_COLOR, (0, self.step_x*i), (SCREEN_SIZE[1], self.step_x*i), 2)

    for i in range(1, self.board.y_size):
      pygame.draw.line(self.window, BORDER_COLOR, (self.step_y*i, 0), (self.step_y*i, SCREEN_SIZE[0]), 2)


  def draw_selections(self):
    for i in range(0, self.board.x_size):
      for j in range(0, self.board.y_size):
        x = self.step_x * i
        y = self.step_y * j
        if self.board.board[i, j] == 1:
          self.draw_x(x , y)
        else:
          if self.board.board[i, j] == 2:
            self.draw_o(x , y)


  def draw_x(self, x, y):
    pygame.draw.line(self.window, BORDER_COLOR, (x, y), (x + self.step_x, y + self.step_y), 2)
    pygame.draw.line(self.window, BORDER_COLOR, (x, y + self.step_y), (x + self.step_x, y), 2)

  def draw_o(self, x, y):
    pos = (int(x + self.step_x/2), int(y + self.step_y/2))
    r = int(self.step_x/2)
    pygame.draw.circle(self.window, BORDER_COLOR, pos, r, 2)


  def input(self, x, y, current_player): # here it's a raw mouse input (x & y are screen coordinates)
    print("x: ", x, "y: ", y)
    board_x = int(x / 200)
    board_y = int(y / 200)
    self.board.move(board_x, board_y, current_player)
