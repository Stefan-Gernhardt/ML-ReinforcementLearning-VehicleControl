import sys
import numpy as np
import constants

#####################################################################################
def printNP(npa):
    rows = npa.shape[0]
    cols = npa.shape[1]

    for row in range (0, rows):
        for col in range(0, cols):
            if npa[row][col] > 0: 
                print("X", end='')
            else: 
                print("0", end='')
        print()


#####################################################################################
def printNPFloat(npa):
    rows = npa.shape[0]
    cols = npa.shape[1]

    for row in range (0, rows):
        for col in range(0, cols):
            print(str(npa[row][col]) + " ", end='')
        print()
        
        
#####################################################################################
def printNPFloatWithComma(npa):
    rows = npa.shape[0]
    cols = npa.shape[1]

    print("    imageNA = np.array([")
    for row in range (0, rows):
        print("        [", end='')
        for col in range(0, cols):
            v = npa[row][col]
            s = str(v).replace("[", "").replace("]", "")
            if col == cols-1: print(str(s) + "]", end='')
            else:        print(str(s) + ", ", end='')
        if row == rows-1: print(", ")
        else: print(", ")
    print("    ])")
    


#####################################################################################
class Record():

    def __init__(self, imageThatLeadsToModelOutput, modelOutput, action, imageNA, state):
        self.imageThatLeadsToModelOutput = imageThatLeadsToModelOutput
        self.modelOutput                 = modelOutput
        self.action                      = action
        self.imageNA                     = imageNA
        self.state                       = state
        self.collision                   = False 
        self.collisionPygame             = False 
        self.collisionPygameImage        = imageThatLeadsToModelOutput 
        #self.isInitial                   = True
        self.canBeUsedForTraining        = False
        self.learningVector              = np.zeros(constants.COUNT_ACTIONS)
                        
       
    # example output for imageNA:
    #[
    #    [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
    #    [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
    #    [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
    #    [0., 0., 0., 0.12705882, 0.48932157, 0.48932157, 0.48932157], 
    #    [0., 0., 0.48667451, 0.48667451, 0.48932157, 0.48932157, 0.48932157], 
    #    [0., 0., 0.48667451, 0.48667451, 0.48932157, 0.48932157, 0.48932157], 
    #    [0., 0., 0.12705882, 0.01114118, 0.48932157, 0.48932157, 0.48932157], 
    #]

    

