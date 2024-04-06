from queue import PriorityQueue



def Prima(G,n,start):

    MSTset = [False for _ in range(n)]
    q = PriorityQueue()

    cnt= 0
    Result = []
    MSTset[start] = True

    for i in range(len(G[start])):
        q.put((G[start][i][1], start, G[start][i][0]))

    while True:

        vertex = q.get()
        while MSTset[vertex[2]] is True:
            if q.qsize() == 0:
                break
            vertex = q.get()

        MSTset[vertex[2]] = True
        Result.append(vertex)
        cnt += 1
        if cnt == len(G)-1:
            break

        for i in range(len(G[vertex[2]])):
            q.put((G[vertex[2]][i][1],vertex[2],G[vertex[2]][i][0]))

    return Result

G = [[[1,1],[5,12]],
     [[0,1],[2,5],[5,7]],
     [[1,5],[3,3000],[4,4],[5,6]],
     [[2,3000],[4,9]],
     [[2,4],[3,9],[5,8]],
     [[0,12],[1,7],[2,6],[4,8]]
     ]

print(Prima(G,6,0))