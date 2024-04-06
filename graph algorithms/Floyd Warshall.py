def Floyd(G):

    S = G
    for t in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                S[i][j] = min(S[i][j],S[i][t] + S[t][j])

    return S


graph = [[0, 5, math.inf, 10],
         [math.inf, 0, 3, math.inf],
         [math.inf, math.inf, 0,   1],
         [math.inf, math.inf,math.inf, 0]
         ]
print(Floyd(graph))