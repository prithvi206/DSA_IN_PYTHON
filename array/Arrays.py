from array import *

my_array = array.array("i",[1,2,3,4])
print(my_array)

my_array.insert(0,6)
#if the index is also out of range then also it will insert to the last

def traversalArray(array):
    for i in array:
        print(i)

def accessElement(array,index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])

accessElement(my_array,3)

my_array.remove(3)


import numpy as np

np_array = np.array([],dtype=int)
print(np_array)

np_array1 = np.array([1,2,3,4])
print(np_array1)