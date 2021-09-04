from pgzero.actor import Actor
import constants

class Hintergrund(Actor):

    def __init__(self, x, y):
        Actor.__init__(self, 'hintergrund1.png', midbottom=(constants.WH, constants.HEIGHT))
        #self.x = 250
        #self.y = 550
        self.alive = True
        self.vel = -1
        
    def update(self):
        self.y -= self.vel
        if(self.top < 0):
            self.alive = False
    