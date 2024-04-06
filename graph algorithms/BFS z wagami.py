from queue import PriorityQueue





def BFS_z_wagami(T,start,end):

    q = PriorityQueue()
    go = start
    Vertex = [False for _ in range(len(T))]
    Distance = [0 for _ in range(len(T))]
    Vertex[start] = True

    #start
    for i in range(len(T)):
        if T[go][i] != 0:
            q.put((T[go][i],i,T[go][i]))

    while True:
        p = q.get()
        while Vertex[p[1]] is True:
            if q.qsize() == 0:
                if Distance[end] > 0:
                    return Distance[end]
                else:
                    return -1
            p = q.get()

        Distance[p[1]] = p[0]
        Vertex[p[1]] = True
        go = p[1]
        if p[2] >= 2:
            q.put((p[0],go,p[2]-1))
        else:
            for i in range(len(T)):
                if T[go][i] != 0 and Vertex[i] is False:
                    if T[go][i] == 1:
                        q.put((p[0] + 1,i,1))
                    if T[go][i] >= 2:
                        q.put((p[0] + 2,i,T[go][i]))



T = [[0,2,0,1,2,1,2,0,0,0],
     [2,0,2,0,1,0,0,0,0,0],
     [0,2,0,0,1,0,0,2,2,0],
     [1,0,0,0,1,0,1,1,0,0],
     [2,1,1,1,0,0,0,1,0,0],
     [1,0,0,0,0,0,1,0,0,0],
     [2,0,0,1,0,1,0,1,0,0],
     [0,0,2,1,1,0,1,0,1,0],
     [0,0,2,0,0,0,0,1,0,2],
     [0,0,0,0,0,0,0,0,2,0]]

print(BFS_z_wagami(T,0,9))