#####################################################################################    
class Recording():
    # recordStore[n].modelOutput leads to recordStore[n].action leads to recordStore[n].image leads to state recordStore[n+1].state
    # be aware that the action and resulting image are in the same record. And the resulting game state is one record ahead (n+1)
    # the output of the neuronal net that leads to action(n) is also in record(n)
    # neuronalNetOutput(n) -> action(n) -> image(n) -> gamestate(n+1)
    
    collisionTimetick = -1  
    
    def __init__(self):
        self.keyForInitialRecord = -1
        self.recordStore = {}
        
    #pass or something else    #recordStoreAction    = {}
    #recordStoreImage     = {}
    #recordStoreGamestate = {}

    #def addRecordAction(self, timetick, action):
    #    if timetick in self.recordStoreAction:
    #        print("Warning: duplicate recording in recordStoreAction at tick: " + str(timetick))
    #    self.recordStoreAction[timetick] = action
        
    
    #def addRecordImage(self, timetick, image):
    #    if timetick in self.recordStoreImage:
    #        print("Warning: duplicate recording in recordStoreImage at tick: " + str(timetick))
    #    self.recordStoreImage[timetick] = image
        
    
    #def addRecordGamestate(self, timetick, gamestate):
    #    if timetick in self.recordStoreAction:
    #        print("Warning: duplicate recording in recordStoregamestate at tick: " + str(timetick))
    #    self.recordStoreGamestate[timetick] = gamestate

        
    #def printRecording(self):
    #    print("ticks: " + str(len(self.recordStoreAction)) + " " + str(len(self.recordStoreImage)) + " " + str(len(self.recordStoreGamestate)) + " " )
    #    
    #    for key in self.recordStoreImage:
    #        print(str(key))
    #        print("action: " + str(self.recordStoreAction[key]))
    #        #printNPFloat(recordStoreImage[key])
    #        print("GameState: " + str(self.recordStoreGamestate[key]))
            
    def reportCollision(self, timetick, imageNA):
        self.collisionTimetick = timetick
        self.collisionImageNA  = imageNA
        if timetick in self.recordStore:
            self.recordStore[timetick].collisionPygame = True
            self.recordStore[timetick].collisionPygameImage = imageNA


    def addRecord(self, timetick, imageNAThatLeadsToModelOutput, modelOutput, action, imageNA, state, verbose=False):
        if verbose: print("addRecord( timetick: " + str(timetick)  + ", action: " + str(action)  + ", zustand: " + str(state) + ")")
        if verbose: print("imageNAThatLeadsToModelOutput")
        if verbose: printNPFloatWithComma(imageNAThatLeadsToModelOutput)
        if verbose: print("modelOutput")
        if verbose: print(modelOutput)
        if verbose: print("imageNA")
        if verbose: printNPFloatWithComma(imageNA)
        
        if timetick in self.recordStore:
            print("Warning: duplicate recording in recordStore at tick: " + str(timetick))
        
        self.recordStore[timetick] = Record(imageNAThatLeadsToModelOutput, modelOutput, action, imageNA, state)

    
    def multiplyWithBitmaskNA(self, bitMaskNA, imageNA):
        #print("bitMaskNA")
        #printNPFloat(bitMaskNA)
        #print("imageNA begin")
        #printNPFloat(imageNA)
        #print("imageNA end")
        
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
                #print (imageNA[x,y])
                if imageNA[x][y]>0: bitMaskNA[x][y] = 1
                
        return bitMaskNA
    
    
    def isImageInitial(self, imageNA, verbose=False):
        initialImageNA = self.recordStore[self.keyForInitialRecord].imageNA
        diffNA = imageNA - initialImageNA
        
        if verbose: print("initial Image:")
        if verbose: printNPFloat(initialImageNA) 
        
        if verbose: print("diffNA")
        if verbose: printNPFloat(diffNA) 
        
        bitMask = self.createBitmaskNA(initialImageNA)
        if verbose: print("bitMask")
        if verbose: printNPFloat(bitMask)
         
        productNA = self.multiplyWithBitmaskNA(bitMask, diffNA)
        if verbose: print("productNA")
        if verbose: printNPFloat(productNA)
        #isCollision = (np.count_nonzero(productNA) > 0)  
        
        isImageInitialReturnValue = (np.count_nonzero(diffNA) == 0)
        
        return isImageInitialReturnValue #, isCollision
    

    def computeLabelVectorOnHitPrediction(self, prediction, indexHitPrediction, learningRate):
        actionVector = np.zeros((1, constants.COUNT_ACTIONS))
        actionVector[0][indexHitPrediction] = 1.0
    
        y = prediction + (learningRate * (actionVector - prediction))
        return y

        
    def computeLabelVectorOnHitPredictionLearningRate1(self, prediction, indexHitPrediction):
        actionVector = np.zeros((1, constants.COUNT_ACTIONS))
        actionVector[0][indexHitPrediction] = 1.0
        return actionVector
        
        
    def computeLabelVectorOnFailedPredictionLearningRate1(self, prediction, indexToValueToZero):
        y = np.zeros((1, constants.COUNT_ACTIONS))
    
        value = prediction[0][indexToValueToZero]
        
        gain = (1.0 * value) / (1.0 * (constants.COUNT_ACTIONS-1))
        for i in range(0, constants.COUNT_ACTIONS):
            y[0][i] = prediction[0][i] + gain
        y[0][indexToValueToZero] = 0
        return y
    
    
    def computeLabelVectorOnFailedPrediction(self, prediction, indexToValueToZero, learningRate):
        y = np.zeros((1, constants.COUNT_ACTIONS))
    
        value = prediction[0][indexToValueToZero]
        valueLearningRate = learningRate * value
        
        gain = (1.0 * valueLearningRate) / (1.0 * (constants.COUNT_ACTIONS-1))
        for i in range(0, constants.COUNT_ACTIONS):
            y[0][i] = prediction[0][i] + gain
        y[0][indexToValueToZero] = value - valueLearningRate #  value - (learningRate*value) = (1-learningRate)*value 
        return y
    

    def processRecordings(self, verbose=False):
        #verbose = True
        if verbose: print("==== processRecordings =======================================================")
        if verbose: print("ticks: " + str(len(self.recordStore)))
        
        listOfIndices = []

        counter = 0
        totalNumberOfCollisions = 0
        numberOfCollisions = 0        
        for key in self.recordStore:
            counter = counter + 1
            listOfIndices.append(key)
            if verbose: print("-------------------------------------")
            if self.keyForInitialRecord == -1: self.keyForInitialRecord = key
            if verbose: print("timetick: " + str(key))
            record = self.recordStore[key]

            if verbose: print("image that leads to model")
            if verbose: printNPFloat(record.imageThatLeadsToModelOutput)
            if verbose: print(constants.imageSum(record.imageThatLeadsToModelOutput))
            if verbose: print("modelOutput: " + str(record.modelOutput))
            if verbose: print("action: " + str(record.action))
            if verbose: print("resulting image")
            if verbose: printNPFloat(record.imageNA)
            if verbose: print(constants.imageSum(record.imageNA))
            
            # initial image
            #initial = self.isImageInitial(record.imageNA, False)
            #record.isInitial = initial
            #if verbose: print("initial image: " + str(initial))

            # collision
            collision = record.collisionPygame
            if collision: totalNumberOfCollisions = totalNumberOfCollisions + 1
            record.collision = collision
            if verbose: print("collision: " + str(collision))

            if verbose: print("GameState: " + str(record.state))
            record.canBeUsedForTraining = numberOfCollisions <= 0
            if counter == 1: record.canBeUsedForTraining = False
            if verbose: print("canBeUsedForTraining: " + str(record.canBeUsedForTraining))

            if numberOfCollisions == 0:            
                if collision: 
                    record.learningVector = self.computeLabelVectorOnFailedPredictionLearningRate1(record.modelOutput, record.action)
                    if(counter >= 2):
                        lastRecord = self.recordStore[listOfIndices[counter-2]]
                        lastRecord.learningVector = self.computeLabelVectorOnFailedPrediction(lastRecord.modelOutput, lastRecord.action, 0.5)
                    numberOfCollisions = numberOfCollisions + 1
                else:
                    record.learningVector = self.computeLabelVectorOnHitPredictionLearningRate1(record.modelOutput, record.action)

            if verbose: print("record.learningVector")
            if verbose: print(record.learningVector)
            
        #if verbose: print("self.collisionTimetick")
        #if verbose: print(self.collisionTimetick)
        if totalNumberOfCollisions > 1: print("Warning: totalNumberOfCollisions>1")
            
            
    def countNumberZeros(self, na):
        countZeros = 0
        n = na.shape[0]
        for i in range(0, n):
            if na[i] == 0: countZeros = countZeros +1
        return countZeros

            
    def getTrainigDataWithFails(self, countPixels):
        verbose = False
        if verbose: print("=== getTrainigData 1 ==================================")
        if verbose: print("countPixels: " + str(countPixels))
        
        imageList = []
        learningVectorList = []
        
        countFailLearnVectors = 0
        for key in self.recordStore:
            record = self.recordStore[key]
            if verbose: print("key: " + str(key) + " canBeUsedForTraining: " + str(record.canBeUsedForTraining) + " collision: " + str(record.collision) + " colPygame: " + str(record.collisionPygame)  + "  colPygameImage: " + str(constants.imageSum(record.collisionPygameImage)) + " gameState: " + str(record.state) + " action: " + str(record.action) + "  imageUsedForModelOutput: " + str(constants.imageSum(record.imageThatLeadsToModelOutput)) + "  modelOutput: " + str(record.modelOutput) + "  learningVector: " + str(record.learningVector) + "  image after action: " + str(constants.imageSum(record.imageNA)) )
            if record.canBeUsedForTraining:
                imageList.append(np.reshape(record.imageThatLeadsToModelOutput, (countPixels)))
                learningVectorList.append(np.reshape(record.learningVector, (constants.COUNT_ACTIONS)))
                if self.countNumberZeros(np.reshape(record.learningVector, (constants.COUNT_ACTIONS))) == 1: countFailLearnVectors = countFailLearnVectors + 1          
            
        if countFailLearnVectors > 1: print ("Warning: countFailLearnVectors > 1")   
         
        return np.array(imageList), np.array(learningVectorList)
    

    def getTrainigData(self, countPixels):
        verbose = False
        if verbose: print("=== getTrainigData 2 ==================================")
        if verbose: print("countPixels: " + str(countPixels))
        
        imageList = []
        learningVectorList = []

        collisionAtTheEnd = False
        countCollisions = 0
        for key in self.recordStore:
            record = self.recordStore[key]
            if record.collision: collisionAtTheEnd = True
            if verbose: print("key: " + str(key) + " canBeUsedForTraining: " + str(record.canBeUsedForTraining) + " collision: " + str(record.collision) + " action: " + str(record.action) + "  modelOutput: " + str(record.modelOutput) + "  learningVector: " + str(record.learningVector))
            if record.canBeUsedForTraining:
                if record.collision:
                    pass
                else:
                    imageList.append(np.reshape(record.imageThatLeadsToModelOutput, (countPixels)))
                    learningVectorList.append(np.reshape(record.learningVector, (constants.COUNT_ACTIONS)))
                    if self.countNumberZeros(np.reshape(record.learningVector, (constants.COUNT_ACTIONS))) == 1: countCollisions = countCollisions + 1          
            
        if countCollisions > 1: print ("Warning: countCollisions > 1")
        
        #print(learningVectorList)
        if collisionAtTheEnd:
            imageList = imageList[0:len(imageList)-constants.LOOK_AHEAD_STEPS_DRIVING]
            learningVectorList = learningVectorList[0:len(learningVectorList)-constants.LOOK_AHEAD_STEPS_DRIVING]
        
        #print(learningVectorList)
        return np.array(imageList), np.array(learningVectorList)

