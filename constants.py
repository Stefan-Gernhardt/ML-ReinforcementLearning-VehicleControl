WIDTH, HEIGHT = 450, 725
#WIDTH, HEIGHT = 900, 955
W, H = WIDTH, HEIGHT
WH, HH = W/2, H/2
GAMEBOARD_WIDTH, GAMEBOARD_HEIGHT = WIDTH, HEIGHT

COUNT_ACTIONS = 3

LOOK_AHEAD_STEPS_Y = 3
LOOK_AHEAD_STEPS_X = 4
LOOK_AHEAD_STEPS_DRIVING = 3

DRIVE_STRAIGHT = 0
DRIVE_LEFT = 1
DRIVE_RIGHT = 2



def imageSum(image):
    rows = image.shape[0]
    cols = image.shape[1]
    
    sum = 0
    for row in range(0, rows):
        for col in range(0, cols):
            sum = sum + image[row][col]
    
    return sum


def imageSumVector(image):
    elements = image.shape[0]
    
    sum = 0
    for e in range(0, elements):
        sum = sum + image[e]
    
    return sum


