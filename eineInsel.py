import pygame as pg
import os
import sys
import random
import constants
from zustand import Zustand
import textMessage
from test.leakers import test_selftype
import random
import numpy as np
from PIL import Image
from tensorflow.python.ops.image_ops_impl import rgb_to_grayscale
from PIL.ImageOps import grayscale
import recording
from machineLearning import Model
from multiprocessing.dummy import list

VERSION = "0.1"
Autonomous_Driving = True
Autonomous_Driving_TrainingPhase = True
processOnce = True
COUNT_GAMES = 0
COUNT_SUCCESSFUL_RUNS = 0
COUNT_TRAINING_GAMES = 10000000
ALGO_WITH_FAILS = True


def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pg.image.load(os.path.join("images", i)).convert_alpha()

class Player(pg.sprite.Sprite):
    speed = 1
    highSpeed = 2
    action = 0
    modelOutput = np.zeros((1, Model.countOutputNeurons))

    def __init__(self, pos):
        super(Player, self).__init__()
        if Autonomous_Driving: 
            #self.image = load_image("lok-train.png")
            self.image = load_image("lok-70.png")
        else: 
            self.image = load_image("lok-70.png")
        
        
        #print(self.image.get_height())
        pos2 = (pos[0], pos[1]-self.image.get_height()/2)
        self.rect = self.image.get_rect(center=pos2)
        #print("Player constructor " + str(self.rect.x) + ", " + str(self.rect.y))
        self.countPixels = (self.image.get_width() + constants.LOOK_AHEAD_STEPS_X) * (self.image.get_height() + constants.LOOK_AHEAD_STEPS_Y)
        #print("Vehicle image count pixels: " + str(self.countPixels))
        self.mask = pg.mask.from_surface(self.image)
        self.leftBorder = -self.image.get_width()/2
        #print("leftBorder " + str(self.leftBorder))
        self.rightBorder = constants.GAMEBOARD_WIDTH - self.image.get_width()/2
        #print("rightBorder " + str(self.rightBorder))
        self.imageThatLeadsToModelOutput = np.zeros((self.image.get_width() + constants.LOOK_AHEAD_STEPS_X, self.image.get_height() + constants.LOOK_AHEAD_STEPS_Y))
        
    """
    def multiplyWithBitmaskNA(self, bitMaskNA, imageNA):
        rows = imageNA.shape[0]
        cols = imageNA.shape[1]
        
        returnNA = np.zeros((rows, cols))

        for x in range(0, rows):
            for y in range(0, cols):
                returnNA[x][y] = bitMaskNA[x][y] * imageNA[x][y]
                 
        return returnNA
    
    
    def createBitmaskNA(self, imageNA):
        rows = imageNA.shape[0]
        cols = imageNA.shape[1]
        
        bitMaskNA = np.zeros((rows, cols))
        
        for x in range(0, rows):
            for y in range(0, cols):
                if imageNA[x][y]>0: bitMaskNA[x][y] = 1
                
        return bitMaskNA
    
    
    def isCollision(self, imageNA):
        diffNA = imageNA - self.initialImageNA
        bitMask = self.createBitmaskNA(self.initialImageNA)
        productNA = self.multiplyWithBitmaskNA(bitMask, diffNA)
        isCollision = (np.count_nonzero(productNA) > 0)  
        return isCollision
    """
        
    def modelOutputToAction(self, modelOutput):
        drive_straight = modelOutput[0][constants.DRIVE_STRAIGHT]
        drive_left     = modelOutput[0][constants.DRIVE_LEFT]
        drive_right    = modelOutput[0][constants.DRIVE_RIGHT]
        
        #if ALGO_WITH_FAILS:
        #    if drive_left > drive_right and drive_left > drive_straight: return constants.DRIVE_LEFT
        #    if drive_right > drive_left and drive_right> drive_straight: return constants.DRIVE_RIGHT
        #    return constants.DRIVE_STRAIGHT
        #else:
        rng = random.uniform(0, 1)
        if rng < drive_straight: return constants.DRIVE_STRAIGHT
        if rng > (1-drive_right): return constants.DRIVE_RIGHT
        return constants.DRIVE_LEFT
        
        
    def update(self):
        verbose = False
        if(Autonomous_Driving):
            if verbose: print("-------------------------------------------------------")
            if verbose: print("Player::update(): countRadarImagesTaken: " + str(game.countRadarImagesTaken))
            if game.countRadarImagesTaken>0: 
                #print("currentRadarImage")
                #recording.printNP(game.currentRadarImage)
                self.imageThatLeadsToModelOutput = game.currentRadarImage
                self.modelOutput = game.model.getModelOutput(np.reshape(self.imageThatLeadsToModelOutput, (1, self.countPixels)))
                self.action = self.modelOutputToAction(self.modelOutput)
                if verbose: print("imageSum")
                if verbose: print(constants.imageSum(self.imageThatLeadsToModelOutput))
                if game.countRadarImagesTaken == 1:
                    self.initialImageNA = self.imageThatLeadsToModelOutput
                if verbose: print("collision: " + str(self.isCollision(self.imageThatLeadsToModelOutput)))    
            else: 
                self.action = constants.DRIVE_STRAIGHT


            if verbose: print("self.modelOutput")
            if verbose: print(self.modelOutput)

            #if game.hintergrund.timeTickCounter %4 == 1: self.action = constants.DRIVE_RIGHT
            #else: self.action = constants.DRIVE_STRAIGHT

            #self.action = constants.DRIVE_RIGHT
            
            if verbose: print("-> action:", end="")
            if verbose: print(self.action)
            

            self.actionToDx = [ 0, -2, 2 ]
            self.rect.x = self.rect.x + self.actionToDx[self.action]
            if verbose: print("dx:", end="")
            if verbose: print(self.actionToDx[self.action])

        else:
            keys=pg.key.get_pressed()
            
            if keys[pg.K_LSHIFT]:
                velocity = self.highSpeed
            else:
                velocity = self.speed
            
            if keys[pg.K_a] or keys[pg.K_LEFT]:
                #print("keyboard.left")
                self.rect.x = self.rect.x - velocity
                if(self.rect.x < self.leftBorder): 
                    self.rect.x = self.leftBorder
            if keys[pg.K_d] or keys[pg.K_RIGHT]:
                #print("keyboard.right")
                self.rect.x = self.rect.x + velocity
                if(self.rect.x > self.rightBorder): 
                    self.rect.x = self.rightBorder
                    
                
    def collisionLoadUpsideDownImage(self):
        if not Autonomous_Driving: self.image = load_image("lok-70-upside-down.png")
        
    def getPlayerXPosition(self):
        return self.rect.x
                    
    def getPlayerYPosition(self):
        return self.rect.y
                    
    def getPlayerWidth(self):
        return self.image.get_width()
                    
    def getPlayerHeight(self):
        return self.image.get_height()
                    
        
