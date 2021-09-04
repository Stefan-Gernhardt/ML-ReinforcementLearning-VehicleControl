from locomotive import Locomotive
from zustand import Zustand
from hinterGrund import Hintergrund
import pygame as pg

class SgeGame:
    def __init__(self):
        self.state = Zustand.READY
        self.locomotive = Locomotive()
        self.steamClouds = []
        self.hintergrund = Hintergrund(0, 0)

    def get_ready(self):
        self.state = Zustand.READY
        self.locomotive = Locomotive()

    def continue_to_play(self):
        self.state = Zustand.PLAY
        #print ("Zustand continue to play")

    def update(self):
        for actor in self.steamClouds:
        #for actor in self.steamClouds + self.bombs + self.ufos:
            actor.update()
        self.steamClouds = [r for r in self.steamClouds if r.alive]
            
        self.hintergrund.update()
        self.locomotive.update()
        
        if self.locomotive.colliderect(self.hintergrund):
            pg.display.set_caption('collision')
        else:
            pg.display.set_caption('no collision')

