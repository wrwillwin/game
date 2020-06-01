# author=wrwillwin
from abc import abstractmethod

@abstractmethod
class game_role(metaclass=abstractmethod):
    def farm(self):
        pass
    