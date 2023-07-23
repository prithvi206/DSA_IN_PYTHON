class Heap:
    def __init__(self,size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size+1

def peekofHeap(rootNode):
    if not rootNode:
        return
    
    else:
        return rootNode.customList[1]
    
def sizeofHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.heapSize
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.custom[i])

def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex =int(index/2)
    if index <=1:
        return 
    if heapType == "Min":
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index]= rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] =temp 
        heapifyTreeInsert(rootNode,parentIndex,heapType)
    elif heapType == "Max":
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)


def insertNode(rootNode,nodeValue,heapType):
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapsize+1]=nodeValue
    rootNode.heapSize+=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return "The value has been successfully inserted"


def heapifyTreeExtract(rootNode,index,heaptType):
    leftIndex = index*2
    rightIndex = index*2 +1
    swapChild =0

    if rootNode.heapSize <leftIndex:
        return 
    elif rootNode.heapSize == leftIndex:
        if heaptType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return 
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode[leftIndex]
                rootNode.customList[leftIndex]=temp
    else:
        if heaptType=="Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
                return
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
            heapifyTreeExtract(rootNode,swapChild,heaptType)

def extractNode(rootNode,heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.custom[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractNode



def deleteEntireBP(rootNode):
    rootNode.customList = None