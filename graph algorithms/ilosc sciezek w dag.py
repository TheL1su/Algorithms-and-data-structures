class Node():

    def __init__(self,count = None,value=None,visited=None,parent=None):
        self.vis = visited
        self.par = parent
        self.val = value
        self.cnt = count


def DFS(G,start,end):

    def DFSVisit(G,vertex):
        vertex.vis = True
        row = vertex.val

        for i in range(len(G)):
            if G[row][i] == 1:
                sign = V[i]
                if i == end:
                    vertex.cnt += 1
                if sign.vis is False:
                    sign.par = vertex
                    DFSVisit(G,sign)
                vertex.cnt += sign.cnt


    V = []
    for i in range(len(G)):
        v = Node(i)
        v.val = i
        v.cnt = 0
        v.vis = False
        v.par = None
        V.append(v)

    DFSVisit(G,V[start])

    for i in range(len(G)):
        print(V[i].cnt)


T = [[0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
DFS(T,0,4)