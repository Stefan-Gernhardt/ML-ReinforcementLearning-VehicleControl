import pygame as pg
import constants



def center_message(msg, game):
    font = pg.font.Font(None, 25)
    text = font.render(msg, True, pg.Color(0,0,0))
    text_rect = text.get_rect(center=(constants.GAMEBOARD_WIDTH/2, constants.GAMEBOARD_HEIGHT/2))
    game.screen.blit(text, text_rect)
    

def write(text, x, y):
    #GAME_FONT = pg.font.SysFont("Arial", 14)
    font = pg.font.Font(None, 25)
    text = font.render(text, 1, pg.Color(0,0,0))
    text_rect = text.get_rect(center=(constants.GAMEBOARD_WIDTH/2, y))
    return text, text_rect


def center_top_message(msg, game):
    text, text_rect = write(msg, 10, 10) # this will be centered anyhow, but at 10 height
    game.screen.blit(text, text_rect)
    
    
def message_with_background(msg, game):    
    font = pg.font.Font(None, 25)
    text = font.render(msg, True, (255, 255, 255))
    temp_surface = pg.Surface(text.get_size())
    temp_surface.fill((192, 192, 192))
    temp_surface.blit(text, (0, 0))
    game.screen.blit(temp_surface, (0, 0))
    
    
def center_message_with_background(msg, game):
    font = pg.font.Font(None, 25)
    text = font.render(msg, True, (255, 255, 255))
    temp_surface = pg.Surface(text.get_size())
    temp_surface.fill((192, 192, 192))
    temp_surface.blit(text, (0, 0))
    text_rect = text.get_rect(center=(constants.GAMEBOARD_WIDTH/2, constants.GAMEBOARD_HEIGHT/2))
    game.screen.blit(temp_surface, text_rect)
    

    