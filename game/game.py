
from .pygame.display import UIDisplay

class Game:
  def __init__(self):
    pass

  def start(self):
    self.setup()
    self.game_loop()

  def setup(self):
    self.display = UIDisplay()


  def game_loop(self):
    while True:
      self.display.draw()
