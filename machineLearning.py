from tensorflow.keras.layers import Dense,Flatten, InputLayer
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adam
import numpy as np
from pandas.core.window.indexers import BaseIndexer
import constants


class Model():
    fileNameTrainedNet = "trainednet"
    countInputNeurons = 0
    countOutputNeurons = 3  # neuron0 = drive straight, neuron1 = drive left, neuron2 drive right

    def __init__(self, countInputNeurons):
        self.countInputNeurons = countInputNeurons
        self.model = Sequential([
            #Dense(128, input_shape=(4,), activation='sigmoid'), 
            Dense(128, input_shape=(countInputNeurons,), activation='relu'), 
            #Dense(16, activation='relu') doesnt work
            #Dense(16, activation='sigmoid')
            Dense(self.countOutputNeurons, activation='softmax')
        ])
        
        #print(self.model.output_shape)
        print(self.model.summary())
        
        
        self.model.compile(
                loss=categorical_crossentropy,
                optimizer=Adam(),
                metrics=['accuracy'])

        print("init neuronal net")
        self.getModelOutput(np.ones((1, self.countInputNeurons)))
        

    def getFileName(self):
        return self.fileNameTrainedNet + "-" + str(self.countInputNeurons)
    
    
    def getFileNameImageDataNP(self):
        return self.fileNameTrainedNet + "-" + str(self.countInputNeurons) + "-" + "ImagesNP.csv"
    
    
    def getFileNameTrainingVectorDataNP(self):
        return self.fileNameTrainedNet + "-" + str(self.countInputNeurons) + "-" + "TrainingVectorNP.csv"
    
    
    def loadNumpyArrayImageData(self):
        try:
            print("loadNumpyArrayImageData")
            self.dataImagesNA = np.loadtxt(self.getFileNameImageDataNP(), delimiter=',')
            print("self.dataImagesNA.shape")
            print(self.dataImagesNA.shape)
        except:
            print("loading from file " + self.getFileNameImageDataNP() + " not possible" )



    def loadNumpyArrayTrainingVectorData(self):
        try:
            print("loadNumpyArrayTrainingVectorData")
            self.dataTrainingVectorNA = np.loadtxt(self.getFileNameTrainingVectorDataNP(), delimiter=',')
            print("self.dataTrainingVectorNA.shape")
            print(self.dataTrainingVectorNA.shape)
        except:
            print("loading from file " + self.getFileNameTrainingVectorDataNP() + " not possible" )
            
            


    def loadModel(self, algoWithFails):
        try:
            print("loadModel weights")
            self.model.load_weights(self.getFileName())
        except:
            print("loading model from file " + self.getFileName() + " not possible" )
            
        
        if not algoWithFails:    
            self.loadNumpyArrayImageData()
            self.loadNumpyArrayTrainingVectorData()


    def saveNumpyArrayImageData(self):
        try:
            print("saveNumpyArrayImageData")
            if self.dataImagesNA.shape[0] <= 0: return
            np.savetxt(self.getFileNameImageDataNP(), self.dataImagesNA, delimiter=',')
        except:
            print("Saving file " + self.getFileNameImageDataNP() + " not possible" )


    def saveNumpyArrayTrainingVectorData(self):

        try:
            print("saveNumpyArrayTrainingVectorData")
            if self.dataTrainingVectorNA.shape[0] <= 0: return
            np.savetxt(self.getFileNameTrainingVectorDataNP(), self.dataTrainingVectorNA, delimiter=',')
        except:
            print("Saving file " + self.getFileNameTrainingVectorDataNP() + " not possible" )


    def saveModel(self, algoWithFails):
        try:
            print("saveModel weights")
            self.model.save_weights(self.getFileName())
        except:
            print("Saving model from file " + self.getFileName() + " not possible" )
        
        if not algoWithFails:  
            pass  
            self.saveNumpyArrayImageData()
            self.saveNumpyArrayTrainingVectorData()
            
            
    def getModelOutput(self, inputPara):
        # input = np.zeros((0, self.countInputNeurons))
        output = self.model.predict(inputPara)
        return output
    
    
    def trainingWithFails(self, imageData, learningVectorData):
        # mnist example mnist-sacred.train_fc.py
        #x_train.shape
        #(60000, 28, 28, 1)
        #y_train.shape
        # (60000, 10)
        
        # ai.other.trainRL2on2.py
        #x_train.shape
        #(1, 4)
        #y_train.shape
        #(1, 16)
                
        print("imageData.shape")
        print(imageData.shape)
        print("learningVectorData.shape")
        print(learningVectorData.shape)
        
        #imageData.shape
        #(4, 49)
        #learningVectorData.shape
        #(4, 3)
        
        
        self.model.train_on_batch(imageData, learningVectorData)
        self.dataImagesNA = imageData
        self.dataTrainingVectorNA = learningVectorData 
        
        # score = model.evaluate(x_test, y_test, verbose=0)
        
        #print("imageData.shape")
        #print(imageData.shape)
        #ix0 = imageData.shape[0] # number of images
        #ix1 = imageData.shape[1] # x
        #ix2 = imageData.shape[2] # y
        #print(ix0)
        #print(ix1)
        #print(ix2)
        
        #print("learningVectorData.shape")
        #print(learningVectorData.shape)
        #ax0 = learningVectorData.shape[0] # number of images
        #ax1 = learningVectorData.shape[1] # x
        #ax2 = learningVectorData.shape[2] # y
        #print(ax0)
        #print(ax1)
        #print(ax2)
        
        #print(learningVectorData[0])
        #print(learningVectorData[1])

        #for img in range(0, ax0):
        #    self.printNP(imageData[img])
        #    print(learningVectorData[img])
        
        
    def imageEquals(self, image1, image2):
        comparison = image1 == image2
        return comparison.all()
        

    def imageExistInImageData(self, image):
        rows = self.dataImagesNA.shape[0]
        
        for row in range(0, rows):
            if self.imageEquals(image, self.dataImagesNA[row]):
                #print("found duplicate")
                return True
        
        #print("found no duplicate")
        return False
        
        
    def appendWithoutDuplicates(self, imageData, learningVectorData):
        
        rows = imageData.shape[0]
        for row in range(0, rows):
            image = imageData[row]
            learnVector = learningVectorData[row]

            imageDataList = []
            learningVectorList = []
            
            #print("learnVector.shape")
            #print(learnVector.shape)
            
            if not self.imageExistInImageData(image):
                imageDataList.append(image)
                learningVectorList.append(learnVector)
            
                imageDataAppend = np.array(imageDataList)    
                learningVectorAppend = np.array(learningVectorList)    
        
                self.dataImagesNA = np.append(self.dataImagesNA, imageDataAppend, axis=0)
                self.dataTrainingVectorNA = np.append(self.dataTrainingVectorNA, learningVectorAppend, axis=0)
        
        
        
    def appendTrainingData(self, imageData, imageDataSize, learningVectorData, learningVectorSize):
        if hasattr(self, 'dataTrainingVectorNA'):
            #print("self.dataTrainingVectorNA exist")
            pass
        else: 
            #print("self.dataTrainingVectorNA doesnt exist")
            self.dataImagesNA         = np.empty((0, imageDataSize), float)
            self.dataTrainingVectorNA = np.empty((0, learningVectorSize), float)
        
        rows = self.dataImagesNA.shape[0]
        print("count rows training data before adding: " + str(rows))

        
        self.appendWithoutDuplicates(imageData, learningVectorData)
        
        rows = self.dataImagesNA.shape[0]
        print("count rows training data after adding:  " + str(rows))
        

        
    def training(self, imageData, imageDataSize, learningVectorData, learningVectorSize, algoWithFails):
        verbose = False
        if algoWithFails:
            if verbose: 
                rows = learningVectorData.shape[0]
                for row in range(0, rows):
                    print(" " + str(constants.imageSumVector(imageData[row])) + " ", end="")
                    print(learningVectorData[row])
             
            self.model.fit(imageData, learningVectorData, epochs=10, verbose=False)
            #loss, accuracy = self.model.train_on_batch(imageData, learningVectorData)

            loss, accuracy = self.model.evaluate(imageData, learningVectorData)
            print("accuracy: " + str(accuracy))
        else:
            self.appendTrainingData(imageData, imageDataSize, learningVectorData, learningVectorSize)
            if verbose: 
                rows = self.dataImagesNA.shape[0]
                for row in range(0, rows):
                    print(" " + str(constants.imageSumVector(self.dataImagesNA[row])) + " ", end="")
                    print(self.dataTrainingVectorNA[row])
            
            self.model.fit(self.dataImagesNA, self.dataTrainingVectorNA, epochs=10, verbose=False)
            
            loss, accuracy = self.model.evaluate(self.dataImagesNA, self.dataTrainingVectorNA)
            print("accuracy: " + str(accuracy))
        
        
        
