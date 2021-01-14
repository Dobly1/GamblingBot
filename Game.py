from abc import ABC, abstractmethod

#Abstract Game class defining what a game is
class Game(ABC):
    def __init__(self):
        self.players = []
        self.name = ""

    @abstractmethod
    def play_game(self):
        pass

