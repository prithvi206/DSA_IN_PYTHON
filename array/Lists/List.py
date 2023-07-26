#Conditional List Comprehension
#new_list = [new_item for item in list if condition]

shoppingList = ['Milk','Cheese','Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")



myList = [1,2,3,4,5,6,7,8]
myList[2]=33
print(myList)

myList.insert(0,11)
print(myList)

myList.append(55)
print(myList)

newList = [11,12,13,14]
myList.extend(newList)

if 12 in newList:
    print("True")


#linear search
def linear_search(p_list,p_target):
    for i , value in enumerate(p_list):
        if value ==  p_target:
            return i
    return -1