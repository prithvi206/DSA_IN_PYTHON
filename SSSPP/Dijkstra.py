#Dijkstra 

# A path is called a negative cycle if: There is a cycle (a cycle is a path of edges or vertices
#  where in vertex is reachabel form itself) so dijkstra's Algorithm


import heapq
#class for edges
class Edge:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

#class for nodes
class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        #previous node that we come to this node
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")

    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance
    
    def add_egde(self,weight , destination_vertex):
        edge = Edge(weight,self,destination_vertex)
        self.neighbors.append(edge)

#Dijkstra Algorithm
class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self,start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap,start_vertex)
        

        while self.heap:
            #pop element with lowest distance 
            actual_vertex  = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            #consider the neighbors 
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    #update the heap 
                    heapq.heappush(self.heap,target)
            actual_vertex.visited =True

    def get_shortest_path(self,vertex):
        print(f"The shortest path to the vertex is: {vertex.min_distance}" )
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor

#Step 1 - create nodes

nodeA = Node("A")
nodeB = Node("B")    
nodeC = Node("C")   
nodeD = Node("D")  
nodeE = Node("E")  
nodeF = Node("F")  
nodeG = Node("G") 
nodeH = Node("H")

#Step 2 - create edges

nodeA.add_egde(6,nodeB)
nodeA.add_egde(10,nodeC)
nodeA.add_egde(9,nodeD)
nodeB.add_egde(5,nodeD)
nodeB.add_egde(16,nodeE)
nodeB.add_egde(13,nodeF)
nodeE.add_egde(10,nodeG)
nodeC.add_egde(6,nodeD)
nodeC.add_egde(5,nodeH)
nodeC.add_egde(21,nodeG)
nodeD.add_egde(7,nodeH)
nodeD.add_egde(8,nodeF)
nodeF.add_egde(4,nodeE)
nodeF.add_egde(12,nodeG)
nodeH.add_egde(14,nodeG)
nodeH.add_egde(2,nodeH)


algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)