class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    def add_edges(self,s,d,w):
        self.graph.append([s,d,w])

    def addNode(self,value):
        self.nodes.append(value)

    def print_solution(self,dist):
        print("Vertex Distance from source")
        for key,value in dist.items():
            print(' '+ key, ': ',value)

    def bellmanFord(self,src):
        dist = {i : float("Inf") for i in self.nodes}
        dist[src]=0
        for _ in range(self.v-1):
            for s , d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + dist[w]

        for s, d,w in self.graph:
            if dist[s] !=float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                return 
            
        self.print_solution(dist)

