import pygame, pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds
from random import choice, uniform

STEAM_IMAGES = ['steamcloud.png', 'steamcloud2.png']

class SteamCloud(Actor):

    def __init__(self, x, y):
        #Actor.__init__(self, choice(STEAM_IMAGES))
        Actor.__init__(self, 'steamcloud2.png')
        sounds.steamlocwhistle.play()
        self.alive = True
        self.x = x + 10
        self.y = y + 20
        self.vel = 10

    def update(self):
        self.y -= self.vel
        if(self.top < 0):
            self.alive = False
