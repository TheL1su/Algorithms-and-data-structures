

class Node():

    def __init__(self,value=None):
        self.val = value
        self.rank = 0
        self.par = self

def find(x):
    if x != x.par:
        x.par = find(x.par)
    return x.par

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.par = x
    else:
        x.par = y
        if x.rank == y.rank:
            y.rank += 1

def Kruskal(G,n):

    graph = sorted(G,key = lambda G: G[2])

    counter = 0
    Vertex = []
    Sol = []

    for i in range(n):
        q = Node(i)
        q.val = i
        Vertex.append(q)

    index = 0
    while counter < n and index < len(G):
        first = graph[index][0]
        second = graph[index][1]

        first = Vertex[first]
        second = Vertex[second]

        x = find(first)
        y = find(second)

        if x != y:
            counter += 1
            union(x,y)
            Sol.append(graph[index])

        index += 1

    return Sol

G = [[0,1,1],[1,2,12],[2,3,6],[3,4,5],[4,5,2],[5,0,7],[5,1,8],[5,2,3],[1,3,4]]
print(Kruskal(G,6))