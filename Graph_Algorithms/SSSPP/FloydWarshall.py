INF = 9999

def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF" ,end=" ")
            else:
                print(distance[i][j],end=" ")

        print(" ")

def floydWarshall(nV , G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] =  min(distance[i][j],distance[i]+[j])

    printSolution(nV,distance)



