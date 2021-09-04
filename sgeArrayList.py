'''
Created on 08.07.2021

@author: D028650
'''

import numpy as np

if __name__ == '__main__':
    sgeList = []
    
    grid = np.zeros((2, 2))
    
    sgeList.append(grid)
    
    grid = np.ones((2, 2))
    
    sgeList.append(grid)

    print(sgeList)