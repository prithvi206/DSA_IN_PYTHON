from array import *

# 1. Create an array and traverse
my_array = array('i',[1,2,3,4,5])

for i in my_array:
    print(i)

# 2. Access individual elements through indexes
print(my_array[0])

# 3. Append any value in an array using insert() method
my_array.append(4)
print(my_array)

#4. Insert value in an array using insert() method
my_array.insert(3,11)

#5. Extend python array using extend() method
my_array1 = array("i",[10,11,12])
my_array.extend(my_array1)
print(my_array)

#6. Add items from list into array using fromlist() method
tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)

#7. Remove any array element using remove() method
my_array.remove(11)
print(my_array)

#8. Remove last array element using pop() method
my_array.pop()
print(my_array)

#9.Fetch any element its index using index() method 
print(my_array.index(21))

#10. Reverse a python array using reverse() method
my_array.reverse()
print(my_array)

#11. Check for number of occurences of an element using count() method
my_array.count(11)

