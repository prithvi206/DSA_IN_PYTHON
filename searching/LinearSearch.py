#Searching algorithms - Linear Search
#time complexity - O(N)

def linearSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print (linearSearch([12,23,34,45,56,78,89,90],90))