class Princess(pg.sprite.Sprite):
    yOffset = 668
    
    def __init__(self, pos):
        super(Princess, self).__init__()
        #self.image = load_image("princess.png")
        self.image = load_image("racestartline.png")
        
        if Autonomous_Driving: self.yOffset = self.yOffset - self.image.get_height();
         
        self.rect = self.image.get_rect(center=pos)
        self.mask = pg.mask.from_surface(self.image)
            
    def update(self, y):
        #print("princess y: " + str(self.rect.y))
        self.rect.y = self.yOffset + y


class Enemy(pg.sprite.Sprite):

    def __init__(self, pos):
        super(Enemy, self).__init__()
        self.image = pg.Surface((120, 120), pg.SRCALPHA)
        pg.draw.circle(self.image, (240, 100, 0), (60, 60), 60)
        self.rect = self.image.get_rect(center=pos)
        self.mask = pg.mask.from_surface(self.image)
        

class Hintergrund(pg.sprite.Sprite):
    timeTickCounter = 0   
    #imageName = "hintergrundGerade.png"
    #imageName = "hintergrund0.png"
    #imageName = "hintergrund1.png"
    #imageName = "hintergrund2.png"
    #imageName = "hintergrund3.png"
    imageName = "hintergrundAll.png"
    #imageName = "hintergrundKlein1.png"
    #imageName = "hintergrundKlein2.png"
    

    def __init__(self, pos):
        super(Hintergrund, self).__init__()
        #self.image = pg.Surface((120, 120), pg.SRCALPHA)
        
        self.image = load_image(self.imageName)
        
        #pg.draw.circle(self.image, (240, 100, 0), (60, 60), 60)
        #self.rect = self.image.get_rect(center=pos)
        self.rect = self.image.get_rect(midbottom=(constants.GAMEBOARD_WIDTH/2, constants.GAMEBOARD_HEIGHT))
        #self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        

    def update(self):
        self.timeTickCounter = self.timeTickCounter + 1
        # print("timeTickCounter: " + str(self.timeTickCounter))

        self.rect.y = self.rect.y + 1
        if(self.rect.y > constants.GAMEBOARD_HEIGHT): 
            self.rect.y = constants.GAMEBOARD_HEIGHT
            
        # print("background y: " + str(self.rect.y)) 
        if self.rect.y > 0:
            game.stateInsel = Zustand.GAME_OVER_WIN 
            print("end of level reached")
            
    def getYSge(self):
        return self.rect.y
                

