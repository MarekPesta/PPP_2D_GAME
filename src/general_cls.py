from config import *
from dataclasses import dataclass

class Music():
    '''Class used to Configure bacground music'''

    def __init__(self, vol=0.5):
        mixer.init()
        pygame.mixer.music.set_volume(vol)
        mixer.music.load(os.path.join('music', 'main_music.mp3'))

    def play(self):
        mixer.music.play(-1)

    def change(self, mausic):
        mixer.music.load(os.path.join('music', mausic))


@dataclass
class Position:
    '''Dataclass used to store position of objects'''

    x: int
    y: int

    def get(self) -> (int, int):
        return (self.x, self.y)
