from enum import Enum


class Zustand(Enum):
    READY = 0
    PLAY = 1
    HIT = 2
    Collision = 3
    GAME_OVER_LOST = 4    
    GAME_OVER_WIN = 5