""" Example output
-------------------------------------
timetick: 11
action: 0
image (record)
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.12705882] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48667451] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48667451] [0.48932157] [0.48932157] 
[0.] [0.] [0.12705882] [0.01114118] [0.12705882] [0.48932157] [0.48932157] 
productNA
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
initial image: False
collision: False
GameState: Zustand.PLAY
-------------------------------------
timetick: 12
action: 0
image (record)
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.12705882] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48667451] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48667451] [0.48932157] [0.48932157] 
[0.] [0.] [0.12705882] [0.01114118] [0.12705882] [0.48932157] [0.48932157] 
productNA
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
initial image: False
collision: False
GameState: Zustand.PLAY
-------------------------------------
timetick: 13
action: 0
image (record)
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.12705882] [0.] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48667451] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48667451] [0.48932157] [0.48932157] 
[0.] [0.] [0.12705882] [0.01114118] [0.12705882] [0.48932157] [0.48932157] 
productNA
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
initial image: False
collision: False
GameState: Zustand.PLAY
-------------------------------------
timetick: 14
action: 1
image (record)
[0.] [0.] [0.] [0.] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.12705882] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.12705882] [0.01114118] [0.48932157] [0.48932157] [0.48932157] 
productNA
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0026470588235293913 0.0 0.0 
0.0 0.0 0.0 0.0 0.0026470588235293913 0.0 0.0 
0.0 0.0 0.0 0.0 0.36226274509803924 0.0 0.0 
initial image: False
collision: True
GameState: Zustand.PLAY
-------------------------------------
timetick: 15
action: 0
image (record)
[0.] [0.] [0.] [0.] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.] [0.12705882] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.48667451] [0.48667451] [0.48932157] [0.48932157] [0.48932157] 
[0.] [0.] [0.12705882] [0.01114118] [0.48932157] [0.48932157] [0.48932157] 
productNA
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0026470588235293913 0.0 0.0 
0.0 0.0 0.0 0.0 0.0026470588235293913 0.0 0.0 
0.0 0.0 0.0 0.0 0.36226274509803924 0.0 0.0 
initial image: False
collision: True
GameState: Zustand.Collision
"""