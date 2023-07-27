class DisjointSet:
    def __init__(self,vertices,parent):
        self.vertices = vertices
        self.parent = parent
        self.rank = dict.fromkeys(vertices,0)


    def find(self,item):
        if self.parent[item]==item:
            return item
        else:
            return self.find(self.parent[item])
        

    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)