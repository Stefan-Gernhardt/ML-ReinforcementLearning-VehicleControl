import unittest
import numpy as np
import recording
import zustand
import constants


class Test_Recording(unittest.TestCase):
    outputModelDriveStraightNA = np.array([[0.7, 0.2, 0.1]])
    outputModelDriveRightNA = np.array([[0.1, 0.3, 0.6]])
    
    #def setup(self):
    #    pass
    
    imageNA0 = np.zeros((7, 7))

    imageNA1 = np.array([
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0.12705882, 0., 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.], 
    ])

    imageNA2 = np.array([
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0.12705882, 0., 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.], 
    ])

    imageNA3 = np.array([
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0.12705882, 0., 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.], 
    ])

    imageNA4 = np.array([
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0.12705882, 0., 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.], 
    ])

    imageNA5 = np.array([
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0., 0., 0., 0.], 
        [0., 0., 0., 0.12705882, 0., 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.], 
    ])

    imageNA6 = np.array([
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0., 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.48932157], 
    ])

    imageNA7 = np.array([
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0., 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.48932157], 
    ])

    imageNA8 = np.array([
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0., 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.48932157], 
    ])

    imageNA9 = np.array([
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0., 0., 0., 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0., 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0., 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0., 0.48932157], 
    ])

    imageNA10 = np.array([
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0.48932157, 0.48932157], 
    ])

    imageNA11 = np.array([
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0.48932157, 0.48932157], 
    ])

    imageNA12 = np.array([
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0.48932157, 0.48932157], 
    ])

    imageNA13 = np.array([
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0.48932157, 0.48932157], 
    ])
    
    imageNA14 = np.array([
        [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0., 0.12705882, 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.48932157, 0.48932157, 0.48932157], 
    ])
    
    imageNA15 = np.array([
        [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0., 0.12705882, 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48932157, 0.48932157, 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.48932157, 0.48932157, 0.48932157], 
    ])
    
    imageNA16 = np.array([
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0., 0., 0.48932157, 0.48932157], 
        [0., 0., 0., 0.12705882, 0., 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.48667451, 0.48667451, 0.48667451, 0.48932157, 0.48932157], 
        [0., 0., 0.12705882, 0.01114118, 0.12705882, 0.48932157, 0.48932157], 
    ])

    
    def compareVectors(self, vector1, vector2):
        comparison = vector1 == vector2
        return comparison.all()
        
    
    def setupCommon(self, recordingForTest):
        recordingForTest.addRecord(1,   self.imageNA0,  self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA1, zustand.Zustand.PLAY)
        recordingForTest.addRecord(2,   self.imageNA1,  self.outputModelDriveRightNA,    constants.DRIVE_RIGHT,      self.imageNA2, zustand.Zustand.PLAY)
        recordingForTest.addRecord(3,   self.imageNA2,  self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA3, zustand.Zustand.PLAY)
        recordingForTest.addRecord(4,   self.imageNA3,  self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA4, zustand.Zustand.PLAY)
        recordingForTest.addRecord(5,   self.imageNA4,  self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA5, zustand.Zustand.PLAY)
        recordingForTest.addRecord(6,   self.imageNA5,  self.outputModelDriveRightNA,    constants.DRIVE_RIGHT,      self.imageNA6, zustand.Zustand.PLAY)
        recordingForTest.addRecord(7,   self.imageNA6,  self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA7, zustand.Zustand.PLAY)
        recordingForTest.addRecord(8,   self.imageNA7,  self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA8, zustand.Zustand.PLAY)
        recordingForTest.addRecord(9,   self.imageNA8,  self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA9, zustand.Zustand.PLAY)
        recordingForTest.addRecord(10,  self.imageNA9,  self.outputModelDriveRightNA,    constants.DRIVE_RIGHT,      self.imageNA10, zustand.Zustand.PLAY)
        recordingForTest.addRecord(11,  self.imageNA10, self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA11, zustand.Zustand.PLAY)
        recordingForTest.addRecord(12,  self.imageNA11, self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA12, zustand.Zustand.PLAY)
        recordingForTest.addRecord(13,  self.imageNA12, self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA13, zustand.Zustand.PLAY)
        
    
    def setUpCrash(self, recordingForTest):
        self.setupCommon(recordingForTest)
    
        recordingForTest.addRecord(14,  self.imageNA13, self.outputModelDriveRightNA,    constants.DRIVE_RIGHT,      self.imageNA14, zustand.Zustand.PLAY)
        recordingForTest.addRecord(15,  self.imageNA14, self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA15, zustand.Zustand.GAME_OVER_LOST)
        recordingForTest.reportCollision(14, self.imageNA14)


    def setUpNoCrash(self, recordingForTest):
        self.setupCommon(recordingForTest)
    
        recordingForTest.addRecord(14,  self.imageNA13, self.outputModelDriveStraightNA, constants.DRIVE_STRAIGHT,   self.imageNA16, zustand.Zustand.GAME_OVER_WIN)

        
    def test_CrashCase(self):
        self.recordingForTestCrash = recording.Recording()
        self.setUpCrash(self.recordingForTestCrash)
        
        self.recordingForTestCrash.processRecordings(False)
        
        self.assertTrue(self.recordingForTestCrash.recordStore[1].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[2].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[3].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[4].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[5].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[6].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[7].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[8].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[9].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[10].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[11].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[12].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[13].collision == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[14].collision == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[15].collision == False)
    
        self.assertTrue(self.recordingForTestCrash.recordStore[1].canBeUsedForTraining == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[2].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[3].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[4].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[5].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[6].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[7].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[8].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[9].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[10].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[11].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[12].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[13].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[14].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[15].canBeUsedForTraining == False)
    
        """
        self.assertTrue(self.recordingForTestCrash.recordStore[1].isInitial == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[2].isInitial == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[3].isInitial == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[4].isInitial == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[5].isInitial == True)
        self.assertTrue(self.recordingForTestCrash.recordStore[6].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[7].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[8].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[9].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[10].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[11].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[12].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[13].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[14].isInitial == False)
        self.assertTrue(self.recordingForTestCrash.recordStore[15].isInitial == False)
        """
        
        
        #print(self.recordingForTestCrash.recordStore[14].learningVector)
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[1].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[2].learningVector, np.array([[0.0 , 0.0, 1.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[3].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[4].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[5].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[6].learningVector, np.array([[0.0 , 0.0, 1.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[7].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[8].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[9].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[10].learningVector, np.array([[0.0 , 0.0, 1.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[11].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[12].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[13].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[14].learningVector, np.array([[0.4 , 0.6, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[15].learningVector, np.array([[0.0 , 0.0, 0.0]])))
        
        self.assertTrue(not self.compareVectors(self.recordingForTestCrash.recordStore[1].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[1].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[2].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[2].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[3].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[3].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[4].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[4].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[5].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[5].imageNA))
        self.assertTrue(not self.compareVectors(self.recordingForTestCrash.recordStore[6].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[6].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[7].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[7].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[8].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[8].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[9].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[9].imageNA))
        self.assertTrue(not self.compareVectors(self.recordingForTestCrash.recordStore[10].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[10].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[11].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[11].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[12].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[12].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestCrash.recordStore[13].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[13].imageNA))
        self.assertTrue(not self.compareVectors(self.recordingForTestCrash.recordStore[14].imageThatLeadsToModelOutput, self.recordingForTestCrash.recordStore[14].imageNA))
        
        
    def test_NoCrashCase(self):
        self.recordingForTestNoCrash = recording.Recording()
        self.setUpNoCrash(self.recordingForTestNoCrash)
        self.recordingForTestNoCrash.processRecordings(True)
        
        self.assertTrue(self.recordingForTestNoCrash.recordStore[1].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[2].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[3].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[4].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[5].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[6].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[7].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[8].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[9].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[10].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[11].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[12].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[13].collision == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[14].collision == False)
        
        self.assertTrue(self.recordingForTestNoCrash.recordStore[1].canBeUsedForTraining == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[2].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[3].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[4].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[5].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[6].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[7].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[8].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[9].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[10].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[11].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[12].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[13].canBeUsedForTraining == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[14].canBeUsedForTraining == True)
    
        """    
        self.assertTrue(self.recordingForTestNoCrash.recordStore[1].isInitial == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[2].isInitial == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[3].isInitial == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[4].isInitial == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[5].isInitial == True)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[6].isInitial == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[7].isInitial == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[8].isInitial == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[9].isInitial == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[10].isInitial == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[11].isInitial == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[12].isInitial == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[13].isInitial == False)
        self.assertTrue(self.recordingForTestNoCrash.recordStore[14].isInitial == False)
        """

        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[1].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[2].learningVector, np.array([[0.0 , 0.0, 1.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[3].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[4].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[5].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[6].learningVector, np.array([[0.0 , 0.0, 1.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[7].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[8].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[9].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[10].learningVector, np.array([[0.0 , 0.0, 1.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[11].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[12].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[13].learningVector, np.array([[1.0 , 0.0, 0.0]])))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[14].learningVector, np.array([[1.0 , 0.0, 0.0]])))
    
        self.assertTrue(not self.compareVectors(self.recordingForTestNoCrash.recordStore[1].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[1].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[2].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[2].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[3].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[3].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[4].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[4].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[5].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[5].imageNA))
        self.assertTrue(not self.compareVectors(self.recordingForTestNoCrash.recordStore[6].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[6].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[7].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[7].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[8].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[8].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[9].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[9].imageNA))
        self.assertTrue(not self.compareVectors(self.recordingForTestNoCrash.recordStore[10].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[10].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[11].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[11].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[12].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[12].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[13].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[13].imageNA))
        self.assertTrue(self.compareVectors(self.recordingForTestNoCrash.recordStore[14].imageThatLeadsToModelOutput, self.recordingForTestNoCrash.recordStore[14].imageNA))



if __name__ == '__main__':
    unittest.main()
    
    