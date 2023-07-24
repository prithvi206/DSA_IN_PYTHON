import numpy as np 
twoArray = np.array([[11,12,13,14],[23,24,25,26],[34,45,67,12]])


newTwoDArray = np.insert(twoArray ,0, [[1,2,3,4]],axis=1)
#axis=1 --> column
#axis=0 --> row

newTwoDArray = np.insert(twoArray,[[1,2,3,4]],axis=0)
print(newTwoDArray)

def traversalTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

newTwoDArray = np.delete(twoArray,0,axis=0)
print(newTwoDArray)