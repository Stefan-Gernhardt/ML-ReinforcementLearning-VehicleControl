from random import choice, uniform
from enum import Enum
import pygame, pgzrun
from sgeGame import SgeGame
import constants
from zustand import Zustand
from pgzero.loaders import sounds
import sys


VERSION = "0.1"
WIDTH  = constants.WIDTH
HEIGHT = constants.HEIGHT


def center_message(text):
    screen.draw.text(text,
                    center=(constants.WH, constants.HH),
                    #midbottom=(constants.WH, constants.HEIGHT),
                    color="black",
                    fontsize=40)
    

def update():
    if sgeGame.state == Zustand.PLAY:
        sgeGame.update()    
    
    
def on_key_down():
    if sgeGame.state == Zustand.READY:
        sgeGame.state = Zustand.PLAY
        print("state transition from ready to play")
        sounds.steamlocrunningloop.play(-1) 
        return    
    

    if keyboard.space and sgeGame.state == Zustand.PLAY:
        sgeGame.locomotive.launch_steamCloud(sgeGame)    

    if keyboard.m and sgeGame.state == Zustand.PLAY:
        print("mute")
        sounds.steamlocrunningloop.stop()

    if keyboard.q:
        print("quit game")
        sys.exit()
        
def draw():
    screen.fill((255, 255, 255))    
    
    if sgeGame.state == Zustand.READY:
        center_message("press any key to start")
    
    
    if sgeGame.state == Zustand.PLAY:
        screen.fill((0, 0, 0))    
        sgeGame.hintergrund.draw();
        #screen.blit('bg256.bmp', (0, 0))
        #for actor in sgeGame.hintergrundArray + sgeGame.bombs + sgeGame.ufos:
        for actor in sgeGame.steamClouds:
            actor.draw()

        sgeGame.locomotive.draw();
    
print("pyGameZeroIsland version " + VERSION)
sgeGame = SgeGame()
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 1024)
pgzrun.go()


"""
todo:
- in main.draw just call sgeGame.draw


"""