class Game:
    countRadarImagesTaken = 0
    
    
    def __init__(self):
        pg.display.set_mode((constants.GAMEBOARD_WIDTH, constants.GAMEBOARD_HEIGHT))
        tempPlayer = Player((constants.GAMEBOARD_WIDTH/2, constants.GAMEBOARD_HEIGHT))
        self.model = Model(tempPlayer.countPixels)
        self.initGame()
        
        
    def initGame(self):
        global COUNT_GAMES
        global COUNT_SUCCESSFUL_RUNS
        print("successful runs: " + str(COUNT_SUCCESSFUL_RUNS) + "/" + str(COUNT_GAMES))
        COUNT_GAMES = COUNT_GAMES + 1
        global processOnce
        processOnce = True
        self.countRadarImagesTaken = 0
        self.stateInsel = Zustand.READY
        #self.gameRadarList = []
        
        self.recording = recording.Recording()
        #self.recorderPlayground = {}
        #self.recorderActions = {}
        #self.recoderGameState = {}
        
        self.screen = pg.display.set_mode((constants.GAMEBOARD_WIDTH, constants.GAMEBOARD_HEIGHT))
        pg.display.set_caption('Eine Insel')
        self.player = Player((constants.GAMEBOARD_WIDTH/2, constants.GAMEBOARD_HEIGHT))
        self.princess = Princess((constants.GAMEBOARD_WIDTH/2-9, constants.GAMEBOARD_HEIGHT))
        self.hintergrund = Hintergrund((constants.GAMEBOARD_WIDTH/2, constants.GAMEBOARD_HEIGHT/2))
        self.hintergrundSpriteGroup = pg.sprite.Group(self.hintergrund)
        self.enemies = pg.sprite.Group(Enemy((constants.GAMEBOARD_WIDTH, constants.GAMEBOARD_HEIGHT/2)))
        
        #self.all_sprites = pg.sprite.Group(self.princess, self.player, self.hintergrundSprite, self.enemies)
        self.all_sprites = pg.sprite.Group(self.princess, self.player, self.hintergrundSpriteGroup) 
        self.done = False
        self.clock = pg.time.Clock()

        if Autonomous_Driving: self.stateInsel = Zustand.PLAY
        else: self.stateInsel = Zustand.READY
        
        

    def run(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.flip()
            self.clock.tick(60)


    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if self.stateInsel == Zustand.GAME_OVER_LOST or self.stateInsel == Zustand.GAME_OVER_WIN:
                    if event.key == pg.K_y:
                        self.initGame()
                    if event.key == pg.K_n:
                        self.done = True
                     
                if self.stateInsel == Zustand.READY:
                    self.stateInsel = Zustand.PLAY
                
                if event.key == pg.K_LEFT:
                    #print("left key")
                    #location -= 1
                    pass
                if event.key == pg.K_RIGHT:
                    #print("right key")
                    #location += 1
                    pass            
                if event.key == pg.K_q:
                    print("quit game")
                    self.done = True
            
            if event.type == pg.QUIT:
                print("quit game")
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                # self.player.rect.center = event.pos
                if self.stateInsel == Zustand.READY:
                    self.stateInsel = Zustand.PLAY
                    

    def update(self):
        # Check if the player collides with an enemy sprite. The
        # `pygame.sprite.collide_mask` callback uses the `mask`
        # attributes of the sprites for the collision detection.
        if self.stateInsel == Zustand.PLAY:
            if pg.sprite.spritecollide(self.player, self.enemies, False, pg.sprite.collide_mask):
                pg.display.set_caption('collision with enemies')
            else:
                if pg.sprite.spritecollide(self.player, self.hintergrundSpriteGroup, False, pg.sprite.collide_mask): 
                    pg.display.set_caption('collision with background')
                    self.player.collisionLoadUpsideDownImage()
                    self.stateInsel = Zustand.Collision
                    if Autonomous_Driving:
                        if hasattr(self, 'currentRadarImage'): self.recording.reportCollision(self.hintergrund.timeTickCounter, self.currentRadarImage)
                else:
                    pg.display.set_caption('no collision')

        if self.stateInsel == Zustand.PLAY:
            self.player.update()
            self.hintergrundSpriteGroup.update() 
            #numberOfSprites = self.hintergrundSprite.len()
            for hs in self.hintergrundSpriteGroup:
                y = hs.getYSge()
                #print("hintergrund y in update: " + str(y))
                self.princess.update(y)

        if self.stateInsel == Zustand.Collision:
            self.player.update()
            for hs in self.hintergrundSpriteGroup:
                y = hs.getYSge()
                self.princess.update(y)
                
        #game.recoderGameState[game.hintergrund.timeTickCounter] = self.stateInsel 



    """
    def addRadarToList(self, imgGrid, tickCounter):
        print("-----------")
        print("tickcounter: " + str(tickCounter))
        print("radarlist length: " + str(self.gameRadarList.__len__()))
        if self.gameRadarList.__len__() <= tickCounter:
            self.gameRadarList.append(imgGrid)
            print("size of radarList: " + str(sys.getsizeof(self.gameRadarList)))
    """    

    """                
    def grayscaleSge(self, img):
        arr = pg.surfarray.array3d(img)
        #luminosity filter
        avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
        arr = np.array([[[avg] for avg in col] for col in avgs])
        return pygame.surfarray.make_surface(arr), arr / 255.0
    """                    
                
    def greyscaleSurface(self, surface: pg.Surface, x, y):
        arr = pg.surfarray.pixels3d(surface)
        mean_arr = np.dot(arr[:], [0.216, 0.587, 0.144])
        mean_arr3d = mean_arr[..., np.newaxis]
        new_arr = np.repeat(mean_arr3d[:], 1, axis=2)
        arr_normalized = new_arr / 255.0   
    
        #print("grayScaleNPArray.shape")
        #print(grayScaleNPArray.shape)
        grayScaleNPArrayReshaped = np.reshape(arr_normalized, ((x, y)))
        #print("grayScaleNPArrayReshaped.shape")
        #print(grayScaleNPArrayReshaped.shape)
        grayScaleNPArrayReshapedAndTransposed = grayScaleNPArrayReshaped.transpose()
        #print("grayScaleNPArrayReshapedAndTransposed.shape")
        #print(grayScaleNPArrayReshapedAndTransposed.shape)
        #recording.printNPFloat(grayScaleNPArrayReshapedAndTransposed)
        return grayScaleNPArrayReshapedAndTransposed    

        
    # radar (image capturing)        
    def drawRadar(self, tickCounterOffset):
        if not Autonomous_Driving: return
        
        xPaddingPlayer = constants.LOOK_AHEAD_STEPS_X 
        yPaddingPlayer = constants.LOOK_AHEAD_STEPS_Y
        xPos = game.player.getPlayerXPosition() 
        yPos = game.player.getPlayerYPosition() 
        rectx = game.player.getPlayerWidth() + xPaddingPlayer
        recty = game.player.getPlayerHeight() + yPaddingPlayer

        partOfScreen = pg.Surface((rectx, recty))
        partOfScreen.blit(game.screen, (0, 0), (xPos - (xPaddingPlayer/2), yPos - yPaddingPlayer, rectx, recty))
        grayScaleNPArray = self.greyscaleSurface(partOfScreen, rectx, recty)

        
        self.countRadarImagesTaken = self.countRadarImagesTaken + 1 
        self.currentRadarImage = grayScaleNPArray
        
        #print("draw: timeTickCounter: " + str(self.hintergrund.timeTickCounter))
        #self.addRadarToList(grayScaleNPArray, self.hintergrund.timeTickCounter)
        
        #if (self.hintergrund.timeTickCounter+tickCounterOffset) in self.recorderPlayground:
        #    print("Warning: duplicate recording at tick: " + str(self.hintergrund.timeTickCounter))
        #self.recorderPlayground[self.hintergrund.timeTickCounter + tickCounterOffset] = grayScaleNPArray
        #self.recording.addRecordImage(self.hintergrund.timeTickCounter, grayScaleNPArray)
        
        self.recording.addRecord(self.hintergrund.timeTickCounter + tickCounterOffset, self.player.imageThatLeadsToModelOutput, self.player.modelOutput, self.player.action, grayScaleNPArray, self.stateInsel) 
        
        #if self.hintergrund.timeTickCounter == 1 or self.hintergrund.timeTickCounter == 2:
        #    print("ticks: " + str(self.hintergrund.timeTickCounter))
        #    print(self.recorderPlayground[self.hintergrund.timeTickCounter])
        #    print(grayScaleNPArray.ndim)
        #    print(grayScaleNPArray.shape)
        #    print(grayScaleNPArray.size)
        #print("grayScaleNPArray")
        #recording.printNPFloat(grayScaleNPArray)
        #print("grayScaleNPArray.shape")
        #print(grayScaleNPArray.shape)
            
        game.screen.blit(partOfScreen, (constants.W - rectx, 0))  
            


    def draw(self):
        #print("game state draw: " + str(self.stateInsel))
        
        if self.stateInsel == Zustand.READY:
            game.screen.fill((255, 255, 255))    
            textMessage.center_message_with_background("press any key to start", game)
            
        
        if self.stateInsel == Zustand.PLAY:
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            self.drawRadar(0)

        if self.stateInsel == Zustand.Collision:
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            textMessage.center_message_with_background("Collision", game)
            self.stateInsel = Zustand.GAME_OVER_LOST
            print("You lost. Game over. Play again (yes/no)?")


        global processOnce
        if self.stateInsel == Zustand.GAME_OVER_LOST:
            textMessage.center_message_with_background("You lost. Game over. Play again (yes/no)?", game)
            if processOnce:
                self.drawRadar(1)
                processOnce = False             
                if Autonomous_Driving: 
                    self.training()
                    global COUNT_GAMES
                    if COUNT_GAMES < COUNT_TRAINING_GAMES: self.initGame()
                    else: self.done = True

         
        if self.stateInsel == Zustand.GAME_OVER_WIN:
            textMessage.center_message_with_background("You won. Game over. Play again (yes/no)?", game)
            if processOnce:
                self.drawRadar(1)
                processOnce = False             
                if Autonomous_Driving: 
                    self.training()
                    global COUNT_SUCCESSFUL_RUNS
                    COUNT_SUCCESSFUL_RUNS = COUNT_SUCCESSFUL_RUNS + 1
                    if COUNT_GAMES < COUNT_TRAINING_GAMES: self.initGame()
                    else: self.done = True


    def training(self):
        print ("=====================================================================")
        print ("start learning")
        self.recording.processRecordings(False)
        
        if ALGO_WITH_FAILS:
            imageData, learningVectorData = game.recording.getTrainigDataWithFails(self.player.countPixels)
        else:
            imageData, learningVectorData = game.recording.getTrainigData(self.player.countPixels)
        
        self.model.training(imageData, self.player.countPixels, learningVectorData, constants.COUNT_ACTIONS, ALGO_WITH_FAILS)
        print ()
        print ()
        self.model.saveModel(ALGO_WITH_FAILS)



if __name__ == '__main__':
    #if len(sys.argv) > 1: Autonomous_Driving = True
        
    pg.init()
    game = Game()
    game.model.loadModel(ALGO_WITH_FAILS)
    game.run()
    game.model.saveModel(ALGO_WITH_FAILS)
    print("game quit")
    pg.quit()
    
    
    
"""
https://stackoverflow.com/questions/51243222/how-can-i-change-the-resolution-of-my-screen-in-pygame

window.blit(pygame.transform.scale(screen,(windoWidth,windowHeight)),(0,0))
That should work.

EDIT: As the Ted's comments suggests it will be more easy to understand like this.

resized_screen = pygame.transform.scale(screen, (windoWidth,windowHeight)) 
window.blit(resized_screen, (0, 0))

https://www.google.com/search?q=pygame+decrease+resolution&rlz=1C1CHBF_deDE896DE896&oq=pygame+decrease+res&aqs=chrome.1.69i57j33i160l2.6594j0j7&sourceid=chrome&ie=UTF-8

"""   

""" todo list
- resize of screen
- 

"""