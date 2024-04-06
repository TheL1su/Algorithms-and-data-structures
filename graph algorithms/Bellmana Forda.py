import math


class Node():
    def __init__(self,parent=None,distance=None):
        self.par = parent
        self.dis = distance

def Relax(u,v,V,G):
    if V[v].dis > V[u].dis + G[u][v]:
        V[v].dis = V[u].dis + G[u][v]
        V[v].par = V[u]

def Bellman(G,start):

    V = []
    for i in range(len(G)):
         vertex = Node(i)
         vertex.dis = math.inf
         vertex.par = None
         V.append(vertex)

    V[start].dis = 0

    for i in range(len(G)):
        for j in range(i+1,len(G)):

            if G[i][j] != 0:
                Relax(i,j,V,G)

    for i in range(len(G)):
        for j in range(i+1,len(G)):
            if G[i][j] != 0:
                if V[j].dis > V[i].dis + G[i][j]:
                    print("mamy ujemny cykl",i,j)

    for i in range(len(G)):
        print(V[i].dis)

G = [[0,1,0,4],[1,0,-3,0],[0,-3,0,1],[4,0,1,0]]

Bellman(G,0)