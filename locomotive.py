import pygame, pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds
from steamcloud import SteamCloud
import sgeGame
import constants

class Locomotive(Actor):
    def __init__(self):
        #Actor.__init__(self, 'locomotive')
        Actor.__init__(self, 'lok-70')
        locomotiveImage = Actor.__getattr__(self, "image")
        #locomotiveImage.get_rect()
        #self.rect = self.image.get_rect()
        #self.mask = pygame.mask.from_surface(self.image)

        self.bottom = constants.HEIGHT
        self.centerx = constants.WIDTH/ 2
        self.vel = 6

    def update(self):
        if keyboard.left:
            self.x -= self.vel
        if keyboard.right:
            self.x += self.vel
        self.clamp_ip(0, 0, constants.WIDTH, constants.HEIGHT)
        if self.colliderect(self):
            pass

    def launch_steamCloud(self, sgeGame):
        steamCloud = SteamCloud(self.x, self.y-50)
        sgeGame.steamClouds.append(steamCloud)        


"""
    def hit(self):
        sounds.locomotive_hit.play()
        time.sleep(3)
        sys.exit()
